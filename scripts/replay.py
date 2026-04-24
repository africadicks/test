import requests
import random
import string
import time

url = "https://www.luobenyun.homes/api/v1/passport/comm/sendEmailVerify"

headers = {
    "User-Agent": "8848 Titanium Mobile Phone",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.luobenyun.homes",
    "Referer": "https://www.luobenyun.homes/"
}

def gen_email():
    # 7位最小值
    min_val = 10**6  # 1000000
    # 12位最大值
    max_val = 10**12 - 1  # 999999999999
    num = random.randint(min_val, max_val)
    return f"{num}@qq.com"

def send(i):
    email = gen_email()

    data = {
        "email": email,
        "recaptcha_data": ""
    }

    with requests.Session() as s:
        s.cookies.clear()

        resp = s.post(url, data=data, headers=headers)

        print(f"[{i}] email: {email}")
        print("status:", resp.status_code)
        print(resp.text)
        print("-" * 60)

        return resp.text


for i in range(1, 21):
    send(i)
    time.sleep(1)
