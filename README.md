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


<img width="1470" height="956" alt="Screenshot 2026-02-25 at 1 38 03 PM" src="https://github.com/user-attachments/assets/9eddfa24-9512-4c41-ac3a-91ad97a3b598" />
<img width="1470" height="956" alt="Screenshot 2026-02-25 at 1 33 34 PM" src="https://github.com/user-attachments/assets/dc63927a-b122-4aa8-bd7f-d256f43180d1" />
<img width="1470" height="956" alt="Screenshot 2026-02-25 at 1 27 58 PM" src="https://github.com/user-attachments/assets/919675d4-3eb6-4cbb-990f-ddc90fd921de" />
<img width="1470" height="956" alt="Screenshot 2026-02-25 at 1 27 52 PM" src="https://github.com/user-attachments/assets/3abde1f5-89c0-4f8e-9975-fe42744de3bb" />
<img width="1470" height="956" alt="Screenshot 2026-02-25 at 1 27 39 PM" src="https://github.com/user-attachments/assets/8ccf1eb2-ec2a-4639-8f9b-5e9be067f51e" />

