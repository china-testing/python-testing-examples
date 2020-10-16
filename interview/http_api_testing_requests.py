#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/china-testing/python-testing-examples 
# interview/http_api_testing_requests.py
# 项目实战讨论Q群144081101 6089740
# CreateDate: 2020-10-15

import requests

response = requests.post('https://httpbin.org/post', json={'key': 'value'})
print(response.json()['origin'])