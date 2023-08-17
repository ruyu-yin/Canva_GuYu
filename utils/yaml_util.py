import os
import yaml

class YamlUtil:

    #读取djaccount.yml文件
    def read_djaccount_yaml(self,key):
        with open(os.getcwd()+"/dj_account.yml",mode='r',encoding='utf-8') as f:
            value = yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key]

        #  存中多行，读取多行
        #     for data in value:
        #         print(type(data))
        #     print(data)

    #写入djaccount.yaml文件
    def write_djaccount_yaml(self,data):
        # 此处注意：w为替换，始终是最开始的一个变量，a为追加yaml文件每次都增加多个变量a
        # 可结合使用fixture、conftest进行清除
        with open(os.getcwd()+"/dj_account.yml",mode='a',encoding='utf-8') as f:
            yaml.dump(data=data,stream=f,allow_unicode=True)

    #清除djaccount.yaml文件
    def clear_djaccount_yaml(self):
        with open(os.getcwd()+"/dj_account.yml",mode='w',encoding='utf-8') as f:
            f.truncate()