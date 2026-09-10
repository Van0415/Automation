from seleniumbase import BaseCase
import re
import jieba
import os
from dotenv import load_dotenv

load_dotenv()


class Main(BaseCase):
    URL = f'{os.getenv("URL")}/main/Main.jsp'

    CloseAdBtn = '//div[@data-testid="close-button-container"]'
    
    # 搜尋列與按鈕 (Locator)
    SearchInput = '//*[@data-testid="header-search-input"]'
    SearchBtn = '//*[@data-testid="header-search-button"]'
    GuessKeywords = '//*[@data-testid="keyword-item"]'
    RefreshGuessBtn = '//*[@data-testid="refresh-button"]'
    
    # 搜尋結果頁元件
    ProductCards = '//div[contains(@class, "listArea")]//li'
    ProductTitles = '//h3[contains(@class, "prdName")]'
    NoResultMsg = '//*[contains(@class, "noResult")]'

    def close_ad(self, timeout=2):
        """嘗試關閉頁面蓋版廣告"""
        try:
            self.click(Main.CloseAdBtn, timeout=timeout)
        except Exception:
            pass

    def search_keyword(self, keyword: str):
        """關鍵字搜尋"""
        self.type(Main.SearchInput, keyword)
        self.click(Main.SearchBtn)

    def assert_first_productTitles(self, keyword: str):
        """驗證搜尋結果頁的第一筆商品標題是否包含搜尋關鍵字"""
        first_product_text = self.get_text(Main.ProductTitles)
        normalize_first_product_text = Main.normalize_keyword(self, first_product_text)

        normalize_keyword = Main.normalize_keyword(self, keyword)
        keyword_list = Main.dynamic_keyword(self, normalize_keyword)

        result = any(word in normalize_first_product_text for word in keyword_list)

        self.assert_true(result, f"搜尋結果首筆標題未包含關鍵字 '{keyword}'")

    def click_first_guess_keyword(self) -> str:
        """點擊第一個推薦關鍵字，並傳回其文字內容"""
        self.wait_for_element_visible(Main.GuessKeywords)
        keyword_text = self.get_text(Main.GuessKeywords)
        self.click(Main.GuessKeywords)
        return keyword_text

    def dynamic_keyword(self, keyword):
        """動態文字斷詞處理"""
        keyword_list = [word for word in jieba.cut(keyword)]
        return keyword_list

    def normalize_keyword(self, keyword):
        """文字標準化"""
        number_list = {
        '0': '零',
        '1': '一',
        '2': '二',
        '3': '三',
        '4': '四',
        '5': '五',
        '6': '六',
        '7': '七',
        '8': '八',
        '9': '九',
        }
        zh_num_keyword = re.sub(r'\d', lambda match: number_list[match.group(0)], keyword)
        clean_and_lower_keyword = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fa5]', '', zh_num_keyword).lower()
        return clean_and_lower_keyword

    def assert_first_product_promo_titles(self, keyword: str):
        """針對'買一送一'促銷詞，比對 promo_dict 內的廣義特徵清單"""
        promo_dict = {
            "買一送一": [
            "買一送一",
            "2盒",
            "x2",
            "2入",
            "二入",
            "兩盒",
            "任選",
            "2件組",
            "二件組",
            "買1件送1件",
        ]
        }
        first_product_text = self.get_text(Main.ProductTitles)
        normalize_first_product_text = Main.normalize_keyword(self, first_product_text)

        keyword_list = Main.dynamic_keyword(self, keyword)
        promo_list = promo_dict.get(keyword, [keyword])
        promo_list.extend(keyword_list)

        result = any(
            Main.normalize_keyword(self, promo) in normalize_first_product_text
            for promo in promo_list
        )
        
        self.assert_true(result, f"搜尋結果首筆標題未包含關鍵字 '{keyword}'")