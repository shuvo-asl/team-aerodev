# get filtered activity log

**GET** `{{url}}/api/activity-log?start_date=2024-08-28&end_date=2024-08-29&user_name=admin&type=create`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `start_date` | `2024-08-28` | query |
| `end_date` | `2024-08-29` | query |
| `user_name` | `admin` | query |
| `type` | `create` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### get filtered activity log

**Request:** `GET` `{{url}}/api/activity-log?start_date=2024-08-28&end_date=2024-08-29&user_name=admin&type=create`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Activity Log Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 9,
                "deleted_at": null,
                "created_at": "2024-08-29T13:24:05.394604+06:00",
                "updated_at": null,
                "type": "create",
                "model": "User",
                "object": null,
                "user_name": "admin",
                "ip": "192.168.65.1",
                "email": "admin@gmail.com",
                "changes": {
                    "email": "ismail@asl.aero",
                    "groups": 161,
                    "password": "ismail",
                    "username": "ismail",
                    "last_name": "Hasan",
                    "first_name": "Ismail"
                },
                "agent_info": "PostmanRuntime/7.41.1",
                "status": "failed"
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
                "id": 3,
                "deleted_at": null,
                "created_at": "2024-08-28T16:01:52.424400+06:00",
                "updated_at": null,
                "type": "create",
                "model": "User",
                "object": null,
                "user_name": "admin",
                "ip": "192.168.65.1",
                "email": "admin@gmail.com",
                "changes": {
                    "email": "ismail@asl.aero",
                    "groups": 161,
                    "password": "ismail",
                    "username": "ismail",
                    "last_name": "Hasan",
                    "first_name": "Ismail"
                },
                "agent_info": "PostmanRuntime/7.41.1",
                "status": "failed"
            },
            {
                "id": 2,
                "deleted_at": null,
                "created_at": "2024-08-28T16:01:45.435513+06:00",
                "updated_at": null,
                "type": "create",
                "model": "User",
                "object": null,
                "user_name": "admin",
                "ip": "192.168.65.1",
                "email": "admin@gmail.com",
                "changes": {
                    "role": 161,
                    "email": "ismail@asl.aero",
                    "password": "ismail",
                    "username": "ismail",
                    "last_name": "Hasan",
                    "first_name": "Ismail"
                },
                "agent_info": "PostmanRuntime/7.41.1",
                "status": "failed"
            },
            {
                "id": 1,
                "deleted_at": null,
                "created_at": "2024-08-28T16:01:35.784478+06:00",
                "updated_at": null,
                "type": "create",
                "model": "User",
                "object": null,
                "user_name": "admin",
                "ip": "192.168.65.1",
                "email": "admin@gmail.com",
                "changes": {
                    "email": "ismail@asl.aero",
                    "groups": 161,
                    "password": "ismail",
                    "username": "ismail",
                    "last_name": "Hasan",
                    "first_name": "Ismail"
                },
                "agent_info": "PostmanRuntime/7.41.1",
                "status": "failed"
            }
        ]
    }
}
```
