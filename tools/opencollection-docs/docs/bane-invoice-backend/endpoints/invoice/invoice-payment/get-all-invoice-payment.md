# Get All Invoice Payment

**GET** `{{url}}/api/invoice-payment/?invoice_id=32`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `payment_date` | `2024-10-04` | query |
| `limit` | `2` | query |
| `created_at` | `2024-11-04` | query |
| `paid_to` | `227` | query |
| `invoice_id` | `32` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |
| `` | `` |

## Examples

### Get All Invoice Payment

**Request:** `GET` `{{url}}/api/invoice-payment/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice_Payment Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "invoice_id": 30,
                "invoice_no": "INV-000015",
                "payment_date": "2024-11-04",
                "payment_amount": 10,
                "organization_currency": "$",
                "exchange_rate": 122,
                "paid_to": "Owner A Share Capital",
                "reference": null
            },
            {
                "id": 2,
                "invoice_id": 30,
                "invoice_no": "INV-000015",
                "payment_date": "2024-11-04",
                "payment_amount": 10,
                "organization_currency": "$",
                "exchange_rate": 123,
                "paid_to": "Owner A Share Capital",
                "reference": "City Bank"
            },
            {
                "id": 3,
                "invoice_id": 30,
                "invoice_no": "INV-000015",
                "payment_date": "2024-11-04",
                "payment_amount": 10,
                "organization_currency": "$",
                "exchange_rate": 123,
                "paid_to": "Owner A Share Capital",
                "reference": "City Bank"
            }
        ]
    }
}
```
