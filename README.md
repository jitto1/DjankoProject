# DjankoProject
Sample Djanko Project
# Django Survey Tool

A web-based survey application built using the Django framework. Users can create surveys, add questions, and collect responses from participants. The application also provides a dashboard to view the collected data.

---

## Features

- User Authentication (Login/Logout)
- Create, View, and Manage Surveys
- Add and Manage Questions for Surveys
- Collect Responses from Participants
- View Survey Results
- Responsive UI using Bootstrap

---

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (Bootstrap for UI)
- **Database**: SQLite (default, can be replaced with PostgreSQL or MySQL)

---

## Requirements

- Python 3.10+
- Django 5.1+
- Bootstrap (via CDN)

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/django-survey-tool.git
cd django-survey-tool
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv survey_env
source survey_env/bin/activate  # On Windows: survey_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin user.

### 6. Run the Development Server
```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000/`.

---

## Usage

1. **Log In**:
   - Use the superuser account created earlier or register a new user.

2. **Create Surveys**:
   - From the dashboard, create a new survey by providing a title and description.

3. **Add Questions**:
   - Add questions to the created surveys.

4. **Collect Responses**:
   - Share the survey with participants, and they can respond to the questions.

5. **View Results**:
   - View collected responses in the survey results section.

---

## Project Structure

```
.
├── app/                # Main application directory
│   ├── templates/app/  # HTML templates
│   ├── models.py       # Database models
│   ├── views.py        # Views (controllers)
│   ├── urls.py         # URL routes
├── survey_tool/        # Project settings
├── db.sqlite3          # SQLite database (default)
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

---
## Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
