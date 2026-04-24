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
    # 7位数字 + "-" + 12位数字 + @qq.com
    part1 = ''.join(random.choices(string.digits, k=7))
    part2 = ''.join(random.choices(string.digits, k=12))
    return f"{part1}-{part2}@qq.com"

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
