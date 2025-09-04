# 30 Days of Python - Day 29: Building a RESTful API with Flask and MongoDB (Local Setup)

This project is part of the **30 Days of Python** challenge, specifically **Day 29**, where we build a RESTful API using **Python, Flask, and MongoDB**. The goal is to implement a fully functional backend API that supports CRUD operations (Create, Read, Update, Delete) for managing student records.

---

## 🚀 Overview

In this project, we create a simple but complete REST API to manage student data for the *30DaysOfPython* program. The API allows clients to:

- Retrieve all students
- Retrieve a single student by ID
- Create a new studentv
- Update an existing student
- Delete a student

All of this is done **entirely on your local machine**, without requiring any external hosting platforms like Heroku, Render, or Vercel.

---

## 🔐 Why Not Use Heroku or Similar Platforms?

While deploying the API online would make it publicly accessible, this version intentionally avoids using services like:

- **Heroku**
- **Render**
- **Vercel**
- **Railway**
- **Fly.io**

### ✅ Reasons:

1. **No Account Required**  
   You don't need to sign up or log in anywhere. This keeps your workflow private and reduces dependency on third-party services.

2. **No Credit Card or Identity Verification**  
   Some platforms require credit card details even for free tiers — we avoid that completely.

3. **Faster Learning & Immediate Feedback**  
   Running everything locally means you can code, test, and debug instantly without waiting for deployment cycles.

4. **Full Control Over Your Environment**  
   You control your database and server. No risk of data exposure or unexpected shutdowns due to platform policies.

5. **Perfect for Learning Purposes**  
   Since the goal is to learn how APIs work — not production deployment — a local setup is sufficient and recommended.

6. **Avoid Free Tier Limitations**  
   Many cloud platforms sleep or throttle free apps after inactivity, which disrupts testing.

> 📌 **Bottom line**: This is a **learning-first** implementation. We prioritize understanding over public deployment.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|----------|--------|
| **Python** | Backend programming language |
| **Flask** | Lightweight web framework for building APIs |
| **MongoDB** | NoSQL database to store student data |
| **Postman / Insomnia** | Tools to test API endpoints (GET, POST, PUT, DELETE) |
| **BSON/JSON** | Data interchange format for API responses |

---

## 📦 Prerequisites

Before running the project, ensure you have the following installed:

1. **Python 3.6+**  
   Check with: `python --version`

2. **Flask & PyMongo**  
   Install via pip:
   ```bash
   pip install flask pymongo dnspython