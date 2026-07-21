# Get All Users By User Type

**GET** `{{url}}/api/users/?limit=10&user_type=asl`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `10` | query |
| `user_type` | `asl` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Users By User Type ASL

**Request:** `GET` `{{url}}/api/users/?limit=10&user_type=asl`

**Response:** `200 OK`

```json
{
    "success": true,
    "next": null,
    "previous": null,
    "current_page": 1,
    "total_object": 1,
    "total_page": 1,
    "data": [
        {
            "id": 2,
            "groups": [
                {
                    "id": 1,
                    "name": "asl",
                    "permissions": [
                        65,
                        60
                    ]
                }
            ],
            "last_login": "2023-09-12T13:33:05.493511+06:00",
            "is_superuser": false,
            "first_name": "",
            "last_name": "",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2023-09-10T13:17:11+06:00",
            "username": "test1",
            "user_type": "asl",
            "email": "test1@gmail.com",
            "profile_image": null,
            "phone": null,
            "created_at": "2023-09-10T13:17:11.933182+06:00",
            "updated_at": "2023-09-10T15:55:55.791998+06:00",
            "user_permissions": []
        }
    ]
}
```
