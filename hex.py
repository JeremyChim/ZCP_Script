# -*- coding: utf-8 -*-
# @Time ： 2023/8/2 17:44
# @Auth ： JeremyChim
# @File ：hex.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

def ret_hex(str:str):
    '''
    :param str: 输入字符串
    :return: 整形
    '''
    a = str
    a = int(a, 16)
    return a

if __name__ == '__main__':
    a = ret_hex("0xFF")
    print(a.__class__, a)