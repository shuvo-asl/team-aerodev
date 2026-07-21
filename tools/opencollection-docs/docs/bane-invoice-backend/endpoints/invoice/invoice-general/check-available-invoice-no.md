# Check available invoice no

**GET** `{{url}}/api/invoice/check-invoice-no/?invoice_no=INV-000083`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `invoice_no` | `INV-000083` | query |
| `invoice_id` | `84` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Check Available invoice no

**Request:** `GET` `{{url}}/api/invoice/check-invoice-no/?invoice_no=INV-000083`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice number 'INV-000083' is already in use",
    "data": {
        "result": {
            "available": false,
            "invoice_no": "INV-000083",
            "existing_invoice_status": "sent"
        }
    }
}
```

### Available while editing invoice

**Request:** `GET` `{{url}}/api/invoice/check-invoice-no/?invoice_no=INV-000083&invoice_id=84`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice number 'INV-000083' is available",
    "data": {
        "result": {
            "available": true,
            "invoice_no": "INV-000083"
        }
    }
}
```

### Validation Failed

**Request:** `GET` `{{url}}/api/invoice/check-invoice-no/`

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Invoice number parameter is missing",
    "error": "invoice_no parameter is required",
    "errors": null
}
```
