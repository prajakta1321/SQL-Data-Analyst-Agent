# SQL-Data-Analyst-Agent

A simple AI-powered (rule-based) SQL agent that converts natural language questions into SQL queries and executes them on a real SQLite database using a clean Streamlit UI.

# Project Overview

1. This Agent allows users to:

2. Ask questions about data in plain English

3. Automatically generate SQL queries

4. Execute queries on a real database

5. View results instantly in a web interface

The project is designed with a modular architecture, making it easy to replace the rule-based SQL generator with an LLM in the future.

STEPS TO RUN In VSCODE :


# Create virtual environment:

```
python -m venv venv
```

# Activate it:

```
venv\Scripts\activate
```

# How to Run the Project

Step 1: Ensure database exists

If not already created:

```
python db/db_setup.py
```

Step 2: Run the Streamlit app

```
streamlit run app.py
```

Step 3: Open browser

Streamlit will automatically open:

http://localhost:8501


# Result :

# Streamlit UI :

<img width="1920" height="924" alt="image" src="https://github.com/user-attachments/assets/27dcb918-f755-41ff-ad06-f442c3d29ac8" />


# QUERY EXECUTION :

count customers :

<img width="1920" height="924" alt="image" src="https://github.com/user-attachments/assets/b07b72d9-2fe9-4054-b378-c7c1a8b83019" />

show all products :


<img width="1920" height="924" alt="image" src="https://github.com/user-attachments/assets/025e02b6-0bc4-4703-99c3-3b7196890cd3" />










