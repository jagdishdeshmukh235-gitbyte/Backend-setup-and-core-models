Project Title :Task Management System

Overview:-
The Task Management System is a backend-based project developed using Django REST Framework.
It allows users to create, read, update, and delete (CRUD) tasks easily.
This system helps users manage their daily tasks by tracking their status, title, description, and deadlines.
The project also provides REST APIs for task operations and can be tested using Thunder Client.

Features:-
✔ Create Tasks
Add new tasks with title, description, and status.

✔ View Tasks
Fetch all tasks or a single task using API.

✔ Update Tasks
Edit existing task details.

✔ Delete Tasks
Remove tasks when no longer needed.

✔ Track Task Status
Mark tasks as pending or completed.

✔ REST API Support
Uses JSON format for sending and receiving data.

✔ SQLite Database
Light and secure database for storing all tasks.

✔ API Testing Using Thunder Client
Easy to use and quick response testing inside VS Code.

Technologies Used:-
Component:	          Technology:
Backend Framework	  Django
API Framework	          Django REST Framework
Database	          SQLite
Testing Tool	          Thunder Client
Language	          Python
Editor	                  VS Code

Installation & Setup:-
Follow these steps to run the project locally:

1. Clone the Project
git clone <your_repo_link>
cd task_management_system

2. Create Virtual Environment
python -m venv venv

3. Activate Virtual Environment
Windows: venv\Scripts\activate

4. Install Dependencies
pip install -r requirements.txt

5. Run Migrations
python manage.py migrate

6. Start the Server
python manage.py runserver

API Endpoints:-
1. Create Task
POST /tasks/

Send JSON:
{
  "title": "Complete Assignment",
  "description": "Finish Django project",
  "status": "pending"
}

2. Get All Tasks
GET /tasks/

3. Get Single Task
GET /tasks/<id>/

4. Update Task
PUT /tasks/<id>/
PATCH /tasks/<id>/

5. Delete Task
DELETE /tasks/<id>/

Project Structure:-
virtual-setup/
│
├── core/
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│
├── taskmanger/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── venv/
│   ├── Include/
│   ├── Lib/
│   ├── pyvenv.cfg
│
├── db.sqlite3
├── manage.py


Advantages:-
Simple and lightweight backend system
User-friendly APIs
Clear task tracking
Fast and secure database
Easy to test and maintain

Future Scope:-
Add frontend UI
User authentication
Add deadline notifications
Task categories & priorities
Cloud database support

Conclusion:-
The Task Management System is a simple yet powerful backend project that helps users manage their daily tasks efficiently.
It provides all essential CRUD functionalities, REST API support, and easy testing through Thunder Client.
This project is a perfect learning example for understanding backend development, API creation, and database handling in Django.

