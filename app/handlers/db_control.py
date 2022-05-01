import sqlite3
from sqlite3 import Error

class db:
    con = 0 
    def __init__(self) -> None:
        try:
            self.con = sqlite3.connect('mydatabase.db')
            self.__create_table()
        except Error:
            print(Error)

    def __create_table(self):
        cursorObj = self.con.cursor()
        cursorObj.execute('create table if not exists Рецепты(id INTEGER PRIMARY KEY, Название TEXT, Сложность INTEGER, Рецепт TEXT)')
        self.con.commit()
    
    def add_recipe(self, user_data: dict):
        cursorObj = self.con.cursor()
        data = tuple(user_data.values())
        cursorObj.execute('INSERT INTO Рецепты(Название, Сложность, Рецепт) VALUES(?, ?, ?)', data)