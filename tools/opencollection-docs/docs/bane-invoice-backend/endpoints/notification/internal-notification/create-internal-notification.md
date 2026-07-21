# create internal notification

**POST** `{{url}}/api/notifications/`

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
    "subscription": 1,
    "notification_type": "demo",
    "message": "test",
    "broadcast_month": "*",
    "broadcast_day": "*",
    "broadcast_hour": "*",
    "broadcast_minute": "*"
    
}
```

## Examples

### create internal notification

**Request:** `POST` `{{url}}/api/notifications/`

```json
{
    "subscription": "2",
    "notification_type": "create",
    "message": "test created",
    "broadcast_month": "*",
    "broadcast_day": "*",
    "broadcast_hour": "*",
    "broadcast_minute": "*"
    
}
```

**Response:** `200 OK`

```json
{
    "success": true,
    "data": {
        "id": 15,
        "notification_type": "create",
        "message": "test created",
        "broadcast_month": "*",
        "broadcast_day": "*",
        "broadcast_hour": "*",
        "broadcast_minute": "*",
        "is_onetime": false,
        "active": true,
        "created_at": "2023-03-27T11:00:54.250701+06:00",
        "updated_at": "2023-03-27T11:00:54.250711+06:00",
        "subscription": 2,
        "created_by": 1,
        "updated_by": null
    }
}
```
