import os

while True:
    车牌 = input("输入车牌: ").strip()
    if "-" in 车牌:
        url = f"https://www.google.com/search?q={车牌}"
        os.popen(f"chrome.exe --incognito {url}")
