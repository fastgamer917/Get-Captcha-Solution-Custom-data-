from captcha import *
apikey = input("enter api key")
sitekey = input("enter site g-key")
url = input("enter url")

result = captcha(apikey,sitekey,url)
print(result)
