from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
import time  
   
driver = webdriver.Chrome()  
driver.get("https://psdemo.pspme.cn/Manager/")  
 
elem_user = driver.find_element_by_id("form-username")  
elem_user.send_keys("1016657151@qq.com")  
elem_pwd = driver.find_element_by_id("form-password")  
elem_pwd.send_keys("litie123")  
driver.find_element_by_tag_name("form").submit()
