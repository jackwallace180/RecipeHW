import pyodbc
import requests

class database():

        def __init__(self, server, database, username, password):
            self.server = server
            self.database = database
            self.username = username
            self.password = password
            self.conn_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password + '')
            self.cursor = self.conn_db.cursor()

        def filter_query(self, query):
            return self.cursor.execute(query)

        def all_recipes(self):
            rows = self.filter_query("SELECT * FROM Recipe_Table")
            while True:
                record = rows.fetchone()
                if record is None:
                    break
                print('Recipe: ', record.Recipe_Name, ', Ingredients: ', record.Ingredients, ', Method :', record.Method)

        def search_recipe(self, recipe_name):
            find_recipe = self.filter_query(f"SELECT * FROM Recipe_Table WHERE Recipe_Name = '{recipe_name}'")
            return find_recipe.fetchone()

        def add_recipe(self, recipe_name, ingredients, method, postcode):
            self.filter_query(f"INSERT INTO Recipe_Table VALUES ('{recipe_name}','{ingredients}','{method}','{postcode}')")
            self.conn_db.commit()

        def delete_recipe(self, recipe_name):
            self.filter_query(f"DELETE FROM Recipe_Table WHERE Recipe_Name = '{recipe_name}'")
            self.conn_db.commit()

