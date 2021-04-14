#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : c1_urllib.py
@Time  : 2021/4/14 10:15
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

import unittest
import socket
from urllib import request, parse, error

import xlogs


logger = xlogs.get_logger()


class LearnUrllib(unittest.TestCase):
    url = 'http://httpbin.org'
    url_get = 'http://httpbin.org/get'
    url_post = 'http://httpbin.org/post'

    url_baidu = 'http://www.baidu.com'

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    # request
    def test_1(self):
        response = request.urlopen(self.url)
        logger.info(type(response))
        logger.info(response.read().decode('utf-8'))

    # error
    def test_2(self):
        data = bytes(parse.urlencode({'word': 'hellow'}), 'utf8')
        try:
            response = request.urlopen(self.url_post, data, timeout=10)
            logger.info(response.read().decode('utf8'))
        except error.HTTPError as e:
            logger.error(e.reason, e.code, e.headers, sep='\n')
        except error.URLError as e:
            if isinstance(e.reason, socket.timeout):
                logger.error(e.reason, "Time Out!!!")

    def test_3(self):
        # 状态码、响应头
        response = request.urlopen(self.url)
        logger.info(response.status)
        logger.info(response.getheaders())
        logger.info(response.getheader('Server'))

    def test_4(self):
        logger.info("Test Request ...")
        req = request.Request(self.url)
        response = request.urlopen(req)
        logger.info(response.read().decode('utf-8'))

    # pase, Request()
    def test_5(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'Host': 'httpbin.org'
        }
        dict_data = {
            'name': 'Germey'
        }
        data = bytes(parse.urlencode(dict_data), encoding='utf8')
        req = request.Request(url=self.url_post, data=data, headers=headers,
                              method='POST')
        req.add_header('accept', 'application / json')
        response = request.urlopen(req)
        print(response.read().decode('utf-8'))

    # Handler
    def skip_test_6(self):
        proxy_handler = request.ProxyHandler({
            'http': 'http://127.0.0.1:9743',
            'https': 'https://127.0.0.1:9743'
        })
        opener = request.build_opener(proxy_handler)
        response = opener.open(self.url_get)
        logger.info(response.read())

    # Cookie
    # HTTP CookieJar
    def test_7(self):
        import http.cookiejar
        cookie = http.cookiejar.CookieJar()
        hander = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(hander)
        response = opener.open(self.url_baidu)
        for item in cookie:
            logger.info(item.name + "=" + item.value)

    # HTTP MozillaCookieJar
    def test_8(self):
        import http.cookiejar
        cookie = http.cookiejar.MozillaCookieJar('cookie.txt')
        hander = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(hander)
        response = opener.open(self.url_baidu)
        for item in cookie:
            logger.info(item.name + "=" + item.value)
        cookie.save(ignore_discard=True, ignore_expires=True)

    # HTTP LWPCookieJar
    def test_9(self):
        import http.cookiejar
        cookie = http.cookiejar.LWPCookieJar('cookie.txt')
        hander = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(hander)
        response = opener.open(self.url_baidu)
        for item in cookie:
            logger.info(item.name + "=" + item.value)
        cookie.save(ignore_discard=True, ignore_expires=True)

        cookie = http.cookiejar.LWPCookieJar()
        cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
        handler = request.HTTPCookieProcessor(cookie)
        opener = request.build_opener(handler)
        response = opener.open(self.url_baidu)
        logger.info(response.read().decode('utf-8'))

    # urlparse
    def test_10(self):
        url = 'http://www.baidu.com/index.html;user?id=5#comment'
        result = parse.urlparse(url)
        logger.info(result)
        result = parse.urlparse(url, scheme='https')
        logger.info(result)
        result = parse.urlparse(url, scheme='https', allow_fragments=False)
        logger.info(result)
        result = parse.urlparse(url, scheme='https', allow_fragments=True)
        logger.info(result)

    # urlunparse
    def test_11(self):
        data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6',
                'comment']
        logger.info(parse.urlunparse(data))

    # urljoin
    def test_12(self):
        logger.info(parse.urljoin('http://www.baidu.com', 'FAQ.html'))
        logger.info(parse.urljoin('http://www.baidu.com',
                                  'https://cuiqingcai.com/FAQ.html'))
        logger.info(parse.urljoin('http://www.baidu.com/about.html',
                                  'https://cuiqingcai.com/FAQ.html'))
        logger.info(parse.urljoin('http://www.baidu.com/about.html',
                                  'https://cuiqingcai.com/FAQ.html?question=2')
                    )
        logger.info(parse.urljoin('http://www.baidu.com?wd=abc',
                                  'https://cuiqingcai.com/index.php'))
        logger.info(parse.urljoin('http://www.baidu.com',
                                  '?category=2#comment'))
        logger.info(parse.urljoin('www.baidu.com', '?category=2#comment'))
        logger.info(parse.urljoin('www.baidu.com#comment', '?category=2'))


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite(map(LearnUrllib, ['test_1']))
    # suite = unittest.TestLoader().loadTestsFromTestCase(LearnUrllib)
    unittest.TextTestRunner(verbosity=2).run(suite)
