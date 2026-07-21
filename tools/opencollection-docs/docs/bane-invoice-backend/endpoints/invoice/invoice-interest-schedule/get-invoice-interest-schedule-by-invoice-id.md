# Get Invoice Interest Schedule by invoice id

**GET** `{{url}}/api/invoice-interest-schedule?invoice_id=178`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `invoice_id` | `178` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get Invoice Interest Schedule by invoice id

**Request:** `GET` `{{url}}/api/invoice-interest-schedule?invoice_id=178`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Interest Schedule Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "invoice": 178,
                "name": "abc",
                "is_cumulative": true,
                "max_repetition": 5,
                "interest_type": "fixed",
                "interest_rate": 10,
                "interest_base": "invoice_amount_after_interest",
                "interest_rule": null,
                "updated_at": null,
                "interest_day": 5
            }
        ]
    }
}
```
