# Update client

**PATCH** `{{url}}/api/client/1/`

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
    "name": "test"
}
```

## Examples

### Update client

**Request:** `PATCH` `{{url}}/api/client/1/`

```json
{
    "name": "test"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Client successfully updated",
    "data": {
        "result": {
            "id": 1,
            "name": "test",
            "short_code": "cl0089",
            "email": "cleint@gmail.com",
            "phone": "+8801684806728",
            "billing_address": "jehfrjh,ehierur",
            "days_to_due_date": 14,
            "client_type": "agent",
            "preferred_currency": {
                "id": 2,
                "prefix": "₹",
                "short_key": "INR",
                "current_rate": 0.7064,
                "default": null,
                "name": "Rupee",
                "flag": "/api/media/india.png",
                "is_active": true
            },
            "status": "inactive",
            "chasing_rule": null
        }
    }
}
```
