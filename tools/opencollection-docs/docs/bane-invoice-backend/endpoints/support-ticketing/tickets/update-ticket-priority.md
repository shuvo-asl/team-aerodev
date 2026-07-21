# update ticket priority

**PATCH** `{{url}}/api/update-ticket-priority/TCK-00014/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "priority": "critical"
}
```

## Examples

### update ticket priority

**Request:** `PATCH` `{{url}}/api/update-ticket-priority/TCK-00014/`

```json
{
    "priority": "critical"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Ticket's Priority successfully updated",
    "data": {
        "result": {
            "priority": "critical"
        }
    }
}
```
