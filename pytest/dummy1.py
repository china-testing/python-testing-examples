#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论钉钉群21745728 商务合作钉钉或微信: pythontesting
# CreateDate: 2019-12-29
import unittest

class TestChatClient(unittest.TestCase):
    def test_nickname(self):
        client = ChatClient("User 1")

        assert client.nickname == "User 1"  

    def test_send_message(self):
        client = ChatClient("User 1")
        client.connection = _DummyConnection()
        sent_message = client.send_message("Hello World")
        print(sent_message)
        
        assert sent_message == "User 1: Hello World"


class _DummyConnection:
    def broadcast(*args, **kwargs):
        pass


class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        self.connection.broadcast(message)
        return sent_message

if __name__ == '__main__':
    unittest.main()
