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
    "invoice_id": 49,
    "is_enable": false
}
```

## Examples

### Enable Or Disable Invoice Chasing

**Request:** `PATCH` `{{url}}/api/enable-or-disable-invoice-chasing/`

```json
{
    "invoice_id": 49,
    "is_enable": false
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice Chasing' Successfully Disabled",
    "data": {
        "result": {}
    }
}
```
