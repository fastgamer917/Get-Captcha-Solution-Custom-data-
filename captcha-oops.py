class captcha:
 def __init__(self,apikey,sitekey):
        self.API_KEY = apikey
        self.sitekey = sitekey




 def captcha(self,url):

    import requests
    from time import sleep

    # Add these values
    self.url = url  # example url

    self.s = requests.Session()

    # here we post site key to 2captcha to get captcha ID (and we parse it here too)
    self.captcha_id = self.s.post("http://2captcha.com/in.php?key={}&method=userrecaptcha&googlekey={}&pageurl={}".format(
        self.API_KEY, self.sitekey, self.url)).text.split('|')[1]
    # then we parse gresponse from 2captcha response
    print(f"captcha id is {self.captcha_id}")
    self.recaptcha_answer = self.s.get(
        "http://2captcha.com/res.php?key={}&action=get&id={}".format(self.API_KEY, self.captcha_id)).text
    print("solving ref captcha...")
    print(self.recaptcha_answer)
    while 'CAPCHA_NOT_READY' in self.recaptcha_answer:
        sleep(5)
        self.recaptcha_answer = self.s.get(
            "http://2captcha.com/res.php?key={}&action=get&id={}".format(self.API_KEY, self.captcha_id)).text
        print(self.recaptcha_answer)
    self.recaptcha_answer = self.recaptcha_answer.split('|')[1]
    return self.recaptcha_answer
