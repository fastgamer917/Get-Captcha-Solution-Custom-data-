from captcha import *
apikey = open("/home/#checkthis/2captchakey.txt","r").read()
apikey = apikey.rstrip()
sitekey = "6LfW6wATAAAAAHLqO2pb8bDBahxlMxNdo9g947u9"
url = "https://recaptcha-demo.appspot.com/recaptcha-v2-checkbox.php"

cap = captcha(apikey,sitekey)
result = cap.captcha(url)
print(result)
