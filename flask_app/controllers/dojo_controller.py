from flask_app import app
from flask import session, render_template, request, redirect
from flask_app.models.dojo_model import Dojo


@app.route( "/" )
@app.route( "/home" )
@app.route( "/dojos" )
@app.route( "/dashboard" )
def display_dashboard():
    list_dojos = []
    list_dojos = Dojo.get_all()
    return render_template( "index.html", list_dojos = list_dojos )

@app.route( "/dashboard", methods = [ 'POST' ] )
def create_dojo():
    Dojo.create( request.form )
    return redirect( "dashboard" )

@app.route( "/dojo/<int:id>/details" )
def get_dojo_by_id( id ):
    data = {
        "id" : id
    }
    current_dojo = Dojo.get_one_with_ninjas( data )
    return render_template( "dojoDetails.html", current_dojo = current_dojo )

@app.route( "/dojo/<int:id>/update" )
def display_update_dojo_by_id( id ):
    data = {
        "id" : id
    }
    current_dojo = Dojo.get_one( data )
    return render_template( "updateDojoForm.html", current_dojo = current_dojo )

@app.route( "/dojo/<int:id>/update", methods = [ 'POST' ] )
def update_dojo_by_id( id ):
    data = {
        "id" : id,
        "name" : request.form[ 'name' ]
    }
    Dojo.upodate_one( data )
    return redirect( "/dashboard" )

@app.route( "/dojo/<int:id>/delete" )
def delete_dojo_by_id( id ):
    data = {
        "id" : id
    }
    Dojo.delete_one( data )
    return redirect( "/dashboard" )