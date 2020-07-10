from app import app
from app import db
from app.models import Classes, Students
from flask import make_response, jsonify
from flask import request
import json


@app.route('/classes', methods=["GET"])
def get_all_classes():
    classes = Classes.query.all()
    dt = []
    for cl in classes:
        dt.append(dict(
            id=cl.id,
            class_name=cl.class_name,
            location=cl.location
        ))
    return jsonify(dt)


@app.route('/class', methods=["POST"])
def insert_new_class():
    req = request.get_json()
    new_class = Classes(class_name=req.get("class name"), location=req.get("location"))
    db.session.add(new_class)
    db.session.commit()
    return {"Message": "Create class " + req.get("class name") + " Sucessfully"}


@app.route('/search/class/<class_name>', methods=["GET"])
def search_class_by_name(class_name):
    name_of_class = Classes.query.filter_by(class_name=class_name).first_or_404(
        description='There is no data with {}'.format(class_name))
    return {"Message": "Class " + class_name + " Founded"}


@app.route('/delete/class/<class_name>', methods=["DELETE"])
def delete_class_by_name(class_name):
    name_of_class = Classes.query.filter_by(class_name=class_name).first_or_404(
        description='There is no data with {}'.format(class_name))
    db.session.delete(name_of_class)
    db.session.commit()
    return {"Message": "Class " + class_name + " Deleted Sucessfully"}


@app.route('/class/<class_name>/<student_name>', methods=["GET"])
def search_student_by_class_name(class_name, student_name):
    return "OK"


@app.route('/insert/class/student', methods=["POST"])
def insert_student():
    req = request.get_json()
    new_student = Student(student_name=req("student name"), age=req.get(
        "age"), height=req.get("height"), class_id=req.get("class_id"))
    db.session.add(new_student)
    db.session.commit()
    return {"Message": "Create student " + req.get("student name") + " Sucessfully"}
