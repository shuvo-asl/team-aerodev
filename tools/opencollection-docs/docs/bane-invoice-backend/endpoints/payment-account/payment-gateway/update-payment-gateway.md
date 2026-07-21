# Update Payment Gateway

**PATCH** `{{url}}/api/payment-gateway/1/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
    {
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
        "currency": 1,
        "supported_currencies": [],
        "payment_gateway_class_name": "EblPaymentGateway",
        "is_active": true,
        "requires_3d_secure": false
    }
```

## Examples

### Update Payment Gateway

**Request:** `PATCH` `{{url}}/api/payment-gateway/1/`

```json
    {
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
        "currency": 1,
        "supported_currencies": [],
        "payment_gateway_class_name": "EblPaymentGateway",
        "is_active": true,
        "requires_3d_secure": false
    }
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Payment Gateway successfully updated",
    "data": {
        "result": {
            "id": 1,
            "deleted_at": null,
            "created_at": "2024-09-02T17:32:31.070819+06:00",
            "updated_at": "2024-09-02T17:33:23.603989+06:00",
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
    }
}
```
