## Getting Started

To run the project locally, follow these steps:

### Prerequisites

Make sure you have the following installed on your system:

- Python (3.x recommended)
- Django
- MySQL

### Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/art-gallery-management.git

2. Navigate to the project directory

3. Install project dependencies

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

