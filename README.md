# ArtistAPI

The ArtistAPI is a Django REST Framework project that allows users to perform CRUD operations on Artist and their Works.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need Python 3.7+ to run ArtistAPI. You can install it from [here](https://www.python.org/downloads/).

### Installation

```bash
git clone https://github.com/username/artistapi.git
cd artistapi
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```
### Optional (admin already exists)
```bash
python manage.py createsuperuser
```

### Run
```bash
python manage.py runserver
```
*This will run the server at localhost (127.0.0.1:8000)*
## Usage

You can use any HTTP client like curl, httpie or Postman to interact with the API.

Read [USAGE](USAGE.md) for available endpoints



