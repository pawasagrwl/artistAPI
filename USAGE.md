# API Usage

## Register a new user

POST `api/register/`

Required Fields: `name`, `username`, `password`

Example:

```bash
curl --location 'http://localhost:8000/api/register/' --header 'Content-Type: application/json' --data '{"name":"Artist2", "username":"user2", "password":"artpass321"}'
```

*Note: This will create a new artist with the provided name*

## Login & get token

POST `api/login/`

Required Fields: `username`, `password`

Example:

```bash
curl --location 'http://localhost:8000/api/login/' --header 'Content-Type: application/json' --data '{"username":"user1", "password":"artpass321"}'
```

## Get Artists

### All Artists

GET `api/artists/`

Required Auth: `Token`

Example:

```bash
curl --location 'http://localhost:8000/api/artists/' --header 'Authorization: Token d1cb28a74bf18075da4eaca6143737d2d579ddaa'
```

### Artist by name

GET `api/artists/artist=[ArtistName]`

Required Auth: `Token`

Example:

```bash
curl --location 'http://localhost:8000/api/artists/?artist=Artist3' --header 'Authorization: Token d1cb28a74bf18075da4eaca6143737d2d579ddaa'
```

## Create Work

POST `api/works/`

Required Fields: `link`, `work_type`

Example:

```bash
curl --location 'http://localhost:8000/api/works/' --header 'Content-Type: application/json' --header 'Authorization: Token d1cb28a74bf18075da4eaca6143737d2d579ddaa' --data '{"link":"https://www.youtube.com", "work_type":"YT"}'
```

## Get Works
### All Works

GET `api/works/`

Required Auth: `Token`

Example:

```bash
curl --location 'http://localhost:8000/api/works/' --header 'Authorization: Token d1cb28a74bf18075da4eaca6143737d2d579ddaa'
```

### Work by work_type

GET `api/works/work_type=[YT/IG/OT]`

Required Auth: `Token`

Example:

```bash
curl --location 'http://localhost:8000/api/works/?work_type=YT' --header 'Authorization: Token d1cb28a74bf18075da4eaca6143737d2d579ddaa'
```

## Get Users (Admin Only)

GET `api/users`

Required Auth: `Token`

Example:

```bash
curl --location 'http://localhost:8000/api/users' --header 'Authorization: Token 6f02795fb5d8ccd326613762be5c96b108aef139'
```