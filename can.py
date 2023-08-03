# -*- coding: utf-8 -*-
# @Time ： 2023/8/1 16:48
# @Auth ： JeremyChim
# @File ：can.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

import zcanpro as z
from time import sleep

from new import copy_file
from row_col import ret_row_col
from sgn import ret_sgn
from read import ret_cell_val
from hex import ret_hex
from list import ret_lst

stopTask = False

def z_main():

    case = r'D:\GithubProject\ZCP_Script\case.xlsx'
    report = r'D:\GithubProject\ZCP_Script\report.xlsx'
    copy_file(old=case, new=report) # 根据用例，生成新的报告

    z.write_log(f'正在初始化，读取用例中...')
    sleep(3)
    z.write_log(f'报告生成路径：{report}')

    busID = init() # 初始化，获取总线ID

    row, col = ret_row_col(report, 1)
    row -= 1
    z.write_log(f'用例总数：{row}')

    for i in range(row):
        i += 2
        a = ret_cell_val(report, i, 2)

        z.write_log(f"发送信号中：{a}")

        can_id = ret_hex(a)
        is_canfd = ret_cell_val(report, i, 3)
        canfd_brs = ret_cell_val(report, i, 4)
        interval_ms = ret_cell_val(report, i, 6)

        data = ret_cell_val(report, i, 5)
        data = ret_lst(data)

        sgn = ret_sgn(can_id=can_id,
                      is_canfd=is_canfd,
                      canfd_brs=canfd_brs,
                      data=data,
                      interval_ms=interval_ms)

        send(busID, sgn)

def init():
    bus = z.get_buses()
    busID = bus[0]["busID"]
    devType = bus[0]["devType"]
    devIndex = bus[0]["devIndex"]
    chnIndex = bus[0]["chnIndex"]
    z.write_log("="*10 + "总线信息" + "="*10)
    z.write_log(f"总线ID: {str(busID)}")
    z.write_log(f"设备类型: {str(devType)}")
    z.write_log(f"设备索引号: {str(devIndex)}")
    z.write_log(f"通道索引号: {str(chnIndex)}")
    z.write_log("="*30)
    return busID

def send(busID, sgn):
    res = z.dev_auto_send_start(busID, sgn)
    if res == 1:
        z.write_log(f"成功：{sgn}")
    else:
        z.write_log(f"失败：{sgn}")
    return res

def z_notify(type, obj):
    z.write_log("Notify " + str(type) + " " + str(obj))
    if type == "stop":
        z.write_log("Stop...")
        global stopTask
        stopTask = True