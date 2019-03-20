import pytest


@pytest.fixture()
def login():
    print('这是个登陆模块！')


def test_soso(login):
    print('case1: 登际后执行搜索')


def test_cakan():
    print('case2:不登陆就看')


def test_cart(login):
    print('case3,登陆，加购物车')

