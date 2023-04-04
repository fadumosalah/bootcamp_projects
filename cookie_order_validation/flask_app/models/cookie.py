from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Cookie:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.cookietype = data['cookietype']
        self.amount = data['amount']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_cookie(data):
        is_valid = True 
        if len(data['name']) < 2:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['cookietype']) < 2:
            flash("Cookie type must be at least 3 characters.")
            is_valid = False
        if int(data['amount']) < 1:
            flash("Order must be for at lease 1 box")
            is_valid = False
        return is_valid

    @classmethod
    def create_order(cls, data):
        query ="""
        INSERT Into cookies (name, cookietype, amount)
        VALUES (%(name)s, %(cookietype)s, %(amount)s)
        """
        results = connectToMySQL('cookie_orders').query_db(query,data)
        return results
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookies;"
        results = connectToMySQL('cookie_orders').query_db(query)
        cookies = []
        for cookie in results:
            cookies.append(cls(cookie))
            return cookies
        
    @classmethod
    def get_one(cls,cookie_id):
        query = """
        SELECT * FROM cookies
        WHERE id = %(id)s;
        """
        data ={
            "id": cookie_id
        }
        results = connectToMySQL('cookie_orders').query_db(query,data)
        return cls(results[0])
    
    @classmethod
    def update_order(cls, data):
        query="""
        UPDATE cookies SET name = %(name)s, cookietype = %(cookietype)s, amount = %(amount)s
        WHERE id = %(id)s;
        """
        return connectToMySQL('cookie_orders').query_db(query, data)