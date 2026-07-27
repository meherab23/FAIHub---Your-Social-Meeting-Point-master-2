# FAIHub – Your Social Meeting Point

FAIHub is a social media platform developed using Python with the Django framework. It utilizes HTML, CSS, JavaScript, Bootstrap, AJAX, and MySQL for a seamless and interactive user experience. This project empowers users to register, create connections, and share content within a vibrant online community.It is a social media platform designed to connect users with each other in a dynamic and interactive online environment. This project provides a range of features that allow users to create profiles, share content, connect with friends, and engage in meaningful interactions.

## Features

### 1. User Authentication

- **Signup and Login:** Users can securely sign up and log in using their email and password.

### 2. Profile Customization

- **Customize Profile:** Users can personalize their profiles by adding details such as bio, location, etc.
- **Profile and Cover Photos:** Upload and set profile pictures and cover photos.

### 3. Social Connectivity

- **Follow and Followers:** Establish connections by following other users and building a network of followers.

### 4. Content Sharing

- **Upload Posts and Pictures:** Share thoughts, experiences, and images with followers through posts.
- **Love and Comment:** Interact with others by expressing love for posts and leaving comments.

### 5. Messaging

- **Direct Messaging:** Users can send private messages, enabling one-on-one communication.

### 6. Unique User Identification

- **Unique Usernames:** Ensure individuality and easy searchability with unique usernames.

## Getting Started

To set up FAIHub on your local machine using XAMPP and MySQL, follow these steps:


   
Setup Database:
Create a MySQL database in XAMPP named "FAIHub."

Open settings.py in your Django project and update the DATABASES configuration:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'FAIHub',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Run Migrations:
python manage.py makemigrations
python manage.py migrate


Create Superuser:
python manage.py createsuperuser

Run the Application:
python manage.py runserver

Access the Platform:
Open your web browser and navigate to http://localhost:8000 to access FAIHub.


Contact
If you have any questions or suggestions, feel free to reach out to us at [rayanchowdhury07@gmail.com].

Happy connecting on FAIHub! 🚀

