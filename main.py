import os, requests
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import date

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
from_phone = os.getenv('FROM_PHONE')
to_phone = os.getenv('TO_PHONE')
cookie = os.getenv('COOKIE')
client = Client(account_sid, auth_token)
todays_date = date.today().strftime("%d/%m/%Y")
# Get compass timetable
burp0_cookies = {"ASP.NET_SessionId": cookie}
burp0_url = "https://brunswick-vic.compass.education:443/services/mobile.svc/GetScheduleLinesForDate?sessionstate=readonly"
burp0_headers = {"Accept": "*/*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "iOS/14_6_0 type/iPhone CompassEducation/6.3.0", "Accept-Language": "en-au", "Connection": "close"}
burp0_json={"date": f"{todays_date} - 12:00 am", "sessionstate": "readonly", "userId": 23438}
classes = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json).json()['d']['data']

if not classes:
    print("No classes today!")
else:
    timetable = {}
    for classobj in classes:
        # Converting 12 hour time to 24 hour time using datetime
        time = classobj['topTitleLine'].split(" - ")[0]
        in_time = date.strptime(time, "%I:%M %p")
        out_time = date.strftime(in_time, "%H:%M")
        
        # Get class name
        class_name = classobj['topTitleLine'].split(" - ")[1]

        # Add to json
        timetable[class_name + "\n"] = out_time

    message = client.messages.create(
        body=' '.join(sorted(timetable, key=timetable.get)),
        from_=from_phone,
        to=to_phone
    )

    print(message.sid)