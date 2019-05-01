from selenium import webdriver
'''
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", 'HOST')
profile.set_preference("network.proxy.http_port", 31280)
profile.set_preference("network.proxy.ssl", 'HOST')
profile.set_preference("network.proxy.ssl_port", 31280)
driver = webdriver.Firefox(firefox_profile=profile)

driver.get("http://myip.ru/")
'''



from selenium import webdriver

PROXY = "52.68.114.44:80" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(options=chrome_options)
#chrome.get("http://whatismyipaddress.com")
chrome.get("http://myip.ru/")
