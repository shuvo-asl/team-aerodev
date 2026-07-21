# Invoice Send To Accounting Software

**POST** `{{url}}/api/invoice-send-to-accounting-software/`

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
    "invoice_id": 68,
    "accounting_software_ids": [1]
}
```

## Examples

### Invoice Send To Accounting Software

**Request:** `POST` `{{url}}/api/invoice-send-to-accounting-software/`

```json
{
    "invoice_id": 68,
    "accounting_software_ids": [1]
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice sent to Accounting Software successfully",
    "data": {
        "result": {}
    }
}
```
