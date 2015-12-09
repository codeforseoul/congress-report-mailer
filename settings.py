# -*- coding: utf-8 -*-

import os

__all__ = ['MONGO_USERNAME', 'MONGO_PASSWORD', 'IP', 'PORT', 'MANDRILL_KEY']

MONGO_USERNAME = os.environ['mongoUsername']
MONGO_PASSWORD = os.environ['mongoPwd']
IP = '0.0.0.0'
PORT = 8080
MANDRILL_KEY = os.environ['mandrillKey']
