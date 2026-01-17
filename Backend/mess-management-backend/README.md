# Mess Management System

## Overview
The Mess Management System is a web application designed to facilitate meal management for students and administrators. It allows students to view menus, book meals, track purchases, and provide feedback, while enabling administrators to manage menus, verify meal entries, and generate reports.

## Features
- **Student Features:**
  - Register and log in using college email.
  - View weekly menus with meal types (breakfast, lunch, dinner).
  - Book meals via QR codes.
  - Track meal purchases and view history.
  - Submit feedback with ratings and comments.

- **Admin Features:**
  - Manage student accounts and view feedback.
  - Create, update, and delete weekly menus and pricing.
  - Verify meal entries using QR code scanning.
  - Generate reports for billing and meal statistics.

## Tech Stack
- **Backend:** Django
- **Database:** PostgreSQL
- **Authentication:** JWT for secure login
- **Frontend:** React.js (for the client-side application)

## Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone <YOUR_GIT_URL>
   cd mess-management-backend
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   - Copy `.env.example` to `.env` and fill in the required values.

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

## Testing
To run the tests, use the following command:
```bash
python manage.py test
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.