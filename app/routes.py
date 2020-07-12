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
            location=cl.location,
        ))
    return jsonify(dt)


@app.route('/insert/class', methods=["POST"])
def insert_new_class():
    req = request.get_json()
    new_class = Classes(class_name=req.get("class name"), location=req.get("location"))
    db.session.add(new_class)
    db.session.commit()
    return {"Message": "Create class " + req.get("class name") + " sucessfully"}


@app.route('/search/class/<class_name>', methods=["GET"])
def search_class_by_name(class_name):
    name_of_class = Classes.query.filter_by(class_name=class_name)
    if name_of_class == True:
        return {"Message": "Class" + class_name + " founded"}
    else:
        return {"Message": "Class " + class_name + " does not exist"}


@app.route('/delete/class/<class_name>', methods=["DELETE"])
def delete_class_by_name(class_name):
    name_of_class = Classes.query.filter_by(class_name=class_name).first()
    if name_of_class == True:
        db.session.delete(name_of_class)
        db.session.commit()
        return {"Message": "Class " + class_name + " deleted sucessfully"}
    else:
        return{"Message": "Class " + class_name + " does not exist"}


@app.route('/class/student/<id>', methods=["DELETE"])
def delete_student_by_id(id):
    student_id = Students.query.filter_by(id=id).first()
    if student_id == True:
        db.session.delete(student_id)
        db.session.commit()
        return {"Message": "Student " + student_id + " deleted sucessfully"}
    else:
        return{"Message": "Student " + student_id + " does not exist"}


@app.route('/insert/<id>/student', methods=["POST"])
def insert_student(id):
    req = request.get_json()
    new_student = Students(student_name=req.get("student name"), age=req.get(
        "age"), height=req.get("height"), class_id=req.get("class id"))
    find_id_of_class = session.query(Classes).filter_by(id=id).all()
    if find_id_of_class == True:
        db.session.add(new_student)
        db.session.commit()
        return {"Message": "Create student " + req.get("student name") + " in class " +
                req.get("class id") + " sucessfully"}
    else:
        return {"Message": "Class not exist"}


@app.route('/class/<class_name>/<student_name>', methods=["GET"])
def search_student_by_class_name(class_name, student_name):
    return "OK"
