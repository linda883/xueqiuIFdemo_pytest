import pytest
'''
这个例子体会yield的用法
'''


@pytest.fixture(scope='module')
def login_y():
    print('\n这是个登陆模块！')
    yield
    print('测试结束时打印！')


def test_soso(login_y):
    print('case1: 登际后执行搜索')


def test_cakan():
    print('case2:不登陆就看')


def test_cart(login_y):
    print('case3,登陆，加购物车')

