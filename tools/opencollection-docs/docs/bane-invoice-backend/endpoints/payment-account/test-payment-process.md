# Test Payment Process

**POST** `{{url}}/api/payment-process/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
{
    "gateway_name" : "ebl",
    "amount": 1000,
    "currency": "BDT"
}
```
