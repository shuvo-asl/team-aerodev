# ticket list

**GET** `{{url}}/api/tickets/?active_tab=mine&status=pending&created_at=2025-05-14&search=28&page=1&limit=2`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `active_tab` | `mine` | query |
| `status` | `pending` | query |
| `created_at` | `2025-05-14` | query |
| `search` | `28` | query |
| `page` | `1` | query |
| `limit` | `2` | query |

## Examples

### ticket list

**Request:** `GET` `{{url}}/api/tickets/?active_tab=mine&status=pending&created_at=2025-05-14&search=28&page=1&limit=2`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Ticket Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 1,
        "total_page": 1,
        "result": [
            {
                "reference_id": "TCK-00028",
                "subject": "example subject",
                "priority": "medium",
                "created_at": "2025-05-14T15:27:27.559132+06:00",
                "issue_type": "Payment",
                "status": "pending",
                "id": 28
            }
        ],
        "status_counts": {
            "pending": 8,
            "in_progress": 2,
            "resolved": 0,
            "closed": 0,
            "discarded": 0,
            "all_tickets": 18,
            "my_tickets": 10
        }
    }
}
```
