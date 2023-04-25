from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User

db = "recipes_schema"

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data ['instructions']
        self.date_cooked = data['date_cooked']
        self.minutes = data['minutes']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.author = None


    @classmethod
    def get_all (cls):
        query = "SELECT * FROM recipes"
        results = connectToMySQL(db).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    @classmethod
    def create_recipe(cls, data):
        query = """
            INSERT INTO recipes (name, description, instructions, date_cooked, minutes, user_id) 
            VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(minutes)s, %(user_id)s);
            """
        return connectToMySQL(db).query_db(query,data)


    @staticmethod
    def validate_recipe(recipe):
        is_valid = True # we assume this is true
        if len(recipe['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(recipe['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if len(recipe['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        return is_valid
    
    
    @classmethod
    def get_recipe(cls, data):
        query = """
            SELECT * FROM recipes
            JOIN users ON users.id = recipes.user_id
            WHERE recipes.id = %(id)s;
            """
        results = connectToMySQL(db).query_db(query,data)
        recipe = cls(results[0])
        author_data ={
            "id" : results[0]["users.id"],
            "first_name": results[0]["first_name"],
            "last_name": results[0]["last_name"],
            "email": results[0]["email"],
            "password": results[0]["password"],
            "created_at": results[0]["users.created_at"],
            "updated_at": results[0]["users.updated_at"]
        }
        recipe.author = User(author_data)
        return recipe

    @classmethod
    def updaterecipe(cls, form_data, recipe_id):
        query = f"UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_cooked = %(date_cooked)s, minutes = %(minutes)s WHERE id = {recipe_id};"
        return connectToMySQL(db).query_db(query,form_data)
    
    @classmethod
    def delete_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query,data)
