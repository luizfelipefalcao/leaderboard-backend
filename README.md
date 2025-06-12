# Leaderboard Backend API

This is a simple CRUD backend API for user management using FastAPI and MongoDB Atlas.

## Features
- Create, read, update, and delete users
- User fields: name, age, address, points (0-50)

## Setup

1. **Clone the repository**

2. **Create a virtual environment and activate it**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory with:
   ```env
   MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<database>?retryWrites=true&w=majority&appName=<appName>
   ```

5. **Run the FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **API Endpoints:**
   - `GET /users` — List all users
   - `POST /users` — Create a new user
   - `GET /users/{user_id}` — Get a user by ID
   - `PUT /users/{user_id}` — Update a user
   - `DELETE /users/{user_id}` — Delete a user

## Notes
- The backend will run locally by default. You can deploy it to Heroku when ready.
- Make sure your MongoDB Atlas cluster is accessible from your IP. 