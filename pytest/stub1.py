#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 技术支持：dwz.cn/qkEfX1u0 项目实战讨论钉钉群21745728 商务合作钉钉或微信: pythontesting
# CreateDate: 2019-12-29
import unittest
import unittest.mock


class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))

        with unittest.mock.patch.object(c, "get_messages", return_value=[]):
            c.broadcast("some message")

            assert c.get_messages()[-1] == "some message"



class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        self.connection.broadcast(message)
        return sent_message


from multiprocessing.managers import SyncManager
class Connection(SyncManager):
    def __init__(self, address):
        self.register("get_messages")
        super().__init__(address=address)
        self.connect()

    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)


if __name__ == '__main__':
    unittest.main()
