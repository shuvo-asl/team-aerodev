# Xero Check Connection

**GET** `{{url}}/api/xero/check-connection/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### Xero Check Connection

**Request:** `GET` `{{url}}/api/xero/check-connection/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Xero' Is Not Connected",
    "data": {
        "result": false
    }
}
```
