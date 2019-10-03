from database_class import *
from recipe_class import *



conn_db =database( 'localhost,1433', 'Recipe_db', 'SA', 'Passw0rd2018')

recipe1 = recipe("Blue lagoon", "red caracao, vodka, lemonade", "mix in a pitcher, drop in some straws, enjoy!", "DA157JQ")
recipe.recipe_to_file(recipe1)
conn_db.add_recipe(recipe1.recipe_name, recipe1.ingredients, recipe1.method, recipe1.postcode)
# conn_db.delete_recipe('Blue lagoon')

print(conn_db.search_recipe('Red lagoon'))

conn_db.all_recipes()