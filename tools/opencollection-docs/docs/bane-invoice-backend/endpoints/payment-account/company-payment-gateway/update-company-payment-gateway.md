# update company payment gateway

**PATCH** `{{url}}/api/company-payment-gateway/1/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "is_active": true
}
```

## Examples

### update company payment gateway

**Request:** `PATCH` `{{url}}/api/company-payment-gateway/1/`

```json
{
    "is_active": true
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Payment Gateway successfully updated",
    "data": {
        "result": {
            "is_active": true,
            "name": "EBL",
            "id": 1,
            "payment_gateway_model": 1,
            "test_mode": true,
            "gateway_type": "ebl",
            "bank": "CITY USD"
        }
    }
}
```
