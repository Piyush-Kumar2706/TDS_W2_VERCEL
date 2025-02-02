from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"]
)

# Load student data from the JSON file
with open("q-vercel-python.json", "r") as file:
    student_data = json.load(file)

# Convert list to dictionary for quick lookup
student_dict = {student["name"]: student["marks"] for student in student_data}

@app.get("/api")
def get_marks(name: list[str]):
    marks = [student_dict.get(n, "Not Found") for n in name]
    return {"marks": marks}
