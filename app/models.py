from app import db


class Classes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(64), index=True, unique=True)
    location = db.Column(db.String(64), index=True)
    students = db.relationship('Students', backref='classes', lazy='dynamic')

    def to_dict(self):
        return dict(
            id=self.id,
            class_name=self.class_name,
            location=self.location
        )


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    student_name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer)
    height = db.Column(db.Integer)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))

    def to_dict(self):
        return dict(
            id=self.id,
            student_name=self.student_name,
            age=self.age,
            height=self.height,
            class_id=self.class_id
        )
