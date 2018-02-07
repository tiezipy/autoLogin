from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import time  
  
#模拟登陆163邮箱  
driver = webdriver.Chrome()  
driver.get("https://glorysky.pspme.cn/web/")  
 
elem_user = driver.find_element_by_id("form-username")  
elem_user.send_keys("100001000100006")  
elem_pwd = driver.find_element_by_id("form-password")  
elem_pwd.send_keys("abc123")  
driver.find_element_by_tag_name("form").submit()
# elem_pwd.send_keys(Keys.RETURN)  
# time.sleep(5)  
# #assert "baidu" in driver.title  
# driver.close()  
# driver.quit() 