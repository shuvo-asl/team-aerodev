# Invoice Chasing Histories

**GET** `{{url}}/api/invoice-chasing-history?invoice_id=33`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `2` | query |
| `invoice_id` | `33` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

## Examples

### Single Chasing Rule with Items

**Request:** `GET` `{{url}}/api/chasing_rule_details/1/`

**Response:** `200 OK`

```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "rule 1",
        "reminder_time": "12:00:00",
        "interest_calculate_time": "06:00:00",
        "calculate_interest_daily": false,
        "daily_interest_rate": 0,
        "default": true,
        "items": [
            {
                "id": 1,
                "day": 2,
                "interest_rate": 10,
                "schedule_type": "before_due",
                "chasing_rule_id": 1,
                "choose_template": 1
            },
            {
                "id": 2,
                "day": 2,
                "interest_rate": 10,
                "schedule_type": "before_due",
                "chasing_rule_id": 1,
                "choose_template": 1
            },
            {
                "id": 3,
                "day": 2,
                "interest_rate": 10,
                "schedule_type": "before_due",
                "chasing_rule_id": 1,
                "choose_template": 1
            }
        ]
    }
}
```
