# get user notifications of subscriptions

**GET** `{{url}}/api/user_notification_subscription`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### get user notifications of subscriptions

**Request:** `GET` `{{url}}/api/user_notification_subscription`

**Response:** `200 OK`

```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "app",
            "send_to_all": false,
            "created_at": "2023-09-20T11:13:18.844242+06:00",
            "updated_at": "2023-09-20T11:13:18.844271+06:00",
            "created_by": 1,
            "updated_by": null,
            "receiver": [
                1,
                2,
                3
            ]
        }
    ]
}
```
