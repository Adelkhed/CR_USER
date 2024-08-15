from flask import Flask , render_template, request, redirect, url_for
from user import User
app = Flask(__name__)


@app.route("/")
def new_user():
    return redirect("/users")

@app.route("/user/new", methods=['POST'])
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


if __name__ == "__main__":
    app.run(debug=True)