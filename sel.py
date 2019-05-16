# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')


from datetime import datetime
a = datetime.now().isocalendar()[1]
print(a)