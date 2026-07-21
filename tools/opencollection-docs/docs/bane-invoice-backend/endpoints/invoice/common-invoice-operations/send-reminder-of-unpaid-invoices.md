# send reminder of unpaid invoices

**POST** `{{url}}/api/send-reminder-of-unpaid-invoices/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "client": 30,
    "invoices": [249, 250]
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/send-reminder-of-unpaid-invoices/`

```json
{
    "client": 30,
    "invoices": [249, 250]
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Reminder sent to client successfully",
    "data": {
        "result": {}
    }
}
```
