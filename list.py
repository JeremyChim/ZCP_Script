# -*- coding: utf-8 -*-
# @Time ： 2023/8/3 14:54
# @Auth ： JeremyChim
# @File ：list.py
# @IDE ：PyCharm
# @Github https://github.com/JeremyChim/

def ret_lst(data:str):
    '''
    :param data: 报文内容
    :return: 列表（元素是整形）
    '''
    a = data.replace("[","")
    a = a.replace("]", "")
    a = a.replace(" ","")

    a = a.split(',')
    a = map(int, a)
    a = list(a)

    return a

if __name__ == '__main__':
    a = "[ 1, 2, 3, 4]"
    a = ret_lst(a)
    print(a)