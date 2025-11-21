from fastapi import FastAPI


app = FastAPI(docs_url = "/swagger")


@app.get("/test")
def welcome_kit():
    return {"message" : "Total mark is 500"}

@app.post("/marks/create{student_id}")
def all_marks(student_id):
    return {"message" : "new Student Data created"}


@app.get("/marks/{student_id}")
def student_marks(student_id):
    return {"message" : f"This end point will return marks for Student no.{student_id}"}
