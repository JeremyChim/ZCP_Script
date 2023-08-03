# -*- coding: utf-8 -*-
# @Time ： 2023/8/2 17:22
# @Auth ： JeremyChim
# @File ：read.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import openpyxl as op

def ret_cell_val(file,
            x:int,
            y:int):
    '''
    :param file: 读取的表格
    :param x: 单元格行数
    :param y: 单元格列数
    :return: 单元格的值
    '''
    wb = op.load_workbook(file)
    ws = wb.worksheets[0]
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
                     x=x,
                     y=y)

    print(a.__class__, a)