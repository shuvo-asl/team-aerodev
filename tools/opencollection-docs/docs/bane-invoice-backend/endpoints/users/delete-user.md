# Delete User

**DELETE** `{{url}}/api/users/197/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Delete User

**Request:** `DELETE` `{{url}}/api/users/10/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'User' Successfully Deleted",
    "data": {
        "result": []
    }
}
```
