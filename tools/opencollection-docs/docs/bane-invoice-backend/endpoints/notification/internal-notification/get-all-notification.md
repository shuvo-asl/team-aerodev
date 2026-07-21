# get all notification

**GET** `{{url}}/api/notifications`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### get all notification

**Request:** `GET` `{{url}}/api/notifications`

**Response:** `200 OK`

```json
{
    "success": true,
    "data": [
        {
            "id": 4,
            "notification_type": "non_schedule",
            "message": "test 9",
            "broadcast_month": "*",
            "broadcast_day": "*",
            "broadcast_hour": "*",
            "broadcast_minute": "*",
            "is_onetime": false,
            "active": false,
            "created_at": "2023-09-20T12:19:04.933048+06:00",
            "updated_at": "2023-09-20T12:19:04.933073+06:00",
            "subscription": 1,
            "created_by": 1,
            "updated_by": null
        },
        {
            "id": 3,
            "notification_type": "non_schedule",
            "message": "Hello Nasir",
            "broadcast_month": "*",
            "broadcast_day": "*",
            "broadcast_hour": "*",
            "broadcast_minute": "*",
            "is_onetime": false,
            "active": false,
            "created_at": "2023-09-20T11:59:04.282542+06:00",
            "updated_at": "2023-09-20T11:59:04.282564+06:00",
            "subscription": 1,
            "created_by": 1,
            "updated_by": null
        },
        {
            "id": 2,
            "notification_type": "non_schedule",
            "message": "test 9",
            "broadcast_month": "*",
            "broadcast_day": "*",
            "broadcast_hour": "*",
            "broadcast_minute": "*",
            "is_onetime": false,
            "active": false,
            "created_at": "2023-09-20T11:39:17.850851+06:00",
            "updated_at": "2023-09-20T11:39:17.850882+06:00",
            "subscription": 1,
            "created_by": 1,
            "updated_by": null
        },
        {
            "id": 1,
            "notification_type": "non_schedule",
            "message": "Hello Guys",
            "broadcast_month": "*",
            "broadcast_day": "*",
            "broadcast_hour": "*",
            "broadcast_minute": "*",
            "is_onetime": false,
            "active": false,
            "created_at": "2023-09-20T11:15:19.384732+06:00",
            "updated_at": "2023-09-20T11:15:19.384753+06:00",
            "subscription": 1,
            "created_by": 1,
            "updated_by": null
        }
    ]
}
```
