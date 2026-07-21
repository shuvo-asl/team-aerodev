# total-invoices

**GET** `{{url}}/api/total-invoices/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### total-invoices

**Request:** `GET` `{{url}}/api/total-invoices/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Total Invoices",
    "data": {
        "result": {
            "total_invoices": 218,
            "total_due": 8823.09,
            "total_paid": 5
        }
    }
}
```
