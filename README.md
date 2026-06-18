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
- Python (Django)

### Backend:
- Python Django

### Database:
- SQLite

### Security Libraries:
- Django-WTF
- Django-Login
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
```
Project Structure
```bash
Secure-Booking-System
│
├── secure_booking
|    ├── docs/
|    ├── tests/
|    ├── static/
|    ├── templates/
|    └── secure_booking/
│    
├── .gitignore
├── bandit_report.txt
├── manage.py
├── requirements.txt
└── README.md

```
## Screenshots
### Login Page

<img width="1600" height="841" alt="WhatsApp Image 2026-06-17 at 3 49 28 PM" src="https://github.com/user-attachments/assets/e40bbb36-38f1-4861-b916-dd84dd29492f" />


### Registration Page

<img width="1600" height="685" alt="WhatsApp Image 2026-06-18 at 12 10 30 PM" src="https://github.com/user-attachments/assets/853daa7a-6e32-49bc-8d5f-bf08468570d9" />


### Room Booking Page

<img width="1600" height="693" alt="WhatsApp Image 2026-06-18 at 12 13 14 PM" src="https://github.com/user-attachments/assets/517bba88-7ec6-4697-acfb-de5df292bcd3" />
<img width="1600" height="690" alt="WhatsApp Image 2026-06-18 at 12 17 11 PM" src="https://github.com/user-attachments/assets/7cd983d4-d204-46c0-af18-2548d898a2ca" />


### User Profile Page

<img width="1600" height="684" alt="WhatsApp Image 2026-06-18 at 12 15 07 PM" src="https://github.com/user-attachments/assets/127be729-8156-4ea4-b594-d2aad2b7ba8e" />

<img width="1600" height="686" alt="WhatsApp Image 2026-06-18 at 12 13 57 PM" src="https://github.com/user-attachments/assets/cc616188-1e0c-4370-95de-39a422577d6d" />


### Admin Dashboard

<img width="1600" height="841" alt="WhatsApp Image 2026-06-17 at 3 51 29 PM" src="https://github.com/user-attachments/assets/d5a4d10a-d788-4608-ac31-d383c1e4ae46" />

### Admin Manage Room
<img width="1805" height="953" alt="image" src="https://github.com/user-attachments/assets/3a04926f-d2fd-41be-87ec-769a00af4923" />
<img width="1823" height="768" alt="image" src="https://github.com/user-attachments/assets/d5141ae4-b48e-4ebf-8120-e94dce0ba4f9" />


### Audit Log Page

<img width="1600" height="693" alt="WhatsApp Image 2026-06-18 at 12 19 19 PM" src="https://github.com/user-attachments/assets/1da7c2f2-e5e7-4590-988f-6531ae1b9334" />


## Security Testing

### Tools Used:
- Burp Suite
- Bandit 

### Testing Conducted:
- SQL Injection Testing
- Cross-Site Scripting (XSS) Testing
- Authentication Testing
- Access Control Testing
- Fuzz Testing
- Input Validation Testing


## Team Members

| **Name**	| **Role** |
| :--- | :---: | 
| Muhammad Irman Haqiemy Bin Syafrizal	| Developer & Project Leader|
| Muhammad Arif Shafira Bin Shahrin Amri | GitHub Handler |
| Muhammad Haris Haikal Bin Muhd Hata	| Security Checker |


## GitHub Repository

### Repository Name:

Secure-Booking-System

### Version:
```bash
v1.0.0 Initial Secure Release

```
### License:

This project is developed for educational purposes under the Secure Software Development course.
