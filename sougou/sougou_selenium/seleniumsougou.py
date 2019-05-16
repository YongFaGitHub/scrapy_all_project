from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.ximalaya.com/passport/login?fromUri=http://www.ximalaya.com/my/')#http://www.ximalaya.com/passport/login?fromUri=/my/
# driver.current_window_handle
time.sleep(3)
driver.find_element_by_id("userAccount").send_keys("13022434516")
driver.find_element_by_id("userPwd").send_keys("qazwsxedc123")

driver.find_element_by_id("login_btn").click()
time.sleep(3)
print(111)
# driver.current_window_handle()
# time.sleep(5)
# driver.find_element_by_class("e-1593453034 first-step").click()

#清除alart
time.sleep(3)
print(222)

driver.find_element_by_xpath('//ul[@class="e-1049550884 album-list-wrap"]/li[3]//div[@class="e-1049550884 text"]').click()
print(222)
# time.sleep(3)
# driver.find_element_by_class_name("e-2304105070 text").click()

time.sleep(5)
# print(333)

# driver.find_element_by_xpath("//ul[@class='e-2304105070']/li[1]//i[@class='e-2304105070 text']").click()






# driver.find_elements_by_xpath("//a[@title='《阴间神探》紫襟故事']/@href").click()

# time.sleep(2)
#
# li_list = driver.find_elements_by_xpath("//ul[@class='e-1049550884 album-list-wrap']/li[3]/div[2]/div[1]")
# for li in li_list:
#     li.find_element_by_xpath("./div[1]").click()
#     time.sleep(5)


# driver.find_element_by_class("e-3793817119 page-link").click()
# time.sleep(2)

#
# (driver.current_url)
# get_log






# import time
# import re
# import requests
#
# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
# browser.get("https://baike.sogou.com/")
# list  = ["肾炎","糖尿病"]
# for i in list:
#
#     browser.find_element_by_id("searchText").send_keys(i)
#     browser.find_element_by_id("enterLemma").click()
#     time.sleep(3)
#
#     text1 = browser.page_source
#     bbb = re.findall("lemmaData.lemmaId=(.*?);",text1)
#
#     url = "http://baike.sogou.com/v" + str(bbb[0]) + ".htm?fromTitle={}" .format(i)
#     print(url) #将网址存储
#
#     browser.find_element_by_id("searchText").clear()   #清楚输入框中的内容
#
#
# browser.close()
# response = requests.get(url)
# disease = response.xpath("//div[@class='abstract']/p//text()").extract()
# print(disease)

# print(text1)
# print(browser.page_source)
# browser.close()