# -*- coding: utf-8 -*-
# @Time ： 2023/8/2 17:22
# @Auth ： JeremyChim
# @File ：read.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import openpyxl as op

def ret_cell_val(file,
                 sheet:int,
                 x:int,
                 y:int):
    '''
    :param file: 文件的路径
    :param sheet: 表格的sheet号
    :param x: 单元格行数
    :param y: 单元格列数
    :return: 单元格的值
    '''
    wb = op.load_workbook(file)
    sheet -= 1
    ws = wb.worksheets[sheet]

    a = ws.cell(x, y).value
    return a

if __name__ == '__main__':
    # from os import system
    # cmd = 'copy case.xlsx report.xlsx'
    # system(cmd)

    file = 'report.xlsx'
    x = 2
    y = 2
    a = ret_cell_val(file=file,
                     sheet=1,
                     x=x,
                     y=y)

    print(a.__class__, a)