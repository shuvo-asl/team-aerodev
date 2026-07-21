# notification count

**GET** `{{url}}/api/in-app-notifications/notification-count/`

## Auth

Type: `bearer`

## Examples

### notification count

**Request:** `GET` `{{url}}/api/in-app-notifications/notification-count/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Successfully fetched Notification Count",
    "data": {
        "result": {
            "notification_count": 1
        }
    }
}
```
