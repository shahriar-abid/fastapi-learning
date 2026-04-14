# 🎓 Student Management API (FastAPI)

> 🚀 Beginner-friendly FastAPI project demonstrating core backend development concepts.

A simple REST API built with FastAPI to manage student data.
This project demonstrates core backend development concepts like routing, data handling, searching, sorting, and error handling.

---

## 🚀 Features

* 📌 Get all students
* 🔍 Get student by ID
* 🔃 Sort students (by `id` or `cgpa`)
* ⚠️ Proper error handling using HTTPException

---

## 🛠️ Tech Stack

* Python 🐍
* FastAPI ⚡
* JSON (for data storage)

---

## 📂 Project Structure

```
LearningApi/
│
├── main.py
├── students.json
├── .gitignore
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/shahriar-abid/fastapi-learning.git
cd fastapi-learning
```

2. Create virtual environment:

```
python3 -m venv myenv
source myenv/bin/activate
```

3. Install dependencies:

```
pip install fastapi uvicorn
```

4. Run the server:

```
uvicorn main:app --reload
```

---

## 📄 API Docs

Interactive API documentation available at:

```
http://127.0.0.1:8000/docs
```

---

## 📌 API Endpoints

### Home

```
GET /
```

### About

```
GET /about
```

### Get All Students

```
GET /view
```

### Get Student by ID

```
GET /student/{student_id}
```

### Sort Students

```
GET /sort?sort_by=id&order=asc
GET /sort?sort_by=cgpa&order=desc
```

---

## 🧪 Example Usage

Get student with ID 1:

```
GET /student/1
```

Sort students by CGPA descending:

```
GET /sort?sort_by=cgpa&order=desc
```

---

## ⚠️ Error Handling

* Returns proper HTTP status codes
* Examples:

```
404 → Student not found
400 → Invalid query parameters
```

---

## 💡 Future Improvements

* Add POST (create student)
* Add DELETE and UPDATE
* Connect with PostgreSQL database
* Add authentication

---

## 👨‍💻 Author

Md Al Shahriar Abid
CSE Student | BRAC University

---

## ⭐ Notes

This project is part of my learning journey in backend development and FastAPI.
