# ✨ AI Scrapbook Backend

A Django REST API that accepts an uploaded image and a requested aesthetic, then returns a caption and (eventually) a transformed version of the image.

## 🚀 Live App

Backend API: [https://ai-scrapbook-backend-a3be7e5c44b0.herokuapp.com/api/scrapbook/](https://ai-scrapbook-backend-a3be7e5c44b0.herokuapp.com/api/scrapbook/)

## 🛠 Features

- Upload original image (`original_image`)
- Select desired aesthetic (`aesthetic`)
- Get back:
  - AI-generated caption
  - Placeholder for edited image (same as original for now)
- DRF UI available for easy testing

## 📆 Tech Stack

- Python 3.13
- Django 5.2
- Django REST Framework
- Gunicorn + WhiteNoise
- Heroku (with Neon PostgreSQL)
- psycopg2-binary (PostgreSQL adapter for Django)
- `python-decouple` for environment config

## 🧪 Local Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/ai_scrapbook_backend.git
   cd ai_scrapbook_backend/backend
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file:
   ```env
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

5. Run migrations:
   ```bash
   python3 manage.py migrate
   ```

6. Start the server:
   ```bash
   python3 manage.py runserver
   ```

## 🧳 Environment Variables

| Variable      | Purpose                       |
|---------------|-------------------------------|
| `SECRET_KEY`  | Django secret key             |
| `DEBUG`       | Toggle debug mode (True/False)|
| `DATABASE_URL`| Postgres URL (Heroku only)    |

## 🚪 Deployment to Heroku

This app is deployed to Heroku using the following steps:

1. Set up Heroku app and Postgres DB (Neon):
   ```bash
   heroku create ai-scrapbook-backend
   heroku config:set SECRET_KEY='your-key'
   heroku config:set DEBUG=False
   heroku config:set DATABASE_URL='your-neon-postgres-url'
   ```

2. Add required build settings:
   - `gunicorn` for production server
   - `whitenoise` for static file handling
   - `.slugignore` to exclude files like `README.md` from deploy

3. Add Postgres driver:
   ```bash
   pip install psycopg2-binary
   pip freeze > requirements.txt
   ```

4. Push to Heroku:
   ```bash
   git push heroku main
   heroku run python3 manage.py migrate
   ```

5. Done! The app is live at your Heroku URL.

## 📅 Future Plans

- Add real AI image processing
- Build a React frontend

---

## 👨‍💻 Author

Built by [Joseph Keane](https://github.com/itjosephk2)

