# 🩸 Bondhon — Blood Bank Backend

A RESTful API backend for the **Bondhon Blood Bank** platform — connecting blood donors with those in need. Built with Django REST Framework and deployed on Vercel.

[![Live API](https://img.shields.io/badge/Live%20API-bloodbank--teal.vercel.app-red?style=flat-square&logo=vercel)](https://bloodbank-teal.vercel.app/api/v1/)
[![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0.2-green?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.16.1-orange?style=flat-square)](https://www.django-rest-framework.org/)

---

## 🌐 Live API

**Base URL:** `https://bloodbank-teal.vercel.app/api/v1/`

| Endpoint | Description |
|---|---|
| `GET /api/v1/` | API root — lists all available endpoints |
| `GET /api/v1/donors/` | List all registered blood donors |
| `GET /api/v1/requests/` | List all blood requests |
| `GET /api/v1/my-requests/` | List blood requests by the authenticated user |
| `GET /api/v1/dashboard/` | Dashboard statistics |

---

## ✨ Features

- **Donor Management** — Register, update, and manage blood donors with blood group, age, availability status, and last donation date
- **Blood Request System** — Submit and track blood requests
- **User Authentication** — JWT-based authentication via `djangorestframework-simplejwt` and `djoser`
- **Social Auth** — OAuth2 / Social login support via `social-auth-app-django`
- **Dashboard** — Summary statistics for the platform
- **API Documentation** — Auto-generated Swagger/OpenAPI docs via `drf-yasg`
- **Media Storage** — Cloudinary integration for media file storage
- **CORS Support** — Cross-origin requests handled via `django-cors-headers`
- **Filtering** — Query filtering via `django-filter`
- **Nested Routes** — Nested REST resource routing via `drf-nested-routers`
- **Deployed on Vercel** — Serverless Python deployment

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 6.0.2 |
| API | Django REST Framework 3.16.1 |
| Auth | JWT (SimpleJWT), Djoser, Social Auth |
| Database | PostgreSQL (via `psycopg2-binary`) |
| Media Storage | Cloudinary |
| Deployment | Vercel (Python serverless) |
| Static Files | WhiteNoise |
| API Docs | drf-yasg (Swagger/ReDoc) |
| Config | python-decouple |

---

## 📁 Project Structure

```
Bondhon-BloodBank-Backend/
├── accounts/           # User accounts and authentication
├── api/                # API root router and URL configuration
├── blood_bank/         # Django project settings (wsgi.py, settings.py)
├── blood_request/      # Blood request models, views, serializers
├── dashboard/          # Dashboard stats and analytics
├── donors/             # Donor profiles, availability, blood groups
├── staticfiles/        # Collected static files
├── manage.py
├── requirements.txt
└── vercel.json         # Vercel deployment config
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL database
- Cloudinary account (for media storage)

### 1. Clone the repository

```bash
git clone https://github.com/naim13107/Bondhon-BloodBank-Backend.git
cd Bondhon-BloodBank-Backend
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_django_secret_key
DEBUG=True

# Database
DATABASE_URL=your_postgresql_database_url

# Cloudinary
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/v1/`

---

## 📋 API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/users/` | Register a new user |
| `POST` | `/auth/jwt/create/` | Obtain JWT access & refresh tokens |
| `POST` | `/auth/jwt/refresh/` | Refresh access token |
| `GET` | `/auth/users/me/` | Get current user profile |

### Donors

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/donors/` | List all available donors |
| `POST` | `/api/v1/donors/` | Register as a donor |
| `GET` | `/api/v1/donors/{id}/` | Get donor detail |
| `PUT/PATCH` | `/api/v1/donors/{id}/` | Update donor profile |

### Blood Requests

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/requests/` | List all blood requests |
| `POST` | `/api/v1/requests/` | Create a blood request |
| `GET` | `/api/v1/my-requests/` | List my blood requests (auth required) |
| `GET` | `/api/v1/requests/{id}/` | Get request detail |

### Dashboard

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/v1/dashboard/` | Get platform statistics |

---

## 🩸 Blood Groups Supported

`A+`, `A-`, `B+`, `B-`, `AB+`, `AB-`, `O+`, `O-`

---

## ☁️ Deployment (Vercel)

This project is configured for serverless deployment on Vercel using the `@vercel/python` builder.

The `vercel.json` routes all traffic through `blood_bank/wsgi.py`:

```json
{
  "builds": [{
    "src": "blood_bank/wsgi.py",
    "use": "@vercel/python",
    "config": { "maxLambdaSize": "15mb", "runtime": "python3.11.3" }
  }],
  "routes": [{ "src": "/(.*)", "dest": "blood_bank/wsgi.py" }]
}
```

To deploy your own instance:

1. Push your code to GitHub
2. Import the repository on [Vercel](https://vercel.com)
3. Add your environment variables in the Vercel dashboard
4. Deploy 🎉

---

## 📦 Key Dependencies

```
Django==6.0.2
djangorestframework==3.16.1
djangorestframework_simplejwt==5.5.1
djoser==2.3.3
django-cors-headers==4.9.0
django-filter==25.2
cloudinary==1.44.1
psycopg2-binary==2.9.11
drf-yasg==1.21.14
drf-nested-routers==0.95.0
social-auth-app-django==5.7.0
whitenoise==6.11.0
python-decouple==3.8
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a new feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source. Feel free to use it for educational or personal purposes.

---

## 👤 Author

**Md.Naim-UL-Haque** — [@naim13107](https://github.com/naim13107)

---

> *Bondhon (বন্ধন) — meaning "bond" in Bengali — connecting lives through the gift of blood.*
