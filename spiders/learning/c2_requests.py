#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : c2_requests.py
@Time  : 2021/4/14 10:25
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

import unittest
import requests
import json
import sys
from spiders.learning import logger


class LearnUrllib(unittest.TestCase):
    url = 'http://httpbin.org'
    url_get = 'http://httpbin.org/get'
    url_post = 'http://httpbin.org/post'

    url_baidu = 'http://www.baidu.com'

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_01(self):
        response = requests.get(self.url_baidu)
        logger.info(type(response))
        logger.info(response.status_code)
        logger.info(type(response.text))
        logger.info(response.text)
        logger.info(response.cookies)

    def test_02(self):
        requests.post(self.url_post)
        requests.put('http://httpbin.org/put')
        requests.delete('http://httpbin.org/delete')
        requests.head('http://httpbin.org/get')
        requests.options('http://httpbin.org/get')

    def test_03(self):
        response = requests.get("http://httpbin.org/get?name=germey&age=22")
        logger.info(response.text)

        data = {
            'name': 'germey',
            'age': 22
        }
        response = requests.get(self.url_get, params=data, timeout=10)
        logger.info(response.text)

        logger.info(response.json())
        logger.info(type(response.json()))
        logger.info(json.loads(response.text))

    # 获取二进制数据
    def test_04(self):
        response = requests.get("https://github.com/favicon.ico")
        with open('favicon.ico', 'wb') as f:
            f.write(response.content)
            f.close()

    def test_05(self):
        data = {'name': 'germey', 'age': '22'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        response = requests.post(self.url_post, data=data, headers=headers)
        logger.info(response.json())

    # reponse属性
    def test_06(self):
        response = requests.get('http://www.jianshu.com')
        logger.info(type(response.status_code), response.status_code)
        logger.info(type(response.headers), response.headers)
        logger.info(type(response.cookies), response.cookies)
        logger.info(type(response.url), response.url)
        logger.info(type(response.history), response.history)

    def test_07_1(self):
        response = requests.get('http://www.jianshu.com/hello.html')
        sys.exit() if not response.status_code == requests.codes.not_found \
            else print('404 Not Found')

    def test_07_2(self):
        response = requests.get('http://www.jianshu.com')
        sys.exit() if not response.status_code == 200 \
            else print('Request Successfully')

    # 文件上传
    def test_08(self):
        files = {'file': open('favicon.ico', 'rb')}
        response = requests.post("http://httpbin.org/post", files=files)
        print(response.text)

    # 获取cookie
    def test_09(self):
        response = requests.get("https://www.baidu.com")
        print(response.cookies)
        for key, value in response.cookies.items():
            print(key + '=' + value)

    # 会话维持
    def test_10(self):
        s = requests.Session()
        s.get('http://httpbin.org/cookies/set/number/123456789')
        response = s.get('http://httpbin.org/cookies')
        print(response.text)

    # 证书验证
    def test_11(self):
        from requests.packages import urllib3
        urllib3.disable_warnings()
        response = requests.get('https://www.12306.cn', verify=False)
        print(response.status_code)

        response = requests.get('https://www.12306.cn',
                                cert=('/path/server.crt', '/path/key'))
        print(response.status_code)

    # 代理设置
    def test_12(self):
        proxies = {
            "http": "http://127.0.0.1:9743",
            "https": "https://127.0.0.1:9743",
        }

        response = requests.get("https://www.taobao.com", proxies=proxies)
        print(response.status_code)

        proxies = {
            "http": "http://user:password@127.0.0.1:9743/",
        }
        response = requests.get("https://www.taobao.com", proxies=proxies)
        print(response.status_code)

        # pip3 install 'requests[socks]'
        proxies = {
            'http': 'socks5://127.0.0.1:9742',
            'https': 'socks5://127.0.0.1:9742'
        }
        response = requests.get("https://www.taobao.com", proxies=proxies)
        print(response.status_code)

    # 认证设置
    def test_13(self):
        from requests.auth import HTTPBasicAuth

        r = requests.get('http://120.27.34.24:9001',
                         auth=HTTPBasicAuth('user', '123'))
        print(r.status_code)

        r = requests.get('http://120.27.34.24:9001', auth=('user', '123'))
        print(r.status_code)

    # 异常处理
    def test_14(self):
        from requests.exceptions import ReadTimeout, ConnectionError, \
            RequestException
        try:
            response = requests.get("http://httpbin.org/get", timeout=0.5)
            print(response.status_code)
        except ReadTimeout:
            print('Timeout')
        except ConnectionError:
            print('Connection error')
        except RequestException:
            print('Error')


if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite(map(LearnUrllib, ['test_01']))
    suite = unittest.TestLoader().loadTestsFromTestCase(LearnUrllib)
    unittest.TextTestRunner(verbosity=2).run(suite)
