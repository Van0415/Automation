from seleniumbase import BaseCase
from page.main import Main
# from page.err404 import Err404


class MainTest(BaseCase):
    def setUp(self):
        super().setUp()
        self.maximize_window()
        self.open(Main.URL)
        Main.close_ad(self)

    def test_search_valid_keyword(self):
        """搜尋一般商品名稱，應正常顯示結果且包含關鍵字"""
        keyword = "測試"
        
        Main.search_keyword(self, keyword)
        self.assert_element(Main.ProductCards)
        Main.assert_first_productTitles(self, keyword)

    def test_search_invalid_keyword(self):
        """輸入無效亂碼關鍵字，應出現無結果提示且無商品卡片"""
        invalid_keyword = "xyzqwerty999888777unreal"
        
        Main.search_keyword(self, invalid_keyword)
        self.assert_element(Main.NoResultMsg)
        self.assert_element_not_visible(Main.ProductCards)

    def test_click_guess_keyword(self):
        """點擊推薦關鍵字標籤，應順利跳轉並帶出相關商品"""
        clicked_keyword = Main.click_first_guess_keyword(self)
        self.assert_element(Main.ProductCards)
        Main.assert_first_productTitles(self, clicked_keyword)

    def test_refresh_guess_keywords(self):
        """點擊更換推薦關鍵字按鈕，應能更換推薦關鍵字"""
        first_keyword_before = self.get_text(Main.GuessKeywords)
        self.click(Main.RefreshGuessBtn)
        self.assert_text_not_visible(first_keyword_before, Main.GuessKeywords)
        first_keyword_after = self.get_text(Main.GuessKeywords)
        
        self.assert_not_equal(
            first_keyword_before, 
            first_keyword_after, 
            "刷新後推薦關鍵字未發生改變"
        )

    def test_search_promo_keyword(self):
        """搜尋買一送一，應正常顯示結果且包含關鍵字"""
        keyword = "買一送一"

        Main.search_keyword(self, keyword)
        self.assert_element(Main.ProductCards)
        Main.assert_first_product_promo_titles(self, keyword)

    def test_search_empty_keyword(self):
        """未輸入任何關鍵字直接點擊搜尋，應以placeholder搜尋"""
        default_keyword = self.get_attribute(Main.SearchInput, "placeholder")
        
        self.click(Main.SearchBtn)
        self.assert_element(Main.ProductCards)
        Main.assert_first_productTitles(self, default_keyword)

    def test_search_special_keyword(self):
        """搜尋包含符號與英文大小寫的規格，應正常顯示結果且包含關鍵字"""
        keyword = "測試-english!@#123"

        Main.search_keyword(self, keyword)
        self.assert_element(Main.ProductCards)
        Main.assert_first_productTitles(self, keyword)

    def test_search_by_pressing_enter(self):
        """輸入關鍵字後按下 Enter 鍵，應能正常觸發搜尋"""
        keyword = "測試Enter"
        
        self.type(Main.SearchInput, keyword + "\n")
        self.assert_element(Main.ProductCards)
        Main.assert_first_productTitles(self, keyword)