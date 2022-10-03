import os

TOKEN = '5629380216:AAFDA16iaSPiXJxXy_MAiZR6U-vTm-5G6rU'
# название БД
NAME_DB = 'products.sqlite'
# версия приложения
VERSION = '0.0.1'

# родительская директория
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# путь до базы данных
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0
