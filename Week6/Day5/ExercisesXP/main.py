import psycopg2
import re 

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'popova129'
DATABASE = 'bootcamp'

def run_query(query):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        results = cursor.fetchall()
        connection.close()
        return results
    except:
        connection.close()

class MenuItem():
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    def save(self):
        insert_query = (f"insert into  (name, price) values ('{self.name}', {self.price})")
        run_query(insert_query)

    @classmethod
    def delete(name):
        query = f'delete from menu where name = "{name}"'
        run_query(query)

    def update(self, name, price):
        query = f'update menu set price = {price}, set name = "{name}" where name = "{self.name}"'
        run_query(query)
        
    @classmethod
    def all():
        query = f'select * from menu'
        run_query(query)

    @classmethod
    def get_by_name(name):
        query = f'select * from menu where name = "{name}"'
        run_query(query)

item = MenuItem('Burger', 35)
item.save()
item.delete()
item.update('Veggie Burger', 37)
item2 = MenuItem.get_by_name('Beef Stew')
items = MenuItem.all()