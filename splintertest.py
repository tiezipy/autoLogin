from splinter.browser import Browser

browser = Browser('chrome')                  #模拟一个浏览器
browser.visit('https://glorysky.pspme.cn/manager')                          #访问指定URL
browser.fill('account','1016657151@qq.com')          #填充表单用户名
browser.fill('pwd','litie123')       #填充表单密码
browser.find_by_value('登录').click()    #表单提交