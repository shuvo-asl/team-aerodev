# get activity log with pagination

**GET** `{{url}}/api/activity-log?limit=5&page=1`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `5` | query |
| `page` | `1` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### get activity log with pagination

**Request:** `GET` `{{url}}/api/activity-log?limit=5&page=1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Activity Log Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 8,
        "total_page": 2,
        "result": [
            {
                "id": 8,
                "deleted_at": null,
                "created_at": "2024-08-29T12:42:33.169151+06:00",
                "updated_at": null,
                "type": "create",
                "model": "User",
                "object": 3,
                "user_name": "",
                "ip": "192.168.65.1",
                "email": "",
                "changes": {
                    "last_login": {
                        "to": "2024-08-29T06:42:33.160012Z",
                        "from": "2024-08-28T16:03:25.189727+06:00"
                    }
                },
                "agent_info": "PostmanRuntime/7.41.1",
                "status": "success"
            },
            {
                "id": 7,
                "deleted_at": null,
                "created_at": "2024-08-28T16:08:55.456901+06:00",
                "updated_at": null,
                "type": "create",
                "model": "User",
                "object": null,
                "user_name": "admin",
                "ip": "192.168.65.1",
                "email": "admin@gmail.com",
                "changes": {
                    "email": "ismail2@asl.aero",
                    "groups": 1,
                    "password": "ismail",
                    "username": "ismail2",
                    "last_name": "Hasan",
                    "first_name": "Ismail"
                },
                "agent_info": "PostmanRuntime/7.41.1",
                "status": "failed"
            },
            {
                "id": 6,
                "deleted_at": null,
                "created_at": "2024-08-28T16:08:29.822228+06:00",
                "updated_at": null,
                "type": "update",
                "model": "User",
                "object": 10,
                "user_name": "admin",
                "ip": "192.168.65.1",
                "email": "",
                "changes": {},
                "agent_info": "PostmanRuntime/7.41.1",
                "status": "success"
            },
            {
                "id": 5,
                "deleted_at": null,
                "created_at": "2024-08-28T16:08:29.809931+06:00",
                "updated_at": null,
                "type": "update",
                "model": "User",
                "object": 10,
                "user_name": "admin",
                "ip": "192.168.65.1",
                "email": "",
                "changes": {},
                "agent_info": "PostmanRuntime/7.41.1",
                "status": "success"
            },
            {
                "id": 4,
                "deleted_at": null,
                "created_at": "2024-08-28T16:02:58.227493+06:00",
                "updated_at": null,
                "type": "auth",
                "model": null,
                "object": null,
                "user_name": "",
                "ip": "192.168.65.1",
                "email": "admin@gmail.com",
                "changes": {
                    "email": "admin@gmail.com",
                    "password": "admin2",
                    "user_type": "asl"
                },
                "agent_info": "PostmanRuntime/7.41.1",
                "status": "failed"
            }
        ]
    }
}
```
