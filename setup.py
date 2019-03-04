#-*- coding:utf-8 -*-
from setuptools import setup, find_packages
setup(
    name = "weixinioen",
    version = "0.1.0",
    keywords = ("pip", "weixinioen"),
    description = "微信第三方平台接口",
    long_description = "微信第三方平台接口",
    license = "Wx cence",

    url = "https://github.com/livelu/weixinopen",
    author = "zhanglu",
    author_email = "zhanglu90@126.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "weixin",
    install_requires = ['pycurl']
)
