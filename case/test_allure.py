import pytest
import allure




@pytest.fixture()
def login_fixture():
    print("先登录")

    yield

    print("用例运行完成")

@allure.step("步骤1")
def step_01():
    print("1")


@allure.step("步骤2")
def step_02():
    print("2")

@allure.step("步骤3")
def step_03():
    print("3")

@allure.step("步骤4")
def step_04():
    print("4")


@allure.feature("模块；功能点：编辑页面")
class TestAllure():

    @allure.story("用例1xxxx")
    @allure.title("用例标题")
    @allure.description("描述")
    def test_01(self,login_fixture):
        with allure.step("第一步"):
            step_01()
        with allure.step("第二步"):
            step_02()
        with allure.step("第三步"):
            step_03()

    @allure.story("用例2xxxx")
    def test_02(self):
        step_03()
        step_02()