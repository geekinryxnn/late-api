# Late Show API

A REST API for managing a late night TV show system.

## Features

- User authentication with JWT
- CRUD operations for episodes, guests, and appearances
- PostgreSQL database
- Flask RESTful architecture

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Create PostgreSQL database
4. Set environment variables in `.env` file
5. Run migrations: `flask db upgrade`
6. Seed database: `python server/seed.py`
7. Start server: `flask run`

## API Endpoints

| Route | Method | Auth Required | Description |
|-------|--------|---------------|-------------|
| `/register` | POST | No | Register a new user |
| `/login` | POST | No | Login and get JWT token |
| `/episodes` | GET | No | Get all episodes |
| `/episodes/<id>` | GET | No | Get episode details |
| `/episodes/<id>` | DELETE | Yes | Delete an episode |
| `/guests` | GET | No | Get all guests |
| `/appearances` | POST | Yes | Create a new appearance |

## Authentication

1. Register a user at `/register`
2. Login at `/login` to get a JWT token
3. Include the token in protected requests: `Authorization: Bearer <token>`

## Postman Collection

Import the provided Postman collection to test all endpoints.