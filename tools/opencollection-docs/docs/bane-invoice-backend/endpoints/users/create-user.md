# Create User

**POST** `{{url}}/api/users/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

```
[{'name': 'username', 'type': 'text', 'value': 'new_user'}, {'name': 'first_name', 'type': 'text', 'value': 'first_name'}, {'name': 'last_name', 'type': 'text', 'value': 'last_name'}, {'name': 'user_type', 'type': 'text', 'value': 'caab'}, {'name': 'email', 'type': 'text', 'value': 'u667688@gmail.com'}, {'name': 'profile_image', 'type': 'file', 'value': ['/home/devs/Music/images.png']}, {'name': 'password', 'type': 'text', 'value': 'testpassword'}, {'name': 'companies', 'type': 'text', 'value': '1'}, {'name': 'companies', 'type': 'text', 'value': '2'}]
```

## Examples

### Create User

**Request:** `POST` `{{url}}/api/users/`

```json
[{'name': 'username', 'type': 'text', 'value': 'new_user'}, {'name': 'first_name', 'type': 'text', 'value': 'first_name'}, {'name': 'last_name', 'type': 'text', 'value': 'last_name'}, {'name': 'user_type', 'type': 'text', 'value': 'operator'}, {'name': 'email', 'type': 'text', 'value': 'u5@gmail.com'}, {'name': 'profile_image', 'type': 'file', 'value': ['/home/devs/Music/images.png']}, {'name': 'password', 'type': 'text', 'value': 'testpassword'}, {'name': 'companies', 'type': 'text', 'value': '1'}, {'name': 'companies', 'type': 'text', 'value': '2'}]
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "User successfully created",
    "data": {
        "result": {
            "id": 35,
            "username": "new_user",
            "first_name": "first_name",
            "last_name": "last_name",
            "is_active": false,
            "user_type": "operator",
            "email": "u5@gmail.com",
            "profile_image": null,
            "phone": null,
            "groups": [
                {
                    "id": 2,
                    "name": "Operator",
                    "permissions": [
                        68,
                        70,
                        71,
                        72,
                        73
                    ]
                }
            ]
        }
    }
}
```
