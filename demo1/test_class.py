import pytest
import allure
'''
体会scope范围的含义：autouse=True 自动激活功能
'''


@allure.feature("fixture autouse=True的功能显示")
@pytest.fixture(scope='class', autouse=True)
def open_broswer():
    print('这是打开浏览器')


def setup_module():
    print('\n整个模块.py开始')


def teardown_module():
    print('\n整个模块.py结束')


def setup_function():
    print('\n不在类中的函数前')


def teardown_function():
    print('\n不在类中的函数后')


@allure.title("pytest 的结构-function")
@allure.description("这是测试没在类中的方法加fixture及整体setup各层的调用")
def test_w_one():
    print('\n不在类中的方法1')


@allure.severity(allure.severity_level.NORMAL)
def test_w_two():
    print('\n不在类中的方法2')


@allure.title("pytest 的结构-class")
@allure.description("这是测试在类中的方法加fixture及整体setup_class/method的调用")
class TestClass:
    def setup_class(self):
        print('\n类前面')

    def teardown_class(self):
        print('\n类之后')

    def setup_method(self):
        print('\n方法前')

    def teardown_method(self):
        print('\n方法后')

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("断言了4与5的大小")
    def test_one(self):
        assert not 4 > 5
        print('\n方法1测试')

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("断言hello 与字符串是否相等")
    def test_two(self):
        x = "hello"
        assert "hello" == x
        print('\n方法2测试')

    @allure.description_html("""
<h1>这是一个调试的测试内容，查看一下人名和断言</h1>
<table style="width:100%">
  <tr>
    <th>名</th>
    <th>姓</th>
    <th>年龄</th>
  </tr>
  <tr align="center">
    <td>linda</td>
    <td>fang</td>
    <td>888</td>
  </tr>
  <tr align="center">
    <td>sevenruby</td>
    <td>huang</td>
    <td>999</td>
  </tr>
</table>
""")
    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b
        print('\n方法3测试')


if __name__ == '__main__':
    pytest.main(["-s", "test_class.py"])

