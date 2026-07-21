# invoices-by-status

**GET** `{{url}}/api/invoices-by-status`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### invoices-by-status

**Request:** `GET` `{{url}}/api/invoices-by-status`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoices By Status",
    "data": {
        "result": {
            "draft": 30,
            "sent": 184,
            "paid": 0,
            "overdue": 0
        }
    }
}
```
