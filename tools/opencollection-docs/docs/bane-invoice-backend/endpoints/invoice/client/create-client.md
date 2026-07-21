# Create Client

**POST** `{{url}}/api/client/`

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
    "name": "US Bangla5",
    "short_code": "us5",
    "email": "usbangla415@asl.aero",
    "phone": "+8801558250667",
    "billing_address": "Dhaka, Bangladesh",
    "days_to_due_date": 23,
    "chasing_rule":[1, 2],
    "interest_rule": [8]
}
```

## Examples

### Create Client

**Request:** `POST` `{{url}}/api/client/`

```json
{
    "name": "US Bangla5",
    "short_code": "us5",
    "email": "usbangla415@asl.aero",
    "phone": "+8801558250667",
    "billing_address": "Dhaka, Bangladesh",
    "days_to_due_date": 23,
    "chasing_rule":[1, 2],
    "interest_rule": [8]
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Client successfully created",
    "data": {
        "result": {
            "id": 27,
            "name": "US Bangla5",
            "short_code": "us5",
            "email": "usbangla415@asl.aero",
            "phone": "+8801558250667",
            "billing_address": "Dhaka, Bangladesh",
            "days_to_due_date": 23,
            "client_type": "agent",
            "preferred_currency": null,
            "status": "active",
            "chasing_rule": [
                {
                    "id": 2,
                    "name": "default",
                    "is_default": true,
                    "chase_on": "after due date",
                    "is_cumulative": true,
                    "max_repetition": 4,
                    "email_template": 1,
                    "email_template_name": "default",
                    "chasing_days": []
                },
                {
                    "id": 1,
                    "name": "fixed interest",
                    "is_default": false,
                    "chase_on": "after due date",
                    "is_cumulative": true,
                    "max_repetition": null,
                    "email_template": 2,
                    "email_template_name": "payment notification",
                    "chasing_days": []
                }
            ],
            "interest_rule": [
                {
                    "id": 8,
                    "name": "Ridoy",
                    "is_default": true,
                    "is_cumulative": false,
                    "day": 3,
                    "max_repetition": null,
                    "interest_type": "percentage",
                    "interest_rate": 12,
                    "interest_base": "invoice_base_amount"
                }
            ]
        }
    }
}
```
