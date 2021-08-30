from common.base import Base


url = "http://122.51.56.87:8888/api/login/"
class LoginPage(Base):
    #用户名//*[@id="account"]
    loc1 = ("xpath","//*[@id='account']")
    #密码
    loc2 = ("xpath", "//*[@id='password']")
    #登录
    loc3 = ("xpath", "//*[@id='login_submit']")
    #判断元素
    loc4 = ("xpath","/html/body/div[2]/div[1]/div[1]/a")

    def input_username(self,text="liuyang"):
        """输入用户名"""
        self.send(self.loc1,text)

    def input_password(self,text="123456"):
        """输入密码"""
        self.send(self.loc2,text)

    def click_login(self):
        """点击登录按钮"""
        self.click(self.loc3)


    def login(self,user="liuyang",password="123456"):
        self.driver.get(url)
        self.input_username(user)
        self.input_password(password)
        self.click_login()

    def is_login_sucess(self):
        """判断登录是否成功"""
        return self.is_element_exist(self.loc4)



if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    web.login()
    time.sleep(9)
    result = web.is_login_sucess()
    print("登录结果：", result)
    assert result

    driver.close()