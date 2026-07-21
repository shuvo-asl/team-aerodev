# sse notification

**GET** `{{url}}/sse/notifications-stream/`

## Auth

Type: `bearer`

## Body

Type: `text`

```
{
    "email": "admin@gmail.com",
    "password": "admin@123",
    "user_type": "asl"
}
```

## Examples

### sse notification

**Request:** `GET` `{{url}}/api/sse/notifications-stream/`

```json
{
    "email": "admin@gmail.com",
    "password": "admin@123",
    "user_type": "asl"
}
```

**Response:** `200 OK`
