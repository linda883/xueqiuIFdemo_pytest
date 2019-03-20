import pytest

'''
体会scope范围的含义：autouse=True 自动激活功能
'''
#
#
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


def test_w_one():
    print('\n不在类中的方法1')


def test_w_two():
    print('\n不在类中的方法2')


class TestClass:
    def setup_class(self):
        print('\n类前面')

    def teardown_class(self):
        print('\n类之后')

    def setup_method(self):
        print('\n方法前')

    def teardown_method(self):
        print('\n方法后')

    def test_one(self):
        assert not 4 > 5
        print('\n方法1测试')

    def test_two(self):
        x = "hello"
        assert "hello" == x
        print('\n方法2测试')

    def test_three(self):
        a = "hello"
        b = "hello world"
        assert a in b
        print('\n方法3测试')


if __name__ == '__main__':
    pytest.main(["-s", "test_class.py"])

