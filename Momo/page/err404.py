from seleniumbase import BaseCase
import os
from dotenv import load_dotenv

load_dotenv()

class Err404(BaseCase):
    URL = f'{os.getenv("URL")}/ecm/js/err404/EC404.html'

    NotExistTxt = '//*[text()="很抱歉，這個網頁不存在!"]'
