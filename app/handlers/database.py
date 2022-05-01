import sqlite3
from sqlite3 import Error

class database:
    con = 0 
    def __init__(self) -> None:
        try:
            self.con = sqlite3.connect('mydatabase.db')
            self.__create_table()
        except Error:
            print(Error)

    def __create_table(self):
        cursorObj = self.con.cursor()
        cursorObj.execute('create table if not exists Рецепты(id integer, Название text, Сложность integer, Рецепт text)')
        self.con.commit()