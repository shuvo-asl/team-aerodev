# generate invoice number

**GET** `{{url}}/api/generate-invoice-number/`

## Auth

Type: `bearer`

## Examples

### generate invoice number

**Request:** `GET` `{{url}}/api/generate-invoice-number/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Changes are being pushed to the accounting software",
    "data": {
        "result": {
            "invoice_number": "000033",
            "prefix": "INV:"
        }
    }
}
```
