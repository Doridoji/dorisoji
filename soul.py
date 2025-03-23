import requests
url = "https://telegram.org/support"

data = {
    "problem": "This channel https://t.me/ is running illegal activities.\n"
    "It takes money from people to teach DDoS attacks on BGMI, hacking courses,\n"
    "and attacks on Indian government sites. It also performs DDoS attacks on Telegram VCs.\n"
    "Now, the channel owner has cleared history, so please review its past week's logs.",
    "full_name": "SoulCrack Rana",
    "email": "@gmail.com",
    "phone_number": "+91",
}
response = requests.post(url, data=data)


if response.status_code == 200:
    print("Report submitted successfully!")
else:
    print(f"Failed to submit report. Status code: {response.status_code}")
# file owner @SOULCRACK