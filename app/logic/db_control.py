import sqlite3
from sqlite3 import Error
import random as rnd


class db:
    con = 0 
    def __init__(self) -> None:
        '''Создает базу данных'''
        try:
            self.con = sqlite3.connect('mydatabase.db')
            self.__create_table()
        except Error:
            print(Error)

    def __create_table(self):
        '''Создает таблицу'''
        cur = self.con.cursor()
        cur.execute('create table if not exists Рецепты(id INTEGER PRIMARY KEY, Название TEXT, Сложность INTEGER, Рецепт TEXT)')
        self.con.commit()
    
    def add_recipe(self, user_data: dict):
        '''Добавляет новую запись в базу данных'''
        cur = self.con.cursor()
        data = tuple(user_data.values())
        cur.execute('INSERT INTO Рецепты(Название, Сложность, Рецепт) VALUES(?, ?, ?)', data)
        self.con.commit()
    
    def show_recipes(self, count:int = None, rnd_choice=False):
        if count!=None and rnd_choice==True:   
            '''Показыавет count случайных рецептов из базы данных'''
            cur = self.con.cursor()
            cur.execute('SELECT COUNT(*) FROM Рецепты')
            count_recipes = int(cur.fetchall()[0][0])
            list_id = []
            while len(list_id)<count:
                id_recipe = rnd.randint(1,count_recipes)
                if id_recipe not in list_id:
                    list_id.append(id_recipe)
                    continue
            cur.execute('SELECT id, Название, Сложность FROM Рецепты WHERE id IN (%s)' % ','.join('?'*len(list_id)), list_id)
            return cur.fetchall()
        
        elif count==None and rnd_choice==False:
            '''Показыавет рецепты из базы данных'''
            cur = self.con.cursor()
            cur.execute('SELECT id, Название, Сложность FROM Рецепты')
            return cur.fetchall()
        
        elif count!=None and rnd_choice==False:
            '''Показыавет рецепт из базы данных по id'''
            cur = self.con.cursor()
            cur.execute('SELECT id, Название, Сложность, Рецепт FROM Рецепты WHERE id = ?', (count,))
            return cur.fetchall()


    def edit_recipe(self, value:str, id:int, cell: str):
        '''Редактирует выбранное поле рецепта'''
        cur = self.con.cursor()
        if cell.lower() == 'название':
            cur.execute('UPDATE Рецепты SET Название = ? WHERE id = ?', (value, id,))
        if cell.lower() == 'сложность':
            cur.execute('UPDATE Рецепты SET Сложность = ? WHERE id = ?', (int(value), id,))
        if cell.lower() == 'рецепт':
            cur.execute('UPDATE Рецепты SET Рецепт = ? WHERE id = ?', (value, id,))
        self.con.commit()

if __name__ == '__main__':
    db = db()
    print(db.show_recipes(6))