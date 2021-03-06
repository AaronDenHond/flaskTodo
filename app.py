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


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # value of taskContent is the form input with the name taskcontent
        taskContent = request.form['taskcontent']
        newTask = Todo(content = taskContent)
        
        
        # good practice to use try catches wherever poss, here it seems to be try
        try:
            db.session.add(newTask)
            db.session.commit()
            return redirect('/')

        except:
            return "there's an error adding your task bro unlucky"

    else:
        #query to return tasks in order of date created.  
        tasks = Todo.query.order_by(Todo.dateCreated).all()  
        return render_template("index.html", tasks = tasks)


# Delete functionality. We need a diff route first. when going to that route, we want a delete function to trigger. we need to identify what task to delete
# We want to take smth unique to the task to identify it by, which will be the id of said task/todo.
# We need to query our DB to get the tasks needed.
# We also need to update the hrefs in index.html.

#the <int:id> is needed here cause if we just route to delete, the url doesnt exist when clicking the link.<> is used to specify a variable for dynamic routing.
@app.route('/delete/<int:id>')
def delete(id):
    todoToDelete = Todo.query.get(id)
    
    try:
        db.session.delete(todoToDelete)
        db.session.commit()
        return redirect('/')
    
    except:
        return "there was an issue deleting your todo"
    

# Update functionality. A bit like deleting but with some extra stuff. For example we need the task.content so we can update it.
# We need to pass the task so it knows what we're talking about, so make a var with value being the queried db.
# We need a diff view when going to the url. Make a new one.
# If we go to update page rn, we notice the input field is empty. We need the existing task.content.
# We have to give the var task/todo w/e we call it to the view!

@app.route('/update/<int:id>', methods = ['POST', 'GET'])
def update(id):
    todoToUpdate = Todo.query.get(id)
    if request.method == "POST":
        todoToUpdate.content = request.form["taskcontent"]
        
        try: 
            db.session.commit()
            return redirect('/')
             
        
        except : 
            "didnt work homes"
        
    else:
        return render_template("update.html", task = todoToUpdate)


# this is so your module doesnt insta run in import
if __name__ == '__main__':
    app.run(debug=True)
