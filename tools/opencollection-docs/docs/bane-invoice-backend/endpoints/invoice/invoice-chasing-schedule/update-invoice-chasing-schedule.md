# Update  Invoice Chasing Schedule

**PATCH** `{{url}}/api/invoice-chasing-schedule/5/`

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
    "invoice": 11,
    "chase_on": "after due date",
    "is_cumulative": true,
    "chasing_days": [3],
    "email_template": 1,
    "name": "sample name3",
    "max_repetition": 5
}
```

## Examples

### Update  Invoice Chasing Schedule

**Request:** `PATCH` `{{url}}/api/invoice-chasing-schedule/2/`

```json
{
    "invoice": 33,
    "day": 14,
    "interest_type": "fixed",
    "interest_rate": 10,
    "email_template": 1
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Chasing Schedule successfully updated",
    "data": {
        "result": {
            "id": 2,
            "deleted_at": null,
            "created_at": "2024-09-01T21:41:35.122610+06:00",
            "updated_at": "2024-09-01T21:42:16.039878+06:00",
            "day": 14,
            "interest_type": "fixed",
            "interest_rate": 10,
            "is_cumulative": false,
            "chased": false,
            "chasing_date": null,
            "invoice": 33,
            "chasing_rule_item": null,
            "email_template": 1
        }
    }
}
```
