# -*- coding: utf-8 -*-
# @Time ： 2023/8/2 14:33
# @Auth ： JeremyChim
# @File ：sgn.py
# @IDE ：PyCharm
# @Github ：https://github.com/JeremyChim/

# a = {"can_id": 0x10A,"is_canfd": 0,"canfd_brs": 0,"data": [0, 1, 2, 3, 4],"interval_ms": 500}

def ret_sgn(can_id,
            is_canfd : int,
            canfd_brs : int,
            data : list,
            interval_ms : int):
    '''
    :param can_id: 帧ID
    :param is_canfd: 是否为CANFD数据, 0-CAN, 1-CANFD
    :param canfd_brs: CANFD加速, 0-不加速, 1-加速
    :param data: 数据
    :param interval_ms: 本帧数据定时发送间隔, 毫秒
    :return: 只有一个信号的列表
    '''

    a = {"can_id": can_id,
         "is_canfd": is_canfd,
         "canfd_brs": canfd_brs,
         "data": data,
         "interval_ms": interval_ms}
    a = [a]
    return a

if __name__ == '__main__':

    a = ret_sgn(can_id = 0x10A,
                is_canfd = 0,
                canfd_brs = 0,
                data = [0, 1, 2, 3, 4],
                interval_ms = 500)

    print(a)