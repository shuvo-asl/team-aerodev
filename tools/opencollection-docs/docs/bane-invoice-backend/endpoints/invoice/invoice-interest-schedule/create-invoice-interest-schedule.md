# Create  Invoice Interest Schedule

**POST** `{{url}}/api/invoice-interest-schedule/`

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
    "invoice": 178,
    "name": "abcd",
    "is_cumulative": true,
    "max_repetition": 6,
    "interest_type": "fixed",
    "interest_rate": 3,
    "interest_base": "invoice_amount_after_interest",
    "interest_day": 10
}
```

## Examples

### Create  Invoice Chasing Schedule

**Request:** `POST` `{{url}}/api/invoice-chasing-schedule/`

```json
{
    "invoice": 11,
    "chase_on": "after due date",
    "is_cumulative": true,
    "chasing_days": [3],
    "email_template": 1,
    "name": "sample name3",
    "max_repetition": 4
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Invoice Chasing Schedule successfully created",
    "data": {
        "result": {
            "id": 5,
            "invoice": 11,
            "name": "sample name3",
            "chase_on": "after due date",
            "is_cumulative": true,
            "max_repetition": 4,
            "email_template": 1,
            "email_template_name": "default",
            "updated_at": null,
            "chasing_rule": 7,
            "custom": false,
            "chasing_days": [
                3
            ]
        }
    }
}
```
