# -*- coding: utf-8 -*-
__author__ = 'zcfrank1st'

from mysql_runner import MySQLRunner

READER_HOST = '192.168.100.107'
READER_USER = 'root'
READER_PASSWORD = 'root'
READER_DB = 'dev'

WRITER_HOST = ''
WRITER_USER = ''
WRITER_PASSWORD = ''
WRITER_DB = ''

reader = MySQLRunner(host=READER_HOST, user=READER_USER, passwd=READER_PASSWORD, db=READER_DB)
writer = MySQLRunner(host=WRITER_HOST, user=WRITER_USER, passwd=WRITER_PASSWORD, db=WRITER_DB)
