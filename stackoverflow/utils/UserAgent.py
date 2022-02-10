"""
-------------------------------------------------
   开发人员：janeho
   开发日期：2021-11-16
   开发工具：PyCharm
   功能描述：生成随机请求头
-------------------------------------------------
"""
import json
import os
import random


class UserAgent(object):
    """
    获取随机请求头
    """

    def __init__(self):
        """请求头初始化.

        初始化请求头信息.

        """
        self.current_path = os.path.dirname(__file__)
        self.json_file = self.current_path + '/fake_user_agent.json'
        self.ua_data = self.user_agent_data().get("browsers")
        self.b = ['chrome', 'opera', 'firefox', 'safari', 'internetexplorer']
        self.chrome = lambda: random.choice(self.ua_data.get("chrome"))
        self.opera = lambda: random.choice(self.ua_data.get("opera"))
        self.firefox = lambda: random.choice(self.ua_data.get("firefox"))
        self.safari = lambda: random.choice(self.ua_data.get("safari"))
        self.ie = lambda: random.choice(self.ua_data.get("internetexplorer"))
        self.random = lambda: random.choice(self.ua_data.get(random.choice(self.b)))

    def user_agent_data(self):
        """ 读取文件

        读取文件以用于生成随机请求头

        Returns:
            data: json格式的数据
        """
        with open(self.json_file, "r") as fp:
            data = fp.read()
        return json.loads(data)

    def get_header(self):
        """ 获取随机请求头

        通过random函数获取随机请求头

        Returns:
            data: dict格式的请求头，仅包含User-Agent
        """
        return {'User-Agent': self.random()}
