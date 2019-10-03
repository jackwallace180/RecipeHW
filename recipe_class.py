import pyodbc
import requests
# define a class recipe

    # Give it the need attributes

    #defining methods
        #new()
            # creates a recipe object

        #save()
            #saves a recipe object to DB (make persistant)

        #read()
            # read one object

        #all()
            # gets all the instances from DB
            # makes instances
            # store in a list


        # destroy()
            # one object

class recipe():
    def __init__(self, recipe_name, ingredients, method, postcode):
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.method = method
        self.postcode = postcode








