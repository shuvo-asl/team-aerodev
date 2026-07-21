# Generate login credentials

**GET** `{{url}}/api/generate_login_credentials?username=admin`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `username` | `admin` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Generate login credentials

**Request:** `GET` `{{url}}/api/generate_login_credentials?username=admin`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Succesfully Generated Login Credentials",
    "data": {
        "result": {
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTE5NTEwMSwiaWF0IjoxNzI1MTY2MzAxLCJqdGkiOiJjZTFiMGJjNzU3ZjA0NjQyOTAwOWNlODI4MGRjYWQ2ZiIsInVzZXJfaWQiOjN9.qOVgu9dAHFhmm4_ZGM3bVrJDgcd1qkmYPVUu433wGCo",
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1MTk1MTAxLCJpYXQiOjE3MjUxNjYzMDEsImp0aSI6ImI5NDFkYzBkMGQ3YTQyMTk5ZTU3OWRhOTQwZTI4NDI3IiwidXNlcl9pZCI6M30.5NDioFGTJXjSTM3nZpbGGt3rGXz1BKyiRN_ojREHDww",
            "id": 3,
            "username": "admin",
            "first_name": "local",
            "last_name": "admin",
            "email": "admin@gmail.com",
            "phone": "+8801687192510",
            "user_type": "asl",
            "profile_image": null,
            "redirect_url": "http://localhost:3000/asl"
        }
    }
}
```
