import pytest
from pages.login_page import LoginPage
from selenium import webdriver
from pages.projectinfo_page import ProjectInfo
import allure
import os
from common.read_yml import readyml

cur_path = os.path.dirname(os.path.realpath(__file__))
yaml_path = os.path.join(cur_path,"data_demo.yml")
a = readyml(yaml_path)
test_data = a["test_add_project"]

"""
test_data = [
    ["test1",True],
    ["test2",True],
    ["test3",True]
]
"""

@pytest.fixture(scope="function")
def delete_some_data():
    print("清理数据")


@allure.title("{title}")
@allure.severity("blocker")
@pytest.mark.parametrize("projectname,expected,title",test_data)
@allure.story("添加项目成功")
def test_add_project_01(login_fixture,delete_some_data,projectname,expected,title):
    driver = login_fixture
    project = ProjectInfo(driver)
    with allure.step("点击列表"):
        project.click_projectlist()
    with allure.step("点击添加"):
        project.click_addproject()
    with allure.step("输入内容"):
        project.input_projectname(projectname)
        project.input_respname()
        project.input_tester()
        project.input_dever()
        project.input_app()
        project.input_simpledesc()
        project.input_simpledesc()
    with allure.step("点击保存"):
        project.click_send()
    with allure.step("获取页面结果"):
        result = project.is_add_success()
        print(result)
    with allure.step("判断是否成功"):
        pytest.assume: result == expected


@allure.story("重复添加失败")
@allure.title("重复添加失败")
def test_add_project_02(login_fixture,delete_some_data):
    """重复添加失败"""
    """先添加成功"""
    driver = login_fixture
    project = ProjectInfo(driver)

    """再次添加，添加失败"""
    project.click_addproject()
    project.input_projectname()
    project.input_respname()
    project.input_tester()
    project.input_dever()
    project.input_app()
    project.input_simpledesc()
    project.input_simpledesc()
    project.click_send()
    result = project.is_add_success()
    assert not result


if __name__ == '__main__':
    cur_path = os.path.dirname(os.path.realpath(__file__))
    yaml_path = os.path.join(cur_path, "data_demo.yml")
    a = readyml(yaml_path)
    test_data = a["test_add_project"]
    print(test_data)