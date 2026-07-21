# initiate payment process

**POST** `{{url}}/api/initiate-payment-process/`

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{
    "gateway_name": "stripe",
    "invoice_id": 60,
    "company_id": 1,
    "token": "e6c8ef45-3734-4fbe-aaa4-c912cfefe0cd"
}
```

## Examples

### Stripe initiate payment process

**Request:** `POST` `{{url}}/api/initiate-payment-process/`

```json
{
    "gateway_name": "stripe",
    "invoice_id": 84,
    "company_id": 1,
    "token": "26b90704-db60-4591-bda6-a4342604e5d4"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Payment Process Successfully Initiated",
    "data": {
        "result": {
            "client_secret": "pi_3RGdYL4Jc2o38mIb0iWnlWF9_secret_SGOfirOVcLupM3i0MOJlDuEb3",
            "invoice_id": 84,
            "public_key": "pk_test_51RFyzg4Jc2o38mIbKBKbhQOsZPfsntxeP8x3e9JQYRq7SQmCkcB2T6klf5Wz6roIwOZN6UzK7gYLnbKIiE7HxfK800Md3rt0GJ",
            "payment_amount": 20,
            "amount": 25,
            "currency": "bdt",
            "processing_fee": 5,
            "tax_amount": 0,
            "invoice_no": "INV-000083",
            "items": [
                {
                    "name": "aaaa",
                    "quantity": 1,
                    "unitPrice": 20
                }
            ]
        }
    }
}
```
