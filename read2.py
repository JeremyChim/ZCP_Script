# -*- coding: utf-8 -*-
# @Time ： 2023/8/2 17:22
# @Auth ： JeremyChim
# @File ：read2.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import openpyxl as op

def ret_val(x:int, y:int):
    '''
    :param x: 单元格行数
    :param y: 单元格列数
    :return: 单元格的值
    '''
    wb = op.load_workbook('report2.xlsx')
    ws = wb.worksheets[0]
    a = ws.cell(x, y).value
    return a

if __name__ == '__main__':
    from os import system
    cmd = 'copy case2.xlsx report2.xlsx'
    system(cmd)

    a = ret_val(2, 2)
    print(a.__class__, a)