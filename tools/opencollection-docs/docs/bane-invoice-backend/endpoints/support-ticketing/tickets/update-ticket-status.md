# update ticket status

**PATCH** `{{url}}/api/update-ticket-status/TCK-00014/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "status": "in_progress"
}
```

## Examples

### update ticket status

**Request:** `PATCH` `{{url}}/api/update-ticket-status/TCK-00014/`

```json
{
    "status": "in_progress"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Ticket's Status successfully updated",
    "data": {
        "result": {
            "status": "in_progress"
        }
    }
}
```
