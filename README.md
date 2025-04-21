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

## 📅 Future Plans

- Add real AI image processing
- Store media in Cloudinary or S3
- Build a React frontend
- Add user authentication for saved scrapbooks

---

## 👨‍💻 Author

Built by [Joseph Keane](https://github.com/itjosephk2)