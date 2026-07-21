# Retrieve User

**GET** `{{url}}/api/users/249/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Retrieve User

**Request:** `GET` `{{url}}/api/users/10/`

**Response:** `200 OK`

```json
{
    "id": 10,
    "groups": [],
    "last_login": null,
    "is_superuser": false,
    "first_name": "ismail",
    "last_name": "titas",
    "is_staff": false,
    "is_active": false,
    "date_joined": "2024-03-24T11:31:27+06:00",
    "username": "trinity",
    "user_type": "asl",
    "email": "trinity@gmail.com",
    "profile_image": null,
    "phone": "+8801558970484",
    "created_at": "2024-03-24T11:31:44.234352+06:00",
    "updated_at": "2024-09-01T10:52:46.095007+06:00",
    "user_permissions": []
}
```
