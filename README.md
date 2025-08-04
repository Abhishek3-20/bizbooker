# 📘 BizBooker

BizBooker is a modern, mobile friendly Django booking platform tailored for small businesses and service providers. It allows customers to schedule appointments, view services, and manage bookings through an intuitive interface all with a responsive, professional UI built using "Tailwind CSS" and "DaisyUI".

🌐 Live Site: [https://bizbooker.pythonanywhere.com]

---

# 🚀 Features

- 🔒 **User Authentication**
  - Login / Register for Customers
  - Business Dashboard for Owners

- 📅 **Booking System**
  - Service selection with dynamic dropdown
  - Custom time slot selection
  - Booking history & manual booking

- 🛠️ **Service Management**
  - Add/Edit/Delete services (admin interface)
  - Assign durations and prices

- 📬 **Notifications**
  - Email confirmations (configurable)
  - In-app instructions and alerts

- 🎨 **Modern UI**
  - Responsive mobile-first design
  - Tailwind CSS + DaisyUI for clean, premium visuals
  - Dark mode toggle and QR check-in options

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x
- **Frontend:** Tailwind CSS 3.8 + DaisyUI
- **Database:** SQLite (local) / PythonAnywhere (remote)
- **Hosting:** [PythonAnywhere](https://www.pythonanywhere.com/)
- **Other:** django-widget-tweaks, django-browser-reload

<img width="1366" height="658" alt="home page" src="https://github.com/user-attachments/assets/eb68b615-4aca-438a-ae0e-a6f3f924792c" />

<img width="1366" height="654" alt="signup page" src="https://github.com/user-attachments/assets/8e5622a9-59f9-49ec-8c2d-2f36846fddc7" />

<img width="1363" height="655" alt="booking page" src="https://github.com/user-attachments/assets/d919f1ba-08eb-4315-aa07-7f8d64c0510c" />

<img width="1366" height="641" alt="dashboard page" src="https://github.com/user-attachments/assets/3f329b63-6e19-4add-a724-383c51fb0bf6" />



# 🧑‍💻 Local Development Setup

1. Clone the repository
      git clone https://github.com/Abhishek3-20/bizbooker.git
      cd bizbooker
2. Create and activate a virtual environment

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies

      pip install -r requirements.txt
4. Run migrations

      python manage.py makemigrations
      python manage.py migrate
5. Create superuser (optional for admin access)

      python manage.py createsuperuser
6. Collect static files

      python manage.py collectstatic
   
8. Run the development server

      python manage.py runserver

📝 License
This project is licensed under the MIT License.

👨‍💻 Author
Abhishek Unni
🌐 Portfolio: https://abhishek3-20.github.io
📧 Contact
  email : abhishekunni2003@gmail.com
