# get notifications of subscriptions

**GET** `{{url}}/api/subscription_notifications?subscription=3`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `subscription` | `3` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### get notifications of subscriptions success

**Request:** `GET` `{{url}}/api/subscription_notifications?subscription=2`

**Response:** `200 OK`

```json
{
    "success": true,
    "data": [
        {
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
    ]
}
```

### get notifications of subscriptions failed

**Request:** `GET` `{{url}}/api/subscription_notifications?subscription=3`

**Response:** `400 Bad Request`

```json
{
    "success": false,
    "data": {
        "msg": "NotificationSubsribe matching query does not exist."
    }
}
```
