import json
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
with open("courses.json", "r") as file:
    courses = json.load(file)

with open("student_profiles.json", "r") as file:
    students = json.load(file)
    print("\nAvailable Student Profiles:\n")

for i, student in enumerate(students, start=1):
    print(f"{i}. {student['name']}")

choice = int(input("\nSelect a student (1-3): "))

student = students[choice - 1]
prompt = f"""
You are a Course Recommendation AI Agent.

Student Details:

Name: {student['name']}
Background: {student['background']}
Current Skills: {', '.join(student['skills'])}
Career Goal: {student['goal']}

Available Courses:

{json.dumps(courses, indent=2)}

Your task:

1. Recommend an ordered learning path.
2. Explain why each course is recommended.
3. Mention prerequisites.
4. Give an estimated learning timeline.
5. End with career advice.

Return the answer in a neat, readable format.
"""
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": "You are an expert AI career advisor."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.5
)

print("\n========== COURSE RECOMMENDATION ==========\n")
print(response.choices[0].message.content)
