from page.common import Common


class Home:
    URL = Common.URL
    TopBlockRegister = '//*[text()="從新手到專業者，都能輕鬆使用！"]/..//*[text()="註冊"]'
    MidBlockRegister = '//*[text()="市場趨勢"]/..//*[text()="立即註冊"]'
    DownBlockRegister = '//*[text()="穩健收益還等什麼？"]/..//*[text()="立即註冊"]'
    MarketBuy = '//*[text()="買入"]'
    MarketSold = '//*[text()="賣出"]'
    MyAssets = '//a[text()="我的資產"]'
    SpotTrading = '//a[text()="現貨買賣"]'
    DailyCoins = '//a[text()="日日生幣"]'
    HoyabitCollege = '//a[text()="HOYA BIT 學院"]'
