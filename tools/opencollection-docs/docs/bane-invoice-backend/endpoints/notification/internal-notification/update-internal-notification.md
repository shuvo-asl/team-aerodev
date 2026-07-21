# update internal notification

**PATCH** `{{url}}/api/notifications/15/`

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
    "active": false
    
}
```

## Examples

### update internal notification

**Request:** `PATCH` `{{url}}/api/notifications/15/`

```json
{
    "active": false
    
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
        "active": false,
        "created_at": "2023-03-27T11:00:54.250701+06:00",
        "updated_at": "2023-03-27T11:00:54.250711+06:00",
        "subscription": 2,
        "created_by": 1,
        "updated_by": 1
    }
}
```
