# create test invoice accounting software

**POST** `{{url}}/api/create-test-invoice/`

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
    "account": "xero",
    "data": {
        "invoice_no": "INV000001"
    }
}
```
