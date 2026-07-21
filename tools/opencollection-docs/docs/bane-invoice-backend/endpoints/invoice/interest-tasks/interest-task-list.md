# interest task list

**GET** `{{url}}/api/interest-tasks/?invoice_id=172`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `invoice_id` | `172` | query |

## Examples

### New Request

**Request:** `GET` `{{url}}/api/interest-tasks/?invoice_id=172`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Interest Tasks Successfully Fetched",
    "data": {
        "result": {
            "invoice_no": "INV-000166",
            "id": 172,
            "issue_date": "2025-03-09",
            "due_date": "2025-03-11",
            "sent_date": "2025-03-09",
            "payment_status": "due",
            "status": "sent",
            "currency": "Afs",
            "interest_tasks": [
                {
                    "is_enabled": true,
                    "id": 16,
                    "is_calculated": false,
                    "interest_date": "2025-03-13",
                    "day": 2,
                    "is_cumulative": true,
                    "start_time": "2025-03-13T02:01:00"
                },
                {
                    "is_enabled": true,
                    "id": 17,
                    "is_calculated": false,
                    "interest_date": "2025-03-15",
                    "day": 2,
                    "is_cumulative": true,
                    "start_time": "2025-03-15T02:01:00"
                }
            ]
        }
    }
}
```
