from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Marks, Coaches  

DB_URL = "postgresql+psycopg2://postgres:AcademyRootPassword@localhost:5432/myspace"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base.metadata.create_all(bind=engine)

app = FastAPI()


def connect_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/marks/add/{student_id}")
def add_student(student_id: int, name: str, marks: int, db: Session = Depends(connect_db)):
    student = Marks(student_id=student_id, name=name, marks=marks)
    db.add(student)
    db.commit()
    db.refresh(student)
    return {"message" : student}


@app.get("/marks/check/{student_id}")
def check_student(student_id: int, db: Session = Depends(connect_db)):
    student = db.query(Marks).filter(Marks.student_id == student_id).first()
    if student:
        return student
    return {"error": "Student not found"}


@app.get("/marks/all")
def get_all_students(db: Session = Depends(connect_db)):
    return db.query(Marks).all()


@app.put("/marks/update/{student_id}")
def update_student(student_id: int, name: str, marks: int, db: Session = Depends(connect_db)):
    student = db.query(Marks).filter(Marks.student_id == student_id).first()
    if student:
        student.name = name
        student.marks = marks
        db.commit()
        db.refresh(student)
        return student
    return {"error": "Student not found"}

@app.delete("/marks/delete/{student_id}")
def delete_student(student_id: int, db: Session = Depends(connect_db)):
    student = db.query(Marks).filter(Marks.student_id == student_id).first()
    if student:
        db.delete(student)
        db.commit()
        return {"message": f"Student {student_id} deleted"}
    return {"error": "Student not found"}


@app.delete("/marks/delete_all")
def delete_all_students(db: Session = Depends(connect_db)):
    db.query(Marks).delete()
    db.commit()
    return {"message": "All students deleted"}

@app.post("/coaches/add/{coach_id}")
def add_coach(coach_id: int, name: str, section: str, subject: str, db: Session = Depends(connect_db)):
    coach = Coaches(coach_id=coach_id, name=name, section=section, subject=subject)
    db.add(coach)
    db.commit()
    db.refresh(coach)
    return {"message" : coach}


@app.get("/coaches/check/{coach_id}")
def check_coach(coach_id: int, db: Session = Depends(connect_db)):
    coach = db.query(Coaches).filter(Coaches.coach_id == coach_id).first()
    if coach:
        return coach
    return {"error": "Coach not found"}

@app.get("/coaches/all")
def get_all_coaches(db: Session = Depends(connect_db)):
    return db.query(Coaches).all()


@app.put("/coaches/update/{coach_id}")
def update_coach(coach_id: int, name: str, section: str, subject: str, db: Session = Depends(connect_db)):
    coach = db.query(Coaches).filter(Coaches.coach_id == coach_id).first()
    if coach:
        coach.name = name
        coach.section = section
        coach.subject = subject
        db.commit()
        db.refresh(coach)
        return coach
    return {"error": "Coach not found"}

@app.delete("/coaches/delete/{coach_id}")
def delete_coach(coach_id: int, db: Session = Depends(connect_db)):
    coach = db.query(Coaches).filter(Coaches.coach_id == coach_id).first()
    if coach:
        db.delete(coach)
        db.commit()
        return {"message": "Coach data is deleted"}
    return {"error": "Coach not found"}