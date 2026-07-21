# Get A Single Invoice Payment

**GET** `{{url}}/api/invoice-payment/3/`

## Auth

Type: `bearer`

## Examples

### Get A Single Invoice Payment

**Request:** `GET` `{{url}}/api/invoice-payment/3/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice_Payment Fetched Successfully",
    "data": {
        "result": {
            "id": 3,
            "invoice_id": 30,
            "invoice_no": "INV-000015",
            "invoice_client": "Ismail Hasan Sarker",
            "invoice_due_date": "2024-11-08",
            "invoice_total_amount": 30,
            "invoice_last_chased_payable_amount": 0,
            "payment_date": "2024-11-04",
            "payment_amount": 10,
            "organization_currency": "$",
            "exchange_rate": 123,
            "paid_to": "Owner A Share Capital",
            "reference": "City Bank",
            "bank_account_number": null
        }
    }
}
```
