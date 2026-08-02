# Course Recommendation Agent

## Overview

This AI agent recommends a personalized learning path for students based on their background, current skills, and career goals using the Groq LLM.

## Features

- Reads student profiles from JSON
- Reads course catalogue from JSON
- Uses Groq AI to generate personalized recommendations
- Provides learning path, prerequisites, timeline, and career advice

## Requirements

- Python 3.14+
- Groq API Key

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_api_key
```

## Run

```bash
python main.py
```

## Sample Student Profiles

- Rahul
- Anjali
- Amit

## Project Structure

- main.py
- courses.json
- student_profiles.json
- requirements.txt
- README.md
- .env
- .gitignore

## Tradeoffs

- Uses a small JSON course catalogue.
- Recommendations depend on the LLM response.
- No graphical user interface.

## Future Improvements

- Add a web interface.
- Support PDF resumes and transcripts.
- Store recommendation history in a database.