# Text & Students API

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import re

app = FastAPI()

# ----------------------
# Student API
# ----------------------
class Student(BaseModel):
    name: str
    dob: str
    country: str
    city: str
    skills: list[str]
    bio: str

students: list[Student] = []

@app.post("/api/students/")
def add_student(student: Student):
    students.append(student)
    return students

@app.get("/api/students/")
def get_students():
    return students

# ----------------------
# WebPage 
# ----------------------
# Static Files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Templates (FastAPI uses Jinja2)
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    techs = {
        "Front end": ["HTML", "CSS"],
        "Back end": ["Python", "FastAPI"]
    }
    name = "Text & Student API"
    
    # Get message from URL query params (for Add Student section)
    message = request.query_params.get("message", "")
    
    
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request, 
            "techs": techs, 
            "name": name, 
            "title": "Home",
            "message": message
        },
    )

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    name = "Text & Student API"
    return templates.TemplateResponse(
        "about.html",
        {
            "request": request,
            "name": name,
            "title": "About Us"
            }
    )

@app.get("/result", response_class=HTMLResponse)
def result(request: Request):
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request
            }
    )

# ----------------------
# Text Analyzer
# ----------------------
@app.get("/post", response_class=HTMLResponse)
def post_get(request: Request):
    name = "Text Analyzer"
    return templates.TemplateResponse(
        "post.html",
        {
            "request": request,
            "name": name,
            "title": name
            }
    )

@app.post("/post", response_class=HTMLResponse)
def post_post(request: Request, content: str = Form(...)):
    # Analyze text
    char_count = len(content)
    word_count = len(content.split())
    sentence_count = content.count(".") + content.count("!") + content.count("?")
    
    # Most frequent word
    def clean_text(txt: str) -> str:
        return re.sub(r"[^a-zA-Z\s]", "", txt)

    def most_frequent_words(clean_txt: str, n: int = 1) -> list[tuple[int, str]]:
        words_count = {}
        words = re.findall(r"\b\w+\b", clean_txt.lower())
        
        for word in words:
            words_count[word] = words_count.get(word, 0) + 1
        
        return sorted([(count, word) for word, count in words_count.items()], reverse=True)[:n]
    
    clean_content= clean_text(content)
    top_words = most_frequent_words(clean_content)
    
    most_frequent = top_words[0][1] if top_words else ""
    freq = top_words[0][0] if top_words else 0
    
    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "content": content,
            "char_count": char_count,
            "word_count": word_count,
            "sentence_count": sentence_count,
            "most_frequent": most_frequent,
            "freq": freq,
            "title": "Analysis Result",
            }
    )

# ----------------------
# Add Student Form
# ----------------------
@app.get("/students", response_class=HTMLResponse)
def show_add_student_form(request: Request):
    return templates.TemplateResponse(
        "add_student.html",
        {
            "request": request,
            "title": "Add Student"
            }
    )

@app.post("/students/add")
def add_student_form(
    request: Request,
    name: str = Form(...), # Using "..." indicates it is mandatory
    dob: str = Form(""),
    country: str = Form(""),
    city: str = Form(""),
    skills: str = Form(""),
    bio: str = Form("")
):
    
    # Parse skills
    skill_list = [s.strip() for s in skills.split(",") if s.strip()]
    
    # Create student
    student = Student(
        name=name,
        dob=dob,
        country=country,
        city=city,
        skills=skill_list,
        bio=bio
    )
    students.append(student)
    
    # Redirect to home page with success message
    return RedirectResponse(
        url="/?message=" + f"🎉+Success!+{name}+has+been+added.".replace(" ", "+"),
        status_code=303  # 303 = Redirect after POST
    )