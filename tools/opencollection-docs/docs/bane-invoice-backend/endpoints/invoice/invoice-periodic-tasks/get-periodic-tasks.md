# get periodic tasks

**GET** `{{url}}/api/periodic-tasks/?invoice_id=18`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `invoice_id` | `18` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### get periodic tasks

**Request:** `GET` `{{url}}/api/periodic-tasks/?invoice_id=158`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Periodic Task Successfully Fetched",
    "data": {
        "result": {
            "invoice_no": "INV-000132",
            "id": 158,
            "issue_date": "2024-10-07",
            "due_date": "2024-10-22",
            "sent_date": "2024-10-09",
            "payment_status": "due",
            "status": "sent",
            "periodic_tasks": [
                {
                    "enabled": true,
                    "id": 17,
                    "start_time": "2024-10-30T00:01:00+06:00",
                    "day": 7,
                    "interest_type": "fixed",
                    "interest_rate": 5,
                    "is_cumulative": true,
                    "chased": false,
                    "chasing_date": "2024-10-30"
                },
                {
                    "enabled": true,
                    "id": 16,
                    "start_time": null,
                    "day": 7,
                    "interest_type": "fixed",
                    "interest_rate": 5,
                    "is_cumulative": false,
                    "chased": false,
                    "chasing_date": "2024-10-23"
                }
            ]
        }
    }
}
```
