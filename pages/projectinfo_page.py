from common.base import Base


class ProjectInfo(Base):
    #项目列表<a href="/api/project_list/1/">项 目 列 表</a>
    loc1 = ("xpath","//*[@href='/api/project_list/1/']")
    #+新增项目按钮，/html/body/div[2]/div[6]/div[1]/dl[2]/button[1]
    loc2 = ("xpath", "/html/body/div[2]/div[6]/div[1]/dl[2]/button[1]")
    #左边栏，新增项目<a href="/api/add_project/">新 增 项 目</a>
    loc3 = ("xpath", "//*[@href='/api/add_project']")
    #新增项目-项目名称//*[@id="project_name"]
    loc4 = ("xpath", "//*[@id='project_name']")
    #新增项目-项目负责人
    loc5 = ("xpath", "//*[@id='responsible_name']")
    #新增项目-测试人员
    loc6 = ("xpath", "//*[@id='test_user']")
    # 新增项目-开发人员
    loc7 = ("xpath", "//*[@id='dev_user']")
    # 新增项目-发布应用
    loc8 = ("xpath", "//*[@id='publish_app']")
    # 新增项目-简要描述
    loc9 = ("xpath", "//*[@id='simple_desc']")
    # 新增项目-其他信息
    loc10 = ("xpath", "//*[@id='other_desc']")
    #新增项目-点击提交
    loc11 = ("xpath","//*[@id='send']")
    #判断成功//*[@id="pro_filter"]/ul/li[3]/button
    loc12 = ("xpath","//*[@id='project_list']/table/tbody/tr[1]/td[3]/a")

    def click_projectlist(self):
        """点击项目列表"""
        self.click(self.loc1)


    def click_addproject(self):
        """点击+新增项目按钮"""
        self.click(self.loc2)

    def click_addprojectleft(self):
        """左侧新增项目"""
        self.click(self.loc3)

    def input_projectname(self,text='test1'):
        """输入项目名称"""
        self.send(self.loc4,text)


    def input_respname(self,text='test1'):
        """输入负责人"""
        self.send(self.loc5,text)

    def input_tester(self,text='tester1'):
        """输入测试人员"""
        self.send(self.loc6,text)

    def input_dever(self,text='dever1'):
        """输入开发人员"""
        self.send(self.loc7,text)


    def input_app(self,text='app1'):
        """输入发布应用"""
        self.send(self.loc8,text)

    def input_simpledesc(self,text='fortest'):
        """输入简要描述"""
        self.send(self.loc9,text)

    def input_otherdesc(self,text='none'):
        """输入其他信息"""
        self.send(self.loc10,text)

    def click_send(self):
        """点击提交"""
        self.click(self.loc11)


    def is_add_success(self,expect="test"):
        """查看是否提交成功"""
        text = self.get_text(self.loc12)
        return expect in text

if __name__ == '__main__':
    from pages.login_page import LoginPage
    from selenium import webdriver
    from time import sleep
    driver = webdriver.Chrome()

    web = LoginPage(driver)
    web.login()

    project = ProjectInfo(driver)
    project.click_projectlist()
    project.click_addproject()
    project.input_projectname()
    project.input_respname()
    project.input_tester()
    project.input_dever()
    project.input_app()
    project.input_simpledesc()
    project.input_simpledesc()
    project.click_send()
    sleep(8)

    driver.close()