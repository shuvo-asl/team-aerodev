# mark notification as read/unread

**PATCH** `{{url}}/api/in-app-notifications/7/`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `is_read` | `false` | query |

## Body

Type: `json`

```json
{
    "is_read": false
}
```

## Examples

### mark notification as read/unread

**Request:** `PATCH` `{{url}}/api/in-app-notifications/7/`

```json
{
    "is_read": false
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "In App Notification successfully updated",
    "data": {
        "result": {
            "is_read": false
        }
    }
}
```
