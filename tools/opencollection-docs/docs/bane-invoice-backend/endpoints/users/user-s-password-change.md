# User's Password Change

**POST** `{{url}}/api/change_users_password/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

```
[{'name': 'new_password', 'type': 'text', 'value': 'admin123456'}, {'name': 'confirm_password', 'type': 'text', 'value': 'admin123456'}, {'name': 'user_id', 'type': 'text', 'value': '8'}]
```

## Examples

### User's Password Change

**Request:** `POST` `{{url}}/api/change_users_password/`

```json
[{'name': 'new_password', 'type': 'text', 'value': 'admin123456'}, {'name': 'confirm_password', 'type': 'text', 'value': 'admin123456'}, {'name': 'user_id', 'type': 'text', 'value': '8'}]
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'User's Password' Successfully Changed",
    "data": {
        "result": []
    }
}
```
