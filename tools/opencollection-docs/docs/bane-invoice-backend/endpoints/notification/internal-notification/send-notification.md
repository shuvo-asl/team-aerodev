# send notification

**POST** `{{url}}/api/send_notification/`

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
    "subscription": 3,
    "message": "test 9"
}
```

## Examples

### send notification success

**Request:** `POST` `{{url}}/api/send_notification/`

```json
{
    "subscription": 1,
    "message": "test 9"
}
```

**Response:** `200 OK`

```json
{
    "success": true
}
```

### send notification failed

**Request:** `POST` `{{url}}/api/send_notification/`

```json
{
    "subscription": 3,
    "message": "test 9"
}
```

**Response:** `400 Bad Request`

```json
{
    "success": false,
    "data": {
        "msg": "NotificationSubsribe matching query does not exist."
    }
}
```
