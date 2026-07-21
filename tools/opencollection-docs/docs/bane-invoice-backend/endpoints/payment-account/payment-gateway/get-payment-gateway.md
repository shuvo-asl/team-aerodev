# Get Payment Gateway

**GET** `{{url}}/api/payment-gateway/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Currency

**Request:** `GET` `{{url}}/api/payment-gateway/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Payment Gateway Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "deleted_at": null,
                "created_at": "2024-09-02T17:32:31.070819+06:00",
                "updated_at": null,
                "name": "EBL",
                "display_name": "Estern Bank",
                "description": "A widely used online payment system.",
                "api_key": "live_api_key_12345",
                "access_key": "live_access_key_12345",
                "secret_key": "live_secret_key_12345",
                "test_api_key": "test_api_key_12345",
                "test_access_key": "test_access_key_12345",
                "test_secret_key": "test_secret_key_12345",
                "test_mode": true,
                "payment_gateway_class_name": "EblPaymentGateway",
                "is_active": true,
                "requires_3d_secure": false,
                "currency": 1,
                "supported_currencies": []
            }
        ]
    }
}
```
