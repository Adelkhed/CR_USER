
from flask_app.config.mysqlconnection import connectToMySQL, DB

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="SELECT * FROM users ;"
        results= connectToMySQL(DB).query_db(query)
        users=[]
        for user in results:
            users.append(cls(user))
        return users
   
    @classmethod
    def save(cls,data):
        query= "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def update_user(cls, data):
            query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
            return connectToMySQL(DB).query_db(query, data)
       
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        if result:
            return cls(result[0])
        return None
    @classmethod
    def delete(cls, user_id):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        return connectToMySQL(DB).query_db(query, data)