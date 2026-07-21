# Get Invoice Chasing Schedule by invoice id

**GET** `{{url}}/api/invoice-chasing-schedule?invoice_id=58`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `invoice_id` | `58` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Invoice Chasing Schedule Copy

**Request:** `GET` `{{url}}/api/invoice-chasing-schedule?invoice_id=58`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Chasing Schedule Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 84,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 3,
                "interest_type": "fixed",
                "interest_rate": 21,
                "is_cumulative": false,
                "chased": true,
                "chasing_date": "2024-08-01",
                "invoice": 58,
                "chasing_rule_item": 2,
                "email_template": 1
            },
            {
                "id": 85,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 15,
                "interest_type": "fixed",
                "interest_rate": 23,
                "is_cumulative": true,
                "chased": true,
                "chasing_date": "2024-08-04",
                "invoice": 58,
                "chasing_rule_item": 3,
                "email_template": 1
            }
        ]
    }
}
```
