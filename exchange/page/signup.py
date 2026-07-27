from page.common import Common


class Signup:
    URL = f"{Common.URL}/signup"
    Email = '//*[@id="email"]'
    Password = '//*[@id="password"]'
    ShowPassword = '//*[contains(@class,"chakra-input__right-element")]'
    ReferralCodeUnfold = '//*[@for="referralCode"]/..//*[contains(@class,"chakra-icon")]'
    ReferralCode = '//*[@id="referralCode"]'
    Submit = '//*[@data-testid="signup"]'
    UserTerms = '//a[text()="使用者條款"]'
    PrivacyPolicy = '//a[text()="隱私權政策"]'
    LoginNow = '//*[text()="立即登入"]'
