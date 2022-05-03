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
        cur = self.con.cursor()
        cur.execute('create table if not exists Рецепты(id INTEGER PRIMARY KEY, Название TEXT, Сложность INTEGER, Рецепт TEXT)')
        self.con.commit()
    
    def add_recipe(self, user_data: dict):
        cur = self.con.cursor()
        data = tuple(user_data.values())
        cur.execute('INSERT INTO Рецепты(Название, Сложность, Рецепт) VALUES(?, ?, ?)', data)
        self.con.commit()
    
    def show_recipes(self):
        '''Показыавет первые рецепты из базы данных'''
        cur = self.con.cursor()
        cur.execute('SELECT id, Название, Сложность FROM Рецепты')
        return cur.fetchall() 