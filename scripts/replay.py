import requests
import time

url = "https://www.luobenyun.homes/api/v1/passport/comm/sendEmailVerify"

data = {
    "email": "postmaster@gov.cn",
    "recaptcha_data": ""
}

headers = {
    "User-Agent": "8848 Titanium Mobile Phone",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.luobenyun.homes",
    "Referer": "https://www.luobenyun.homes/"
}

def send_once(i):
    with requests.Session() as s:
        s.cookies.clear()

        # ✔ 这里改成 data=（POST body）
        resp = s.post(url, data=data, headers=headers)

        print(f"[{i}] status:", resp.status_code)
        print(resp.text)
        print("-" * 60)

        return resp.text


for i in range(1, 6):
    send_once(i)
    time.sleep(1)
