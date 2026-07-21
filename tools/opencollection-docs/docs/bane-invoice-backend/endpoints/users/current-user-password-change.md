# Current User Password Change

**PUT** `{{url}}/api/change_password/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

```
[{'name': 'old_password', 'type': 'text', 'value': 'admin'}, {'name': 'new_password', 'type': 'text', 'value': 'admin'}]
```

## Examples

### Current User Password Change

**Request:** `PUT` `{{url}}/api/change_password/`

```json
[{'name': 'old_password', 'type': 'text', 'value': 'admin'}, {'name': 'new_password', 'type': 'text', 'value': 'admin'}]
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Password' Successfully Changed",
    "data": {
        "result": []
    }
}
```
