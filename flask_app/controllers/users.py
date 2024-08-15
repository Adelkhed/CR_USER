from flask_app.config import mysqlconnection
from flask import Flask, render_template,redirect ,request ,url_for
from flask_app.models.user import  User
from flask_app import app
from datetime import datetime  

@app.route("/")
def users():
    return redirect("/users")

@app.route("/user/new")
def new():
     return render_template("new_user.html")

@app.route("/user/create", methods=['POST'])
def create_user():
       data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
        }
 
       User.save(data)
   
       return redirect(url_for('get_users'))

@app.route("/users")
def get_users():
     users= User.get_all()
     print(users)
     return render_template('all_users.html',users=users)

@app.route("/users/<int:id>/edit")
def edit_user(id):
     user= User.get_one({'id':id})

     return render_template("update.html", user=user)

@app.route("/users/<int:id>/update", methods=['POST'])
def updated_user(id):
     data= {
          "id":id,
          "first_name": request.form["first_name"],
          "last_name": request.form["last_name"],
          "email":request.form["email"]
     }
     User.update_user(data)
     return redirect("/")

@app.route('/users/delete/<int:user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect('/')

@app.route('/users/<int:id>')
def show_user(id):
     
     user=User.get_one({'id':id})
     updated= user.updated_at.strftime("%B  %drd %Y on %I:%M:%S %p ")
     return render_template("show.html", user=user,updated=updated)

