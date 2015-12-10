# -*- coding: utf-8 -*-

import os

__all__ = ['MONGO_DB', 'MONGO_PORT', 'MONGO_USERNAME', 'MONGO_PASSWORD', 'DB_NAME', 'IP', 'PORT', 'MANDRILL_KEY']

MONGO_DB = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = os.environ['mongoUsername']
MONGO_PASSWORD = os.environ['mongoPwd']
DB_NAME = 'congress_report'
IP = '0.0.0.0'
PORT = 8080
MANDRILL_KEY = 'test'
