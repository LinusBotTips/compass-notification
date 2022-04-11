# Compass Timetable SMS Notification

## Getting Started

We assume that before you begin, you will have [Python](http://www.python.org/) and [pip](http://www.pip-installer.org/en/latest/) installed on your system and available at the command line.

Before you can run this project, you will need to set some environment variables in the [example.env](https://github.com/LinusBotTips/compass-notification/blob/main/example.env) file.  These are:

* `TWILIO_ACCOUNT_SID` : Your Twilio "account SID" - it's like your username for the Twilio API.  This and the auth token (below) can be found [on your account dashboard](https://www.twilio.com/user/account).
* `TWILIO_AUTH_TOKEN` : Your Twilio "auth token" - it's your password for the Twilio API.  This and the account SID (above) can be found [on your account dashboard](https://www.twilio.com/user/account).
* `FROM_PHONE` : A Twilio number that you own, that can be used for making calls and sending messages.  You can find a list of phone numbers you control (and buy another one, if necessary) [in the account portal](https://www.twilio.com/user/account/phone-numbers/incoming).
* `TO_PHONE` : Your phone number with the country code extension (_+61456789123_, for example). If you have the Twilio free trial, you will need to [verify the caller ID](https://console.twilio.com/us1/develop/phone-numbers/manage/verified?frameUrl=%2Fconsole%2Fphone-numbers%2Fverified%3Fx-target-region%3Dus1).
* `SUBDOMAIN` : Your Compass subdomain (The piece of text before _.compass.education_ in the URL.)


To find the rest of the values, run the following commands: 

```
pip install -r requirements.txt  
python3 auth.py
```
You will be prompted to login to your Compass account with your username & password. It will then show you your `COOKIE` value and `USER_ID` value.

Now, rename `example.env` to `.env`.

## Running the Script
Once you have finished setting up the `.env` file, you can start the script.
Simply run `python3 main.py` to start the script. It will text you your Compass timetable for the current day. If there are no classes today, it will not send you a text message. However, if there are classes, it will send you a text message and log the SMS's ID in the terminal.

## Scheduling the Script
Theres a couple ways you can make it send every 24 hours. You can either use a [Cronjob](https://ostechnix.com/a-beginners-guide-to-cron-jobs/) or yoink an idea from [StackOverFlow](https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day).

### Contributors
<a href="https://github.com/LinusBotTips/compass-notification/graphs/contributors">
	<img src="https://contrib.rocks/image?repo=LinusBotTips/compass-notification" />
</a> 
