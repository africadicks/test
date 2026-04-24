import requests
import time

url = "https://www.luobenyun.homes/api/v1/passport/comm/sendEmailVerify"

params = {
    "email": "admin@pusytroller.cf",
    "recaptcha_data": ""
}

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.luobenyun.homes",
    "Referer": "https://www.luobenyun.homes/"
}

def send_once(i):
    # 关键点：每次都 new Session = 等价“清 cookie”
    with requests.Session() as s:
        s.cookies.clear()

        resp = s.post(url, params=params, headers=headers)

        print(f"[{i}] status:", resp.status_code)
        print(resp.text)
        print("-" * 60)

        return resp.text


for i in range(1, 6):
    send_once(i)
    time.sleep(1)   # 控制节奏，避免被风控误判
