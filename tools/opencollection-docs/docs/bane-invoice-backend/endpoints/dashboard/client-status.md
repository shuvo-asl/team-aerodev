# client-status

**GET** `{{url}}/api/client-status/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### client-status

**Request:** `GET` `{{url}}/api/client-status/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Client Status",
    "data": {
        "result": {
            "active_clients": 36,
            "inactive_clients": 4
        }
    }
}
```
