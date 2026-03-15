# OpenWebUI Setup and Running Guide

## Tested Environment

The system was developed and tested using the following environment:

- **Operating System:** Windows 10  
- **Python:** 3.11.0  
- **Node.js:** v22.22.1  
- **npm:** 10.9.4  
- **OpenWebUI Base Version:** 0.6.5  

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/MoneebAbuJamos/Moneeb_Abu_Jamos_OpenWebUI.git
```

Navigate to the project directory:

```bash
cd Moneeb_Abu_Jamos_OpenWebUI
```

---

## 2. Setup the Backend Environment

Navigate to the backend directory:

```bash
cd backend
```

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

---

## 3. Install Frontend Dependencies

Return to the project root directory and install Node dependencies:

```bash
npm install
```

---

## 4. Build the Frontend

Build the Svelte frontend:

```bash
npm run build
```

Copy the generated build files to the FastAPI static directory:

```powershell
Remove-Item backend\open_webui\static\* -Recurse -Force
Copy-Item -Recurse build\* backend\open_webui\static\
```

---

## 5. Run the Backend Server

Navigate to the backend directory:

```bash
cd backend
```

Start the FastAPI server:

```bash
uvicorn open_webui.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

---

# Testing Implemented Features

## License Enforcement

The system uses an **offline license file** located at:

```
backend/config/license.json
```

The license file is **digitally signed using RSA** and validated locally using a public key stored in the application.

For testing purposes, the provided license allows a maximum of **3 registered users**.

Expected behavior:

Once three users are registered in the system, any additional signup attempt will be blocked and the system will return a **license limit error**.

> Note: Editing the license file manually will invalidate the signature and the application will refuse to start.

---

## Audit Trail

Login as an **administrator** and perform actions such as:

- User login or logout  
- Creating a new user  
- Changing a user role  
- Updating a model  

Navigate to:

```
Admin Panel → Audit
```

The performed actions should appear in the **Audit Log table**.

---

# Required Files

The licensing system requires the following files to exist for the system to start successfully:

```
backend/config/license.json
backend/open_webui/licensing/public_key.pem
```

These files are required for **offline license validation**.
