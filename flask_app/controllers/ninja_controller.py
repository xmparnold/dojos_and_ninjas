from xml.etree.ElementTree import tostring
from flask_app import app
from flask import session, render_template, request, redirect
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

list_ninjas = []

@app.route( "/ninja" )
def display_create_ninja_form():
    list_dojos = []
    list_dojos = Dojo.get_all()
    return render_template( "ninjaCreationForm.html", list_dojos = list_dojos )

@app.route( "/ninja", methods = [ 'POST' ] )
def create_ninja():
    Ninja.create( request.form )
    return redirect( "/dashboard" )

@app.route( "/ninja/<int:id>/delete" )
def delete_ninja_by_id( id ):
    data = {
        "id" : id
    }
    current_ninja = Ninja.get_one( data )
    current_dojo_id = str(current_ninja.dojo_id)
    Ninja.delete_one( data )
    return redirect( "/dojo/" + current_dojo_id + "/details" )
