import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:02090702Ro1*@localhost:3306/dbgestaosix'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Desabilita a notificação de modificações no banco de dados