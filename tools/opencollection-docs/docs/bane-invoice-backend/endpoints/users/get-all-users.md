# Get All Users

**GET** `{{url}}/api/users/`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `5` | query |
| `page` | `2` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Users with pagination

**Request:** `GET` `{{url}}/api/users/?limit=5&page=2`

**Response:** `200 OK`

```json
{
    "success": true,
    "next": 3,
    "previous": 1,
    "current_page": 2,
    "total_object": 11,
    "total_page": 3,
    "data": [
        {
            "id": 192,
            "groups": [],
            "last_login": null,
            "is_superuser": false,
            "first_name": "Arifuzzaman",
            "last_name": "Shoab",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2023-10-26T21:16:11.277638+06:00",
            "username": "shoab01",
            "user_type": "asl",
            "email": "shoab012@asl.aero",
            "profile_image": null,
            "phone": "+8801687192510",
            "created_at": "2023-10-26T21:16:11.278012+06:00",
            "updated_at": "2023-10-26T23:04:50.629768+06:00",
            "user_permissions": []
        },
        {
            "id": 159,
            "groups": [],
            "last_login": null,
            "is_superuser": false,
            "first_name": "Arifuzzaman",
            "last_name": "Shoab",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2023-10-25T11:40:15.092308+06:00",
            "username": "shoab",
            "user_type": "asl",
            "email": "shoab@asl.aero",
            "profile_image": null,
            "phone": "+8801687192510",
            "created_at": "2023-10-25T11:40:15.092638+06:00",
            "updated_at": "2023-10-25T11:40:15.122890+06:00",
            "user_permissions": []
        },
        {
            "id": 6,
            "groups": [],
            "last_login": null,
            "is_superuser": false,
            "first_name": "nasir",
            "last_name": "khan",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2023-10-11T16:52:52+06:00",
            "username": "nasir",
            "user_type": "asl",
            "email": "nasir@asl.aero",
            "profile_image": null,
            "phone": null,
            "created_at": "2023-10-11T16:52:52.909997+06:00",
            "updated_at": "2023-10-26T23:03:33.838471+06:00",
            "user_permissions": []
        },
        {
            "id": 5,
            "groups": [],
            "last_login": "2023-10-15T11:34:53.383087+06:00",
            "is_superuser": false,
            "first_name": "afroza",
            "last_name": "akter",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2023-10-11T14:58:32+06:00",
            "username": "Afroza",
            "user_type": "asl",
            "email": "afroza@aslgroup.com.bd",
            "profile_image": null,
            "phone": null,
            "created_at": "2023-10-11T14:58:32.996149+06:00",
            "updated_at": "2023-10-26T23:03:47.830040+06:00",
            "user_permissions": []
        },
        {
            "id": 3,
            "groups": [],
            "last_login": null,
            "is_superuser": false,
            "first_name": "test2",
            "last_name": "test2",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2023-09-10T13:18:32+06:00",
            "username": "caabtest1",
            "user_type": "caab",
            "email": "caabtest1@gmail.com",
            "profile_image": null,
            "phone": "+8801558970484",
            "created_at": "2023-09-10T13:18:32.106000+06:00",
            "updated_at": "2023-10-26T18:02:35.516444+06:00",
            "user_permissions": []
        }
    ]
}
```

### user list for support ticketing

**Request:** `GET` `{{url}}/api/users/?limit=5&page=1&for_support_ticket=true`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "User Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 24,
        "total_page": 5,
        "result": [
            {
                "id": 1,
                "username": "admin",
                "first_name": "Admin",
                "last_name": "Admin",
                "is_active": true,
                "user_type": "asl",
                "email": "admin@gmail.com",
                "profile_image": null,
                "phone": "+8801684806728",
                "groups": [
                    {
                        "id": 1,
                        "name": "admin"
                    },
                    {
                        "id": 3,
                        "name": "Admin"
                    },
                    {
                        "id": 7,
                        "name": "Admin"
                    },
                    {
                        "id": 11,
                        "name": "Admin"
                    },
                    {
                        "id": 15,
                        "name": "Admin"
                    },
                    {
                        "id": 20,
                        "name": "Admin"
                    },
                    {
                        "id": 24,
                        "name": "Admin"
                    },
                    {
                        "id": 27,
                        "name": "operator"
                    },
                    {
                        "id": 28,
                        "name": "Admin"
                    },
                    {
                        "id": 32,
                        "name": "Admin"
                    }
                ]
            },
            {
                "id": 2,
                "username": "afroza",
                "first_name": "Afroza",
                "last_name": "Akter",
                "is_active": true,
                "user_type": "asl",
                "email": "afroza@asl.aero",
                "profile_image": null,
                "phone": "+8801704173329",
                "groups": [
                    {
                        "id": 2,
                        "name": "Ridoy"
                    }
                ]
            },
            {
                "id": 3,
                "username": "jeff",
                "first_name": "Jeff",
                "last_name": "Bezos",
                "is_active": true,
                "user_type": "asl",
                "email": "jeff@gmail.com",
                "profile_image": null,
                "phone": "8801558250667",
                "groups": [
                    {
                        "id": 3,
                        "name": "Admin"
                    }
                ]
            },
            {
                "id": 4,
                "username": "admin1",
                "first_name": "admin1",
                "last_name": "admin1",
                "is_active": true,
                "user_type": "asl",
                "email": "admin1@gmail.com",
                "profile_image": null,
                "phone": "+12125552368",
                "groups": [
                    {
                        "id": 7,
                        "name": "Admin"
                    }
                ]
            },
            {
                "id": 5,
                "username": "admin2",
                "first_name": "admin",
                "last_name": "admin",
                "is_active": true,
                "user_type": "asl",
                "email": "admin2@gmail.com",
                "profile_image": null,
                "phone": "8801558250667",
                "groups": [
                    {
                        "id": 11,
                        "name": "Admin"
                    }
                ]
            }
        ]
    }
}
```
