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


@app.route('/class/insert', methods=["POST"])
def insert_new_class():
    req = request.get_json()
    new_class = Classes(class_name=req.get("class name"), location=req.get("location"))
    print(new_class)
    check_if_class_name_exist = Classes.query.filter(Classes.class_name == req.get("class name")).first()
    print(check_if_class_name_exist)
    if check_if_class_name_exist:
        return {"Message": "Class " + req.get("class name") + " already exist"}
    else:
        db.session.add(new_class)
        db.session.commit()
        return {"Message": "Create class " + req.get("class name") + " sucessfully"}


@app.route('/class/search/<class_name>', methods=["GET"])
def search_class_by_name(class_name):
    name_of_class = Classes.query.filter_by(class_name=class_name)
    print(name_of_class)
    if name_of_class:
        return {"Message": "Class" + class_name + " founded"}
    else:
        return {"Message": "Class " + class_name + " does not exist"}


@app.route('/class/delete/<class_name>', methods=["DELETE"])
def delete_class_by_name(class_name):
    name_of_class = Classes.query.filter_by(class_name=class_name).first()
    print(name_of_class)
    if name_of_class:
        db.session.delete(name_of_class)
        db.session.commit()
        return {"Message": "Class " + class_name + " deleted sucessfully"}
    else:
        return{"Message": "Class " + class_name + " does not exist"}


@app.route('/student/insert/<id>', methods=["POST"])
def insert_student(id):
    req = request.get_json()
    new_student = Students(student_name=req.get("student name"), age=req.get(
        "age"), height=req.get("height"))
    find_id_of_class = Classes.query.filter(Classes.id == id).first()
    print(find_id_of_class)
    if find_id_of_class:
        db.session.add(new_student)
        db.session.commit()
        return {"Message": "Create student " + req.get("student name") + " sucessfully"}
    else:
        return {"Message": "Class not exist"}


@app.route('/student/search/<class_id>/<student_name>', methods=["GET"])
def search_student_by_class_name(class_id, student_name):
    get_student_class_id_and_name = Students.query.filter(
        Classes.id == class_id,
        Students.student_name == student_name).first()
    print(get_student_class_id_and_name)
    if get_student_class_id_and_name:
        return {"Message": "Student " + student_name + " Founded"}
    else:
        return {"Message": "Student " + student_name + " Not Founded"}


@app.route('/student/delete/<class_id>/<student_id>', methods=["DELETE"])
def delete_student_by_class_id(class_id, student_id):
    get_class_id_and_student_id = Students.query.filter(
        Classes.id == class_id, Students.id == student_id).first()
    print(get_class_id_and_student_id)
    if get_class_id_and_student_id:
        db.session.delete(get_class_id_and_student_id)
        db.session.commit()
        return {"Message": "Student " + student_id + " deleted sucessfully"}
    else:
        return{"Message": "Student " + student_id + " does not exist"}


@app.route('/<class_id>/students', methods=["GET"])
def get_all_students_by_class_id(class_id):
    query1 = Classes.query.fitler(Classes.id == class_id).first()
    dt = []
    if query1:
        query2 = Students.query.order_by(Students.height).all()
        for cl in students:
            dt.append(dict(
                id=cl.id,
                student_name=cl.student_name,
                age=cl.age,
                height=cl.height,
                class_id=cl.class_id
                ))
        return jsonify(dt)
    else:

    return "OK"

for cl in classes:
        dt.append(dict(
            id=cl.id,
            class_name=cl.class_name,
            location=cl.location,
        ))
    return jsonify(dt)
