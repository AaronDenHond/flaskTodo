# Basic Todo App in Flask (Python).

https://aarondenhond.github.io/flaskTodo/

It has standard CRUD functionality and I choose to try out SQLite, as a dedicated backend wasn't needed for this project.
I had also only worked with MySQL or writing to a local file before this, so it was nice seeing how easy SQLite is to setup
and use for small projects.

Why Flask over Django? Django is a fullstack, big opinionated (MVC structure) framework for Python like Symfony or Laravel are to PHP.
As such it's generally considered better to only work with those once you have a basic/decent grasp of the language first. I'm completely
new to Python, but feel like it's a waste of time to go over the absolute basics in a new language when I have basics of other ones
(var declaration, functions, loops, arrays,...). With a microframework like Flask I get to learn the language, as well as get the tools 
to make smaller scale applications more easily, while still having to write most of the code myself without too much boilerplating, which will
help me grasp the language more easily.

## What I've learned

Python is very readable and very enjoyable to write. 
Basic stuff like setting up a database connection, routing and templating
is very straightforward and clear in Flask. I also enjoyed using SQLAlchemy as an ORM although I will admit I miss
Symfony's Doctrine and how powerful it is.

The bad stuff for me was the boilerplate setup and dependency management overall. I had to activate my virtual
environment multiple times for some reason, had trouble with adding the interpreter even though it should be very easy
and often times my IDE would throw errors with missing dependencies even if they were there.
The overall writing in Flask made sense and was enjoyable, but the environment to work in was less so in my opinion doing this small project.
I'm sure the issue was more my incompetence with the framework than the other way around, but it's something I felt working on this.

Overall the experience was a pretty fun one and I intend to keep using Flask for smaller scale applications.

**Some technical stuff I want to remember :** 

if (name == "main"):
    app.run(debug=True)

Why this piece of code?
Basically, it's boilerplate we don't really have to worry about. It's main use is to 'guard' a script. Without this, every script you import 
would run at import time. We need some conditions so we can choose when to run it and export our scripts as modules. TLDR : guarded scripts > guardless scripts

Templates in Flask by default work with Jinja2 syntax. Comparable to other frameworks we've seen like symfony that use Twig.

{{}} in Jinja2 returns what's in it as a string. 

/// is a relative path, //// absolute in sqlite

flask seems to auto import stuff like datetime etc. 

dont forget to import db object in the python shell.


## Issues I've encountered working with Flask for the first time 

#### Issue 1 : incorrectly installed packages 
denoted by ~ before package? 
Atleast I think so.
Deleting those folder removed the warning issues.

#### Issue 2 : python virtualenv env, file not found
Solution : python -m virtualenv env, need the -m to make folder

Install the virtualenv package
Create the virtual environment
Activate the virtual environment

(env) shows environment is activated

why this virtual environment? so any packages/libs we install are contained within this environment and not installed globally

#### Issue 3 : Imported Flask but wasn't recognized.
Problem? Interpreter. In python we have to select an interpreter to process our code and by default the global python .exe is selected.
When using a virtual environment we need to change to the venv interpreter or it won't recognize the libs and packages.
