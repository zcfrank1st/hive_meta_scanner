# -*- coding: utf-8 -*-
__author__ = 'zcfrank1st'

import MySQLdb


class MySQLRunner(object):
    def __init__(self, host, user, passwd, db):
        self.conn = MySQLdb.connect(host=host, user=user, passwd=passwd)
        self.conn.select_db(db)
        self.cursor = self.conn.cursor()

    def run(self, sql):
        self.cursor.execute(""" %s """ % sql)
        return self

    def fetch_all(self):
        return self.cursor.fetchall()

    def close_conn(self):
        self.conn.close()


def test():
    print "hello world"

if __name__ == '__main__':
    runner = MySQLRunner('192.168.100.107', 'root', 'root', 'dev')
    results = runner.run('select * from mds_itemtable').fetch_all()
    runner.close_conn()
    print results