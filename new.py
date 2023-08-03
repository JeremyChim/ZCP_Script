# -*- coding: utf-8 -*-
# @Time ： 2023/8/3 16:58
# @Auth ： JeremyChim
# @File ：new.py
# @IDE ：PyCharm
# @Github https://github.com/JeremyChim/

from os import system

def copy_file(old, new):
    '''
    :param old: 旧文件的路径
    :param report: 新文件的路径
    :return: None
    '''
    order = f'copy {old} {new}'
    system(order)

if __name__ == '__main__':
    case = 'case.xlsx'
    report = 'report.xlsx'

    copy_file(case, report)