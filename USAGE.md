# API Usage

## Register a new user

POST `api/register/`

Required Fields: `username`, `password`

Example: 

curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}' http://localhost:8000/api/register/

## get token

POST api/token
Required Fields: `username`, `password`

Example: 

curl -X POST -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}' http://localhost:8000/api/register/

curl --location --request POST 'http://localhost:8000/api/token/'
--header 'Content-Type: application/json'
--data-raw '{
  "username": "user1",
  "password": "password1"
}'