from flask import Response, request, make_response, render_template, Request
from sqlalchemy import select

from . import app
from db import Task, Config

Session = Config.SESSION


@app.get("/create")
def task():
    return render_template("create.html")


@app.post("/create")
def create_task():
    name = request.form.get("name")

    with Session.begin() as session:
        task = Task(name=name)
        session.add(task)

    resp = Response("Task created!")
    resp.set_cookie("name", name, max_age=3600)
    print(resp)
    return resp


@app.get("/get_task")
def get_task():
    name = request.cookies.get("name")
    if name:
        return "<h1>Last task you created: " + name + "</h1>"
    else:
        return "You created no task"


@app.get("/delete")
def delete():
    return render_template("delete.html")


@app.post("/delete")
def delete_task():
    name = request.form.get("name")

    with Session.begin() as session:
        task = session.scalar(select(Task).where(Task.name == name))
        if task:
            session.delete(task)
            resp = Response("Task deleted!")
            cookie_name = request.cookies.get("name")
            if name == cookie_name:
                resp.delete_cookie("name")
            return resp
        else:
            return f"No task with this name:{name}"
