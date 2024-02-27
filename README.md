## Getting Started

To run the project locally, follow these steps:

### Prerequisites

Make sure you have the following installed on your system:

- Python (3.7 recommended)
- Django
- MySQL

### Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/art-gallery-management.git

2. Navigate to the project directory.

   ```bash
   cd art-gallery-management


### Configuration 

1. Configure the MySQL database settings in settings.py file located in art_gallery directory.

   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

### Running the Server

1. Apply database migrations.

   ```bash
   python manage.py migrate

3. Start the Django development server.

   ```bash
   python manage.py runserver
   
5. Access the web application in your browser at http://127.0.01:8000/.

### Usage 
* Upon accessing the web application, you can navigate through different sections such as art pieces, artists, and art shows.
* Use the provided interface to add, edit, or delete records as needed.
* Utilize the search and filter functionalities to efficiently query and retrieve information.



