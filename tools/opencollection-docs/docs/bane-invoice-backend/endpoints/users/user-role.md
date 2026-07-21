# User Role

**GET** `{{url}}/api/user_role/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### User Role

**Request:** `GET` `{{url}}/api/user_role/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'User Role' Successfully Fetched",
    "data": {
        "result": [
            "add_actiontype"
        ]
    }
}
```
