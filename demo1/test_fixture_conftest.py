import pytest


# scope=function


def test_soso(login):
    print('case1: 登际后执行搜索')


def test_cakan():
    print('case2:不登陆就看')


@pytest.mark.skipif('2 + 2 != 5', reason='This test is skipped by a triggered condition in @pytest.mark.skipif')
def test_cart(login):
    print('case3,登陆，加购物车')

