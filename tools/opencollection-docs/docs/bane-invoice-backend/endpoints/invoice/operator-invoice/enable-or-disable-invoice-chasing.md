# Enable Or Disable Invoice Chasing

**PATCH** `{{url}}/api/enable-or-disable-invoice-chasing/`

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
    "invoice_id": 2,
    "is_enable": false
}
```
