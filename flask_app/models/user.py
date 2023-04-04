from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = "users"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def all_users(cls):             #Gets all info from DB
        query = "SELECT * FROM users;"
        results = connectToMySQL('users').query_db(query)
        users = []
        for a_user in results:
            users.append(cls(a_user))
        return users
    
    @classmethod
    def create_user(cls, data):     #Adds form data to DB as new row
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s,%(email)s);"
        results = connectToMySQL(cls.DB).query_db(query,data)
        return results
    
    @classmethod
    def show_user(cls,data):        #Gets one row of data from DB
        query = """SELECT * FROM users
                    WHERE id = %(id)s"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update_user(cls,data):      #Updates one row in DB
        query = """UPDATE users
                SET first_name =%(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(id)s;"""
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def delete(cls, id):            #Deletes one row from DB
        query  = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": id}
        return connectToMySQL(cls.DB).query_db(query, data) 