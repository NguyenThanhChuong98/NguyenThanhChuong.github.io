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
    print(new_class)
    check_if_class_name_exist = Classes.query.filter(Classes.class_name == req.get("class name")).first()
    print(check_if_class_name_exist)
    if Classes.class_name:
        return {"Message": "Class " + req.get("class name") + " already exist"}
    else:
        db.session.add(new_class)
        db.session.commit()
        return {"Message": "Create class " + req.get("class name") + " sucessfully"}


@app.route('/search/class/<class_name>', methods=["GET"])
def search_class_by_name(class_name):
    name_of_class = Classes.query.filter_by(class_name=class_name)
    print(name_of_class)
    if name_of_class == True:
        return {"Message": "Class" + class_name + " founded"}
    else:
        return {"Message": "Class " + class_name + " does not exist"}


@app.route('/delete/class/<class_name>', methods=["DELETE"])
def delete_class_by_name(class_name):
    name_of_class = Classes.query.filter_by(class_name=class_name).first()
    print(name_of_class)
    if name_of_class == True:
        db.session.delete(name_of_class)
        db.session.commit()
        return {"Message": "Class " + class_name + " deleted sucessfully"}
    else:
        return{"Message": "Class " + class_name + " does not exist"}


@app.route('/class/student/<id>', methods=["DELETE"])
def delete_student_by_id(id):
    student_id = Students.query.filter_by(id=id).first()
    print(student_id)
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
    find_id_of_class = Classes.query.filter(Classes.id == id).first()
    print(find_id_of_class)
    if find_id_of_class:
        db.session.add(new_student)
        db.session.commit()
        return {"Message": "Create student " + req.get("student name") + " in class " + " sucessfully"}
    else:
        return {"Message": "Class not exist"}


@app.route('/class/<student_class_id>/<student_name>', methods=["GET"])
def search_student_by_class_name(student_class_id, student_name):
    get_student_class_id = Students.query.filter(Students.class_id == student_class_id).first()
    print(get_student_class_id)
    if get_student_class_id:
        get_student_name = Students.query.filter(Students.student_name == student_name).first()
        print(get_student_name)
        if get_student_name:
            return {"Found student" + student_name + "in class"}
    else:
        return {"Student " + student_name + "not exist"}
