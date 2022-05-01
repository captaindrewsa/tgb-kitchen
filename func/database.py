import sqlite3
from sqlite3 import Error

class database:
    con = 0

    def __init__(self) -> None:
        '''Создали соединение'''
        try:
            con = sqlite3.connect('mydatabase.db')
            self.con = con
        except Error:
            print(Error)

    def __sql_table_start(self):
        '''Создали базовую табличку'''
        cursorObj = self.con.cursor()
        cursorObj.execute("CREATE TABLE if not exists Recipes(id integer PRIMARY KEY, Название text, Уровень сложности integer, Краткий рецепт text)")
        self.con.commit()
        
    def init(self):
        self.__sql_table_start()


'''
id  Название    Уровень сложности   Краткий рецепт  

'''