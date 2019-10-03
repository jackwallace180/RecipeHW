from database_class import *
from recipe_class import *



conn_db =database( 'localhost,1433', 'Northwind', 'SA', 'Passw0rd2018')

recipe1 = recipe("Blue lagoon", "blue caracao, vodka, lemonade","mix in a pitcher, drop in some straws, enjoy!", "DA157JQ" )

print(recipe1.recipe_name)