# invoice count

**GET** `{{url}}/api/dashboard/invoice-count/`

## Auth

Type: `bearer`

## Examples

### invoice count

**Request:** `GET` `{{url}}/api/dashboard/invoice-count/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice count fetched successfully",
    "data": {
        "result": {
            "paid": {
                "amount": 20,
                "count": 3
            },
            "sent": {
                "amount": 560,
                "count": 4
            },
            "overdue": {
                "amount": 1029.6,
                "count": 4
            }
        }
    }
}
```
