from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__( self, data ):
        self.id = data[ 'id' ]
        self.first_name = data[ 'first_name' ]
        self.last_name = data[ 'last_name' ]
        self.age = data[ 'age' ]
        self.created_at = data[ 'created_at' ]
        self.updated_at = data[ 'updated_at' ]
        self.dojo_id = data[ 'dojo_id' ]

    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM ninjas;"
        result = connectToMySQL( DATABASE ).query_db( query )
        list_ninjas = []

        for row in result:
            list_ninjas.append( cls( row ) )

        return list_ninjas

    @classmethod
    def create( cls, data ):
        query = "INSERT INTO ninjas(first_name, last_name, age, dojo_id) VALUES( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );"

        id_new_ninja = connectToMySQL( DATABASE ).query_db( query, data )
        return id_new_ninja

    @classmethod
    def get_one( cls, data ):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL( DATABASE ).query_db( query, data )

        if len( result ) > 0:
            ninja = cls( result[ 0 ] )
            return ninja
        else:
            return None

    @classmethod
    def upodate_one( cls, data ):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s WHERE id = %(id)s;"
        return connectToMySQL( DATABASE ).query_db( query, data )

    @classmethod
    def delete_one( cls, data ):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"

        return connectToMySQL( DATABASE ).query_db( query, data )