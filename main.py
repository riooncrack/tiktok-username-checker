from urllib import response
import requests
import time

Url = "https://discord.com/api/webhooks/944854069577662584/SZ2CWWD0zNMtdP_wzqsmOoV2FLyxRErnx2cJ0jecGeQqH2c-unPHPbBwTUPqZP3xn_ay"

wait_time = 5

def check(username):
    response = requests.head(f"https://www.tiktok.com/@{username}")
    if response.status_code == 200 and len(username) > 2:
        print(
            "%s[UNAVAILABLE] https://www.tiktok.com/@%s%s"
            % ('\u001b[31;1m', username, '/u001b[0m')
        )
    else:
        print(
            "%s[AVAILABLE] https://www.tiktok.com/@%s%s"
            % ('\u001b[31;1m', username, '/u001b[0m')
        )

        data = {"embeds": [{"author": {"name": "made by: swm"},"title": f"{username} claimable","description": "Some of these might not be claimable!","color": 15735892}]}
        response = requests.post(Url, json=data)

with open("usernames.txt", "r") as u:
    for user in u.readlines():
        check(user.strip())
        time.sleep(wait_time)