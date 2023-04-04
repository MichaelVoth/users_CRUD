from flask import render_template, redirect, request    #Imports flask functionalilty
from flask_app import app   #Imports flask app
from flask_app.models.user import User #imports user class

@app.route('/')
def index_page():           #displays all users in a table
    return render_template('index.html', users = User.all_users())

@app.route('/add')
def add_user():             #redirects to add_user page
    return render_template('add_user.html')

@app.route('/process',methods=['POST'])
def process_new_user():     #adds form data to DB and redirects to individual page
    user = User.create_user(request.form)
    return redirect(f'/show/{user}')

@app.route('/show/<int:id>')
def show_user(id):          #Shows info for one user
    data = {'id':id}
    return render_template('show_user.html',user=User.show_user(data))

@app.route('/edit/<int:id>')
def edit_user(id):          #redirects to form with individual info displayed
    data = {'id':id}
    return render_template('edit_user.html',user = User.show_user(data))

@app.route('/update', methods=['POST'])
def update_user():          #Updates user info in DB
    User.update_user(request.form)
    return redirect(f"/show/{request.form['id']}")

@app.route('/delete/<int:id>')
def delete(id):             #Removes user from DB
    User.delete(id)
    return redirect('/')