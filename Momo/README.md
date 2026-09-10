## 環境建置 ##
1. 複製專案
git clone <your-repository-url>
cd <your-project-folder>

2. 建立並啟用虛擬環境
python3 -m venv <your-venv-name>
source <your-venv-name>/bin/activate
   Windows (PowerShell):
   .\<your-venv-name>\Scripts\Activate.ps1

3. 安裝依賴套件
pip install --upgrade pip
pip install -r requirements.txt

## 執行測試 ##
1. 基本執行
pytest case/main_test.py

2. 加上報告
pytest case/main_test.py --html=report.html

3. 更改測試URL
URL=<your-test-url> pytest case/main_test.py
   Windows (PowerShell):
   $env:URL="<your-test-url>"; pytest case/main_test.py