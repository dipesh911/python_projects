import requests
import json
from datetime import date

#API url to fetch data
url = "https://json.freeastrologyapi.com/complete-panchang"
url_tithi = "https://json.apiastro.com/tithi-durations"
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
#chat_id = "XXXXXXXXX"
chat_id = "XXXXXXXXXX"

#date extract
today_full_date = date.today()
year = today_full_date.year
month = today_full_date.month
today_date = today_full_date.day

#json payload
payload = json.dumps({
  "year": year,
  "month": month,
  "date": today_date,
  "hours": 6,
  "minutes": 0,
  "seconds": 0,
  "latitude": 17.38333,
  "longitude": 78.4666,
  "timezone": 5.5,
  "config": {
    "observation_point": "topocentric",
    "ayanamsha": "lahiri"
  }
})
headers = {
  'Content-Type': 'application/json',
  'x-api-key': '4qv8omuU8f4x69etiS2Z9YPw09szmDc9fMx1OwN8'
}

response = requests.request("POST", url_tithi, headers=headers, data=payload).text


response_from_api = json.loads(response)['output']
response_json = json.loads(response_from_api)
name = response_json['name']
paksha = response_json['paksha']
message = (f"Today is {paksha} paksha {name}")

#send message to telegram bot
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
(requests.get(url).json()) # this sends the message