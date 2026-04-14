from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('students.json', 'r') as j:
        data = json.load(j)

    return data


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