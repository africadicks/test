import requests
import random
import time

url = "https://www.luobenyun.homes/api/v1/passport/comm/sendEmailVerify"

headers = {
    "User-Agent": "8848 Titanium Mobile Phone",
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://www.luobenyun.homes",
    "Referer": "https://www.luobenyun.homes/"
}

# ✔ 原函数：7~12位范围随机数
def gen_email():
    min_val = 10**6
    max_val = 10**12 - 1
    num = random.randint(min_val, max_val)
    return f"{num}@qq.com"

# ✔ 新增函数：固定10位随机数字
def gen_email_10():
    min_val = 10**9          # 1000000000（10位最小）
    max_val = 10**10 - 1     # 9999999999（10位最大）
    num = random.randint(min_val, max_val)
    return f"{num}@qq.com"

# ✔ 当前使用的生成函数（切换这里）
USE_FUNC = gen_email_10   # ← 改这里切换 gen_email / gen_email_10

def send(i):
    email = USE_FUNC()

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
