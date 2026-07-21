# Current User Profile Update

**PATCH** `{{url}}/api/update_profile/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

```
[{'name': 'profile_image', 'type': 'file', 'value': ['/home/devs/images.jpeg']}, {'name': 'first_name', 'type': 'text', 'value': 'Admin'}, {'name': 'phone', 'type': 'text', 'value': '+8801684806728'}]
```

## Examples

### Current User Profile Update

**Request:** `PATCH` `{{url}}/api/update_profile/`

```json
[{'name': 'profile_image', 'type': 'file', 'value': ['/home/devs/images.jpeg']}, {'name': 'first_name', 'type': 'text', 'value': 'Admin'}, {'name': 'phone', 'type': 'text', 'value': '+8801684806728'}]
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Profile' Successfully Updated",
    "data": {
        "result": {
            "id": 3,
            "first_name": "Admin",
            "last_name": "admin",
            "username": "admin",
            "email": "admin@gmail.com",
            "phone": "+8801684806728",
            "profile_image": "/api/media/images/profile_images/2024/09/britian.png"
        }
    }
}
```
