# switch company

**GET** `{{url}}/api/switch-company/2`

## Auth

Type: `bearer`

## Examples

### company switch fails when membership is inactive

**Request:** `GET` `{{url}}/api/switch-company/2`

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to switch company",
    "error": "You are temporally deactivated from this company",
    "errors": null
}
```

### successful company switch

**Request:** `GET` `{{url}}/api/switch-company/2`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Company switched successfully",
    "data": {
        "result": {
            "id": 3,
            "first_name": "Admin",
            "last_name": "admin",
            "username": "admin",
            "email": "admin@gmail.com",
            "phone": "+8801684806728",
            "profile_image": null,
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMzMjM0MjgyLCJpYXQiOjE3MzMyMDU0ODIsImp0aSI6IjdmMWExZWNmYWIwYzQ3Njk5NWQxY2IyYzA5MGQ0YTAzIiwidXNlcl9pZCI6MywiYWN0aXZlX2NvbXBhbnkiOjJ9.7VH7ti9NokoO6sQiulLjWvxz7gtbloITi5jnMfJcz44",
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMzIzNDI4MiwiaWF0IjoxNzMzMjA1NDgyLCJqdGkiOiI2ZWEyNzZlYTA4OGQ0YjU0YjQzNDFlMzJkNGE2ZjUzYiIsInVzZXJfaWQiOjMsImFjdGl2ZV9jb21wYW55IjoyfQ.ykN2VXJ-cWd9rUhGIFuaN4mydPsGZb2WxgvzklYKSog"
        }
    }
}
```
