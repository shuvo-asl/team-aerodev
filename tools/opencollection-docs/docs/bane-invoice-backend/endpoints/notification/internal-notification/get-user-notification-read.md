# get User notification read

**GET** `{{url}}/api/user_notification_read`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### get User notification read

**Request:** `GET` `{{url}}/api/user_notification_read`

**Response:** `200 OK`

```json
{
    "success": true,
    "data": {
        "id": 1,
        "total_notification": 1,
        "user": 1
    }
}
```
