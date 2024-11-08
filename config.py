import os

'''
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:02090702Ro1*@localhost:3306/dbgestaosix'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Desabilita a notificação de modificações no banco de dados
'''
    
class Config:
    # Outras configurações...
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '02090702Ro1*')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'dbgestaosix')

    # Definir diretamente a URI de conexão como uma string
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
