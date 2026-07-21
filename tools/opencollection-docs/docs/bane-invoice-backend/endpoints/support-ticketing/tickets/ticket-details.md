# ticket details

**GET** `{{url}}/api/tickets/TCK-00037/`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `` | `` | query |

## Headers

| Name | Value |
|---|---|
| `active_tab` | `mine` |

## Examples

### ticket details

**Request:** `GET` `{{url}}/api/tickets/TCK-00037/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Ticket Fetched Successfully",
    "data": {
        "result": {
            "reference_id": "TCK-00037",
            "issue_type": 1,
            "subject": "example subject",
            "status": "pending",
            "priority": "medium",
            "client": 19,
            "assigned_to": null,
            "created_at": "2025-05-18T15:47:28.246613+06:00",
            "issue_type_name": "Payment",
            "client_name": "AIR OP",
            "assigned_to_name": ""
        }
    }
}
```
