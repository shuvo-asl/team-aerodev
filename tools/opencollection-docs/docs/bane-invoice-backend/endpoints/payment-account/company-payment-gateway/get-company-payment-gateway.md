# get company payment gateway

**GET** `{{url}}/api/company-payment-gateway/`

## Auth

Type: `bearer`

## Examples

### get company payment gateway

**Request:** `GET` `{{url}}/api/company-payment-gateway/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Payment Gateway Successfully Fetched",
    "data": {
        "result": [
            {
                "is_active": true,
                "name": "EBL",
                "id": 1,
                "payment_gateway_model": 1,
                "test_mode": true,
                "gateway_type": "ebl",
                "bank": "CITY USD"
            }
        ]
    }
}
```
