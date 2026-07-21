# Update  Invoice Interest Schedule

**PATCH** `{{url}}/api/invoice-interest-schedule/2/`

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
    "interest_rate": 3.0,
    "interest_base": "invoice_amount_after_interest",
    "interest_rule": 1,
    "interest_day": 13
}
```

## Examples

### Update  Invoice Interest Schedule

**Request:** `PATCH` `{{url}}/api/invoice-interest-schedule/2/`

```json
{
    "invoice": 178,
    "name": "abcd",
    "is_cumulative": true,
    "max_repetition": 6,
    "interest_type": "fixed",
    "interest_rate": 3.0,
    "interest_base": "invoice_amount_after_interest",
    "interest_rule": 1,
    "interest_day": 13
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Interest Schedule successfully updated",
    "data": {
        "result": {
            "id": 2,
            "invoice": 178,
            "name": "abcd",
            "is_cumulative": true,
            "max_repetition": 6,
            "interest_type": "fixed",
            "interest_rate": 3,
            "interest_base": "invoice_amount_after_interest",
            "interest_rule": 1,
            "interest_day": 13
        }
    }
}
```
