# 🛒 Mykart – Django E-Commerce Web Application

Mykart is a fully functional e-commerce web application built using Django.  
It allows users to browse products, add items to cart, checkout, and track orders.

---

## 🚀 Features

- 🛍 Product listing with categories
- 🛒 Add to cart (LocalStorage based cart system)
- 💳 Checkout system
- 📦 Order tracking system
- 📨 Contact form
- 🗂 Admin panel for managing products & orders
- 💰 Automatic total price calculation

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

mykart/
│
├── mykart/ # Main project settings
├── shop/ # Main e-commerce app
│ ├── models.py
│ ├── views.py
│ ├── templates/
│ ├── static/
│
├── manage.py
└── db.sqlite3


---

## ⚙ Installation Guide

### 1️⃣ Clone the repository

git clone https://github.com/vishalchaudhary76/mykart.git
cd mykart


2️⃣ Create virtual environment
python -m venv env
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows


3️⃣ Install dependencies
pip install django


4️⃣ Run migrations
python manage.py migrate



5️⃣ Run the server
python manage.py runserver

Open:

http://127.0.0.1:8000/
🔑 Admin Panel Access

Create superuser:

python manage.py createsuperuser

Access admin:

http://127.0.0.1:8000/admin/


<img width="397" height="322" alt="Screenshot 2026-02-24 at 5 52 16 PM" src="https://github.com/user-attachments/assets/e501e164-6133-4126-bb74-f0907d0824c2" />
<img width="1470" height="956" alt="Screenshot 2026-02-24 at 5 51 53 PM" src="https://github.com/user-attachments/assets/ab173e82-aee4-4568-a713-e265791c6405" />
