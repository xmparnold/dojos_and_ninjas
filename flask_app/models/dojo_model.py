from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninja_model import Ninja

list_ninjas = []

class Dojo:
    def __init__( self, data ):
        self.id = data[ 'id' ]
        self.name = data[ 'name' ]
        self.created_at = data[ 'created_at' ]
        self.updated_at = data[ 'updated_at' ]

    @classmethod
    def get_one( cls, data ):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )

        if len( result ) > 0:
            return cls( result[0] )
        else:
            return None

    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM dojos;"
        result = connectToMySQL( DATABASE ).query_db( query )

        list_dojos = []

        for row in result:
            list_dojos.append( cls( row ) )
        
        return list_dojos

    @classmethod
    def create( cls, data ):
        query = "INSERT INTO dojos(name) VALUES(%(name)s);"

        id_new_dojo = connectToMySQL( DATABASE ).query_db( query, data )
        return id_new_dojo

    @classmethod
    def upodate_one( cls, data ):
        query = "UPDATE dojos SET name = %(name)s WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )
    
    @classmethod
    def delete_one( cls, data ):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )

    @classmethod
    def get_one_with_ninjas( cls, data ):
        query = "SELECT * FROM dojos JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"

        result = connectToMySQL( DATABASE ).query_db( query, data )

        if len( result ) > 0:
            selected_dojo = cls( result[ 0 ] )
            list_ninjas = []
            for row in result:
                current_ninja = {
                    "id" : row[ "ninjas.id" ],
                    "first_name" : row[ "first_name" ],
                    "last_name" : row[ "last_name" ],
                    "age" : row[ "age" ],
                    "created_at" : row[ "ninjas.created_at"],
                    "updated_at" : row[ "ninjas.updated_at" ],
                    "dojo_id" : row[ "dojo_id" ]
                }
                ninja = Ninja( current_ninja )
                list_ninjas.append ( ninja )
            selected_dojo.list_ninjas = list_ninjas
            return selected_dojo

        return None