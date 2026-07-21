# login

**POST** `{{url}}/api/auth/`

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{
    "email": "devs@aerogon.aero",
    "password": "devs@2026",
    "user_type": "asl"
}
```

## Examples

### login

**Request:** `POST` `{{url}}/api/auth/`

```json
{
    "email": "admin@gmail.com",
    "password": "admin",
    "user_type": "asl"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Login Successful",
    "data": {
        "result": {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTkzMzc0OCwiaWF0IjoxNzMxOTA0OTQ4LCJqdGkiOiJkNDdhYWRjMGViODE0ZWFmYTQyMDRiYzdkMzkxMDgyNSIsInVzZXJfaWQiOjN9.A7T7gtw_F54qVJldzwO8ertFEEFmsHH5dbUjln1xehk",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxOTMzNzQ4LCJpYXQiOjE3MzE5MDQ5NDgsImp0aSI6IjU2MGE1NDNiZWQwNjRjMjRhYzM2MzRlNDI0YzI2ZTJhIiwidXNlcl9pZCI6M30.lI17kvTBfCKZ4RCUtAokbcMLAHdcxcRKqTv7A8mFmZg",
            "id": 3,
            "username": "admin",
            "first_name": "Admin",
            "last_name": "admin",
            "email": "admin@gmail.com",
            "phone": "+8801684806728",
            "user_type": "asl",
            "profile_image": "http://localhost:5011/api/media/images/profile_images/2024/09/britian.png",
            "default_currency": {
                "id": 1,
                "prefix": "$",
                "short_key": "BDT",
                "current_rate": 1,
                "default": true,
                "name": "TAKA",
                "flag": "http://localhost:5011/api/media/bdflag.jpg",
                "is_active": true
            },
            "app_version": "15",
            "app_name": "Aeronautical Billing"
        }
    }
}
```
