import requests
import json
from flask import Flask, request, render_template, redirect


app = Flask(__name__)
app.config['DEBUG'] = True


# global variables with all the ingredients and recipe id
ingredients = []
recipe_id = []


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html', ingredients = ingredients)
    else:
        ingredient = request.form.get('ingredient')
        ingredients.append(ingredient)
        return redirect('/')

    
# go here to show all the recipes
@app.route('/recipe', methods = ['GET', 'POST'])
def recipe():
    # send ingredient data to backend 
    # generate recipes on another web page
    recipes = []
    api_key = '33c6fab2477342e890a22f8fa6348696'
    number = 8
    base_url = 'https://api.spoonacular.com/recipes/findByIngredients?apiKey=33c6fab2477342e890a22f8fa6348696&ingredients='
    ingredient_url = ',+'.join(ingredients)
    request = requests.get(base_url + ingredient_url + '&number=' + str(number))
    request_json = request.json()

    for i in range(number):
        recipe = {
        'title': request_json[i]['title'], 
        'image': request_json[i]['image'],
        'missed_ingredients': request_json[i]['missedIngredientCount'],
        'used_ingredients': request_json[i]['usedIngredientCount'],
        'likes': request_json[i]['likes'],  
        'id': request_json[i]['id']
        }
        recipes.append(recipe)

    return render_template('recipe.html', recipes = recipes)


recipe = 'test'
@app.route('/price', methods = ['GET', 'POST'])
def price():
    """
    returns the recipe information based on recipe id 
    api_key = '306d1933bfd54f199ec9ce5b4888b79d'
    base_url = 'https://api.spoonacular.com/recipes/findByIngredients?apiKey=306d1933bfd54f199ec9ce5b4888b79d&ingredients='
    x = 'https://api.spoonacular.com/recipes/'
    y = '/priceBreakdownWidget?apiKey=306d1933bfd54f199ec9ce5b4888b79d'
    1082038
    ingredient_url = ',+'.join(ingredients)
    request = requests.get(base_url + ingredient_url + '&number=' + str(number))
    request_json = request.json()
    """

    ingredient = {
        'image': 'https://spoonacular.com/cdn/ingredients_100x100/white-powder.jpg',
        'name': 'baking powder',
        'quantity': '1.0 tsp',
        'price': '$0.54'
    }
    
    return render_template('price.html', ingredient = ingredient)


if __name__ == "__main__":
    app.run(debug=True)



