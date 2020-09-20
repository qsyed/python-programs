from flask import Flask, render_template
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


@app.route("/")
def index():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)

