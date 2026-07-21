# Update User

**PATCH** `{{url}}/api/users/17/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
{
    "username": "ziliun",
    "first_name": "Ziliun",
    "last_name": "Sikder",
    "is_active": true,
    "user_type": "asl",
    "email": "ziliun@asl.aero",
    "phone": "+8801713429926",
    "groups": 11,
    "active_company": 2,
    "companies": [
        3
    ]
}
```

## Examples

### Update User

**Request:** `PATCH` `{{url}}/api/users/40/`

```json
{
    "first_name": "ismail",
    "last_name": "titas",
    "phone": "+8801558970484"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "User successfully updated",
    "data": {
        "result": {
            "id": 40,
            "username": "user7",
            "first_name": "ismail",
            "last_name": "titas",
            "is_active": false,
            "user_type": "operator",
            "email": "user769@gmail.com",
            "profile_image": null,
            "phone": "+8801558970484",
            "groups": [
                {
                    "id": 2,
                    "name": "Operator",
                    "permissions": [
                        66
                    ]
                }
            ]
        }
    }
}
```
