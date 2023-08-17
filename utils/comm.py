import os

from save_report_history.save_report_history import Get_History


def get_report():
    # 1 、 生成json文件
    print("正在生成JSON文件".center(76, '-'))
    cmd = r"pytest E:\UIautotesting\testcases\test_canva_homepage.py " \
          r" --alluredir=E:\catalogserviceUIautotesting\Results --clean-alluredir"
    os.system(cmd)

    print("正在复制配置信息文件".center(76, '-'))
    # 2、 复制配置文件到json文件中
    cmd1 = r'copy E:\catalogserviceUIautotesting\allure-environment\environment.properties' \
           r' E:\catalogserviceUIautotesting\allure-environment\environment.properties '
    os.system(cmd1)

    print("正在生成报告".center(76, '-'))
    # 3、生成报告
    cmd2 = r"allure generate E:\catalogserviceUIautotesting\Results -o " \
           r"E:\catalogserviceUIautotesting\Report --clean "
    os.system(cmd2)
    print("报告生成完毕！！！！".center(76, '-'))

    # 4、 替换历史记录文件
    print("正在生成历史趋势文件".center(76, '-'))
    Get_History().get_history()

    # 5、为报告开启端口，共享查看
    print('正在开启端口，分享报告')
    cmd3 = r'allure open -h 192.168.31.232 -p 8885 E:\catalogserviceUIautotesting\Report'
    os.system(cmd3)

get_report()
