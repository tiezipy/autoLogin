from splinter import Browser 
from settings import *
import time

def main():
	for i in settings:
		openNewWind(settings[i]['url'],settings[i]['account'],settings[i]['password'])	
		time.sleep(3)

def openNewWind(URL,account,password):
	browser = Browser('firefox')
	if URL == 'http://www.pspme.cn/':
	    browser.visit(URL)
	    return
	else:
	    browser.visit(URL)                     
	    browser.find_by_id('form-username').fill(account)
	    browser.find_by_id('form-password').fill(password)
	    browser.find_by_value('登录').click()


if __name__=="__main__":
	main()