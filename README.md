# Secure Hotel Booking System

## Project Description

The Secure Booking System is a web-based application developed as part of the Secure Software Development course.

## Features

### User Features
- User Registration
- User Login
- View Available Rooms
- Create Booking
- Cancel Booking
- User Profile Management
- Booking History

### Administrator Features
- Manage Users
- Manage Hotel Rooms
- Manage Bookings
- View Audit Logs
- Monitor Login Activities

## Security Features

The system implements several security controls:

### Input Validation
- Server-side validation
- Client-side validation
- Input sanitization
- Regex validation

### Authentication & Session Security
- Password hashing using bcrypt
- Secure login authentication
- Session timeout
- CSRF protection
- Secure cookies (HttpOnly and Secure)

### Access Control
- Role-Based Access Control (RBAC)
- Admin and User roles
- Prevention of Insecure Direct Object References (IDOR)

### Sensitive Data Protection
- Passwords stored as hashed values
- HTTPS communication
- Sensitive information excluded from logs

### Error Handling
- Custom error pages (400, 403, 404, 500)
- No sensitive system information exposed

### Logging & Monitoring
- Login activity logging
- Failed login monitoring
- Booking activity logging
- Administrative activity logging

### Output Encoding
- HTML escaping
- Cross-Site Scripting (XSS) prevention

## Technology Stack

### Frontend:
- HTML
- CSS
- Bootstrap
- JavaScript

### Backend:
- Python Flask

### Database:
- SQLite

### Security Libraries:
- Flask-WTF
- Flask-Login
- bcrypt

## Installation Steps

### 1. Clone Repository

Clone the project repository from GitHub:

```bash
git clone https://github.com/arifshafira/secure-booking-system.git

```
### 2. Navigate to Project Folder

Move into the project directory:
```bash
cd secure_booking
```
### 3. Create Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```
### 4. Activate Virtual Environment

Windows
```bash
.venv\Scripts\activate
```
Linux/Mac
```bash
source .venv/bin/activate
```
### 5. Install Dependencies

Install all required packages:
```bash
pip install -r requirements.txt
```
### 6. Configure Environment Variables

Create a .env file based on the project configuration.

Example:
```bash
SECRET_KEY=your-secret-key

DEBUG=True
```
### 7. Run Application

Start the Django development server:
```bash
python manage.py runserver
```
The application will be available at:
```bash
http://127.0.0.1:8000
