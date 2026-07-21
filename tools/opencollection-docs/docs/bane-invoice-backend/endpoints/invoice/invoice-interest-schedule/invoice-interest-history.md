# invoice interest history

**GET** `{{url}}/api/invoice-interest-history/168/`

## Auth

Type: `bearer`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/invoice-interest-history/168/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Interest History Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 2,
                "invoice": 168,
                "invoice_interest_schedule": {
                    "id": 8,
                    "invoice": 168,
                    "name": "proper rule",
                    "is_cumulative": true,
                    "max_repetition": 2,
                    "interest_type": "fixed",
                    "interest_rate": 23,
                    "interest_base": "invoice_amount_after_interest",
                    "interest_rule": 11,
                    "start_day": 2,
                    "custom": true,
                    "interest_day": 2
                },
                "interest_amount": 23,
                "previous_amount": 1020,
                "current_amount": 1043,
                "payable_amount": 1043,
                "tax_amount": 0,
                "exchange_rate": null,
                "created_at": "2025-03-17T11:19:13.162436+06:00"
            }
        ]
    }
}
```
