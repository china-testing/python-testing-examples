#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/china-testing/python-testing-examples 
# interview/http_api_testing_requests2.py
# 项目实战讨论Q群144081101 6089740
# CreateDate: 2020-10-15
import requests

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
response = requests.post('https://httpbin.org/post',data={'key': 'value'},
    headers=headers)

print(response.json()['origin'])