from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# setting up the data base the following lines of code first create a relative path to the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# the db is initialized using app as settings
db = SQLAlchemy(app)


# setting up the rules for the db, like what pieces are required

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date_created =  db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

"""
to create db first execute python3 
    then in python shell: from app import db
                    next: db.create_all()
                    

"""


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # correspondes to the form created in index.html
        # the form name is content; we will take the info from the form and pass it along to the todo class

        task_content = request.form["content"]   
        new_todo = Todo(content = task_content)
        
        # adding new task to db 
        # first we add the task then commit the changes to the db
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return 'there was an issure adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)




if __name__ == "__main__":
    app.run(debug=True)

