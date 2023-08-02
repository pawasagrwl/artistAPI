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
python manage.py createsuperuser
python manage.py runserver
```

## Usage

You can use any HTTP client like curl, httpie or Postman to interact with the API.

### Endpoints

- Register a user: POST /api/register/
- Login a user and get token: POST /api/login/
- Create a new work: POST /api/works/
- Retrieve a list of all works: GET /api/works/
- Filter works by type: GET /api/works/?work_type=<YT/IG/OT>
- Search artists by name: GET /api/artists/?search=[ArtistName]

### Tests

```bash
python manage.py test
```



