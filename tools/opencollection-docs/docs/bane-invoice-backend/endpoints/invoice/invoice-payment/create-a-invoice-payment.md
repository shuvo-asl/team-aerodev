# Create A Invoice Payment

**POST** `{{url}}/api/invoice-payment/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "invoice": "1",
    "payment_date": "2024-11-04",
    "payment_amount": ".1",
    "organization_currency": "1",
    "exchange_rate": "123",
    "paid_to": 56,
    "reference": "City Bank",
    "send_email_to_client": true,
    "email_template": 3
}
```

## Examples

### Create A Invoice Payment

**Request:** `POST` `{{url}}/api/invoice-payment/`

```json
{
    "invoice": "30",
    "payment_date": "2024-11-04",
    "payment_amount": "10",
    "organization_currency": "1",
    "exchange_rate": "123",
    "paid_to": 227,
    "reference": "City Bank"
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Invoice_Payment successfully created",
    "data": {
        "result": {
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
    }
}
```

### Create A Invoice Payment

**Request:** `POST` `{{url}}/api/invoice-payment/`

```json
{
    "invoice": "1",
    "payment_date": "2024-11-04",
    "payment_amount": ".1",
    "organization_currency": "1",
    "exchange_rate": "123",
    "paid_to": 56,
    "reference": "City Bank",
    "send_email_to_client": true,
    "email_template": 3
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Invoice_Payment successfully created",
    "data": {
        "result": {
            "id": 50,
            "invoice_id": 1,
            "invoice_no": "INV-000001",
            "payment_date": "2024-11-04",
            "payment_amount": 0.1,
            "exchange_rate": 123,
            "paid_to": 56,
            "reference": "City Bank",
            "due_date": "2025-01-27"
        }
    }
}
```
