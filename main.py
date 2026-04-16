from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import  JSONResponse
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Literal, List
import json


app = FastAPI()

class Student(BaseModel):
    id : Annotated[int, Field(..., description= ' Id of the student', examples= [1, 4, 5])]
    name : Annotated[str, Field(..., description= ' Name of the student')]
    email : Annotated[EmailStr, Field(..., description= ' email Of the student')]  
    age : Annotated[int, Field(...,gt =0, lt=120, description= 'Age of the student')]
    department : Annotated[Literal['CSE', 'EEE', 'BBA' ], Field(..., description= ' Department of the student')]
    cgpa : Annotated[float, Field(..., gt = 0.0, lt =4.1, description= ' Cgpa of the student')] 
    courses : Annotated[List[str], Field(...,min_items =1, description= ' Couses taken by the student')] 

def load_data():
    with open('students.json', 'r') as j:
        data = json.load(j)

    return data

def save_data(data):
    with open('students.json', 'w') as f:
        json.dump(data, f)


@app.get("/")
def hello():
    return {'message' : 'Student Management System API'}

@app.get('/about')
def about():
    return{
        'message': "A fully functional api for student management"
    }

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/student/{student_id}')
def view_student(
    student_id: int = Path(..., description="Id of the student", example=1)
    ):
    #load the whole student data
    data = load_data()
    for student in data:
        if student['id'] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.get('/sort')
def sort_students(
    sort_by: str = Query(..., description='sort on the basis of id & cgpa'),
    order: str = Query('asc', description='sort in acs or desc order')
    ):
    valid_fields = ['id', 'cgpa']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail= f'Invalid field, Select from {valid_fields}')
    if order not in ['asc', "desc"]:
        raise HTTPException(status_code=400, detail= f'Invalid field, Select between asc and desc')
    
    data = load_data()
    
    reverse = True if order == 'desc' else False
    sorted_data = sorted(data, key=lambda x: x[sort_by], reverse=reverse)

    return sorted_data


@app.post('/create')
def create_student(student : Student):
    #load existing data
    data = load_data()
    # check if the student already exists
    for s in data:
        if s['id'] == student.id:
            raise HTTPException(status_code=400, detail="Student already exists")
    #add new students to database
    new_student = student.model_dump()
    data.append(new_student)
    #save to database
    save_data(data)

    return JSONResponse(status_code=201, content = {
        "message": "Student added successfully"
    })