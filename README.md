# Recipes-API
## :falafel: About

The Recipe API provides endpoints for managing recipes, enabling communication between front-end and back-end systems. It facilitates core functionalities such as creating, retrieving, updating, and deleting recipes, as well as functionalities related to recipe authors, categories, and tags, for example. This API serves as a robust foundation for applications requiring recipe organization capabilities, offering seamless integration and efficient data management. Whether you're developing a cooking application, meal planning platform, or culinary database, the Recipe API streamlines recipe management processes for enhanced productivity and functionality.

### :clipboard: Tecnologies and Tolls
* Python
* Django REST Framework
  
### Features
* CRUD operations for recipes, tags, categories, and authors
* Users (non-authenticated) can read queries on recipes, tags, categories, and authors
* Authentication via JWT token
* Filtering recipes based on their characteristics with Django Rest Filtering
* Publish a recipe (update is_published status)

### Model

Below we have the Django ORM related to the recipe model:
![RecipeModel](https://github.com/WandersoNoleto/Recipes-API/blob/main/doc_files/RecipeModel.png)
After being serialized, this is how the data travels via JSON.
```
{
	"id": 7,
	"title": "Stroganoff",
	"description": "A type of food consisting of meat or mushrooms in a sauce that contains sour cream",
	"author": 1,
	"public": false,
	"category": null,
	"tags": [],
	"preparation": "25 minutos",
	"tag_objects": [],
	"preparation_time": 25,
	"preparation_time_unit": "minutos",
	"servings": 2,
	"servings_unit": "persons",
	"preparation_steps": "Have butcher tenderize steak Cut in strips and brown in olive oil Add onions & sauté ; Add tomato juice and simmer until tender Add sliced mushrooms and yogurt and simmer for five more minutes Add spices to taste Serve with vegetables or salad",
	"cover": null
}
```



## :gear: Installation Guide

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

What things you need to install the software and how to install them

First, clone the repository
```
git clone https://github.com/WandersoNoleto/Recipes-API.git
```
Install the dependencies listed in the requirements.txt file
```
pip install -r requirements.txt
```
###### :key: Create a .env file and set the variables according to the [.env copy](https://github.com/WandersoNoleto/Recipes-API/blob/main/.env%20copy).

Generate a new Django key and assign it to SECRET_KEY (in Python CLI)
```
from django.core.management import utils
print(utils.get_random_secret_key())
```

Use the command to run the service
```
python3 manage.py runserver
```



## :world_map: API Endpoints
##### Here is the <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/insomnia/insomnia-original.svg" width="15" height="15"> [Insomnia File](https://github.com/WandersoNoleto/Recipes-API/blob/main/doc_files/Insomnia_teste_recipe_api.json)  with the routes already configured.

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /recipes/| Search all registered recipes or just public recipes if use only_published=true|
| GET | /recipes/int:id/ | View recipe details |
| POST | /recipes/| Register a new recipe |
| PATCH | /recipes/int:id/| To update recipe values |
| PATCH | /recipes/publish_recipe/int:id/ | Change the is_published recipe state for True |
| DELETE |  /recipes/int:id/ | Delete a recipe |
| GET | /authors/api/| Search all registered authors |
| GET | /authors/api/me/ | View authenticated user details |
| POST | /authors/api/| Register a new author |
| PATCH | /authors/api/int:id/| To update author values |
| DELETE |  /authors/api/int:id/ | Delete a author |
| GET | /categories/| Search all registered categories |
| POST | /categories/| Register a new category |
| PATCH | /categories/int:id/| To update category values |
| DELETE |  /categories/int:id/ | Delete a category |
| GET | /tags/| Search all registered tags |
| POST |/tags/| Register a new tag |
| PATCH | /tags/int:id/| To update tag values |
| DELETE |  /tags/int:id/ | Delete a tag |
| POST |/api/token/| To generate access and refresh tokens (provide username and password) |
| POST |/api/token/refresh/ | To generate a new access token (provide refresh token)
| POST |/api/token/verify/  | To verify if the user is authenticated
