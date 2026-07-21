# check email

**GET** `{{url}}/api/check-email/admin@gmail.com/`

## Auth

Type: `bearer`

## Examples

### check email

**Request:** `GET` `{{url}}/api/check-email/admin@gmail.com/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Email checked successfully",
    "data": {
        "result": {
            "email_exists": true,
            "within_same_tenant": true,
            "profile_data": {
                "id": 3,
                "first_name": "Admin",
                "last_name": "admin",
                "username": "admin",
                "email": "admin@gmail.com",
                "phone": "+8801684806728",
                "profile_image": null
            }
        }
    }
}
```
