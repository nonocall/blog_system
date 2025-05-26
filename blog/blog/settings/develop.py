from .base import * # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'mssql',  # 使用mssql-django提供的引擎
        'NAME': 'model',  # 数据库名称
        'USER': 'sa',  # 数据库用户名
        'PASSWORD': '1',  # 数据库密码
        'HOST': '127.0.0.1',  # SQL Server主机名或IP地址
        'PORT': '1434',  # SQL Server端口号，默认为1433
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',  # 指定ODBC驱动程序
        },
    },
}
