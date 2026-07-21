# assign user to ticket

**POST** `{{url}}/api/assign-user-to-ticket/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "ticket_id": "TCK-00014",
    "user_id": 1
}
```

## Examples

### assign user to ticket

**Request:** `POST` `{{url}}/api/assign-user-to-ticket/`

```json
{
    "ticket_id": "TCK-00014",
    "user_id": 1
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Ticket assigned successfully",
    "data": {
        "result": {}
    }
}
```
