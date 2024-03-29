# -*- coding: UTF-8 -*-
"""
保存每次的测试历史记录
用于生成趋势图

设计思路： 首先进行判断当前文件夹内是否存在历史测试记录文件
如果存在--- 说明不是第一次进行测试，那么要做的操作为  1、 读取历史测试数据 使用一个变量进行保存，
                                            2、读取最新的测试报告数据，使用另一个变量保存，
                                            3、使用for循环 获取每次数据，将每次获取的数据加入到旧的历史记录中，
                                             4、将加入新数据后的旧数据覆盖写入到历史文件中，
                                             5、复制文件到报告文件中

如果不存在 --- 说明为第一次执行测试， 具体操作步骤为： 复制测试报告文件到历史文件中 作为首次记录
"""



import os
import json


class Get_History:
    def get_history(self):
        # 先判断是否为第一次生成（如果该目录下没有history-trend.json文件则为第一次）
        if os.path.exists(
                r"C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\save_report_history\history-trend.json"):
            print('文件存在')
            #如果存在文件，则读取现有文件，将新生成的文件加入到现有文件中，再将处理后的文件复制到报告目录下
            #打开json文件获取数据
            f = open(r"C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\save_report_history\history-trend.json")
            old_history_list = json.load(f)
            # print(f'旧的json文件为{old_history_list}')

            #获取新生成的history文件数据
            f1 = open(r"C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\report\history\history-trend.json")
            new_history_list = json.load(f1)
            # print(f'新的json文件为{new_history_list}')

            #遍历新的history文件，文件处理，依次加入到旧的文件中
            for i in new_history_list:
                # print(i)
                old_history_list.append(i)
            # 覆盖写入数据至保存历史数据文件中
            with open(r"C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\save_report_history\history-trend.json","w") as f:
                    json.dump(old_history_list, f)


            s = open(r'C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\save_report_history\history-trend.json')
            total_history_data = json.load(s)[::-1]     #获取倒序的历史总文件
            filename = r'C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\save_report_history\history-trend_desc.json'        #指定文件名创建倒序文件
            with open(filename,'w') as f :
                json.dump(total_history_data,f)


            #将写入后的倒叙文件复制到报告文件中
            cmd = rf'copy {filename} C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\report\widgets\history-trend.json'
            os.system(cmd)

        else:
            print("第一次执行测试？")
            if os.path.exists(r'C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\report\widgets\history-trend.json'):
                print('获取最新数据为第一版,从报告目录复制文件到历史文件保存目录')
                cmd = r'copy C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\report\widgets\history-trend.json C:\Users\admin\PycharmProjects\pythonProject\Okmarts_test_front\save_report_history\history-trend.json'
                os.system(cmd)
            else :
                print('未找到相关测试记录文件，请先执行测试')


if __name__ == '__main__':
    a = Get_History()
    a.get_history()
