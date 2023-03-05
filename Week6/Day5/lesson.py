import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'popova129'
DATABASE = 'bootcamp'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor() # the cursor is the tool to run queries

class MenuItem:

    def __init__(self, name: str, price: int) -> None:
        self.name = name
        self.price = price
    
    def save(self) -> None:
        query = f"insert into menu (name, price) values ('{self.name}', {self.price})"
        run_query(query)

    def delete(self) -> None:
        query = f"delete from menu where name = '{self.name}'"
        run_query(query)

    def update_price(self, new_price: int) -> None:
        query = f"update menu set price = {new_price} where name = '{self.name}'"
        run_query(query)

    def update_name(self, new_name: str) -> None:
        query = f"update menu set name = {new_name} where name = '{self.name}'"
        run_query(query)

    def all(self) -> list:
        query = "select * from menu;"
        return run_query(query)

def run_query(query: str) -> list:

    cursor.execute(query)
    output = None
    
    try:
        output = cursor.fetchall() # the cursor also holds the output from the query
    except:
        
        connection.commit()

    return output

def load_manager(*items: tuple):
    menu_items = []
    for item in items:
        name, price = item
        menu_items.append(MenuItem(name, price))

    return menu_items

menu_items = load_manager(('Burger', 10), ('Pizza', 10), ('Buratta', 7))