from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from werkzeug.utils import redirect

app = Flask(__name__)

# database config and setup
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(120), nullable=False)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r' % self.id


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # value of taskContent is the form input with the name taskcontent
        taskContent = request.form['taskcontent']
        newTask = Todo(content=taskContent)
        # good practice to use try catches wherever poss, here it seems to be try
        try:
            db.session.add(newTask)
            db.session.commit()
            return redirect('/')

        except:
            return "there's an error adding your task bro"

    else:
        #query to return tasks in order of date created.  
        tasks = Todo.query.order_by(Todo.dateCreated).all()  
        return render_template("index.html", tasks = tasks)


# this is so your module doesnt insta run in import
if __name__ == '__main__':
    app.run(debug=True)
