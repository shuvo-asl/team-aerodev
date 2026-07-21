# Create Payment Gateway

**POST** `{{url}}/api/payment-gateway/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
    {
        "name": "EBL6",
        "display_name": "EBL",
        "description": "A widely used online payment system.",
        "gateway_type": 1,
        "api_key": "live_api_key_12345",
        "access_key": "live_access_key_12345",
        "secret_key": "live_secret_key_12345",
        "test_api_key": "test_api_key_12345",
        "test_access_key": "test_access_key_12345",
        "test_secret_key": "test_secret_key_12345",
        "test_mode": true,
        "supported_currencies": [27, 28],
        "bank": 343,
        "others": {"return_url": "url", "time_out_url": "dummy url"}
    }
```

## Examples

### Create Payment Gateway

**Request:** `POST` `{{url}}/api/payment-gateway/`

```json
    {
        "name": "EBL4",
        "display_name": "EBL",
        "description": "A widely used online payment system.",
        "gateway_type": 1,
        "api_key": "live_api_key_12345",
        "access_key": "live_access_key_12345",
        "secret_key": "live_secret_key_12345",
        "test_api_key": "test_api_key_12345",
        "test_access_key": "test_access_key_12345",
        "test_secret_key": "test_secret_key_12345",
        "test_mode": true,
        "supported_currencies": [1, 2],
        "bank": 55,
        "others": {"return_url": "url", "time_out_url": "dummy url"}
    }
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Payment Gateway successfully created",
    "data": {
        "result": {
            "id": 4,
            "deleted_at": null,
            "created_at": "2025-02-19T10:42:14.505890+06:00",
            "updated_at": null,
            "name": "EBL4",
            "display_name": "EBL",
            "description": "A widely used online payment system.",
            "api_key": "live_api_key_12345",
            "access_key": "live_access_key_12345",
            "secret_key": "live_secret_key_12345",
            "test_api_key": "test_api_key_12345",
            "test_access_key": "test_access_key_12345",
            "test_secret_key": "test_secret_key_12345",
            "test_mode": true,
            "others": {
                "return_url": "url",
                "time_out_url": "dummy url"
            },
            "requires_3d_secure": false,
            "bank": 55,
            "currency": null,
            "gateway_type": 1,
            "owner": 1,
            "supported_currencies": [
                1,
                2
            ]
        }
    }
}
```
