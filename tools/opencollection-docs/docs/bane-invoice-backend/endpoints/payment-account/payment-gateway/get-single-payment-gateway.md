# Get Single Payment Gateway

**GET** `{{url}}/api/payment-gateway/3/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get Payment Gateway Copy

**Request:** `GET` `{{url}}/api/payment-gateway/4/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Payment Gateway Fetched Successfully",
    "data": {
        "result": {
            "id": 4,
            "deleted_at": null,
            "created_at": "2024-09-03T17:07:47.253807+06:00",
            "updated_at": null,
            "name": "Stripe2",
            "display_name": "Stripe",
            "description": "A widely used online payment system.",
            "api_key": "live_api_key_12345",
            "access_key": "live_access_key_12345",
            "secret_key": "live_secret_key_12345",
            "test_api_key": "test_api_key_12345",
            "test_access_key": "test_access_key_12345",
            "test_secret_key": "test_secret_key_12345",
            "test_mode": true,
            "payment_gateway_class_name": "StripePaymentGateway",
            "is_active": true,
            "requires_3d_secure": false,
            "currency": 1,
            "supported_currencies": []
        }
    }
}
```
