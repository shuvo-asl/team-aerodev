# yearly revenue

**GET** `{{url}}/api/dashboard/revenue-data/?type=yearly`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `type` | `yearly` | query |

## Body

Type: `text`

```
{
    "email": "admin@gmail.com",
    "password": "admin@123",
    "user_type": "asl"
}
```

## Examples

### yearly revenue

**Request:** `GET` `{{url}}/api/dashboard/revenue-data/?type=yearly`

```json
{
    "email": "admin@gmail.com",
    "password": "admin@123",
    "user_type": "asl"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Yearly Revenue successfully fetched",
    "data": {
        "result": {
            "January": {
                "paid": 0,
                "sent": 0
            },
            "February": {
                "paid": 0,
                "sent": 0
            },
            "March": {
                "paid": 0,
                "sent": 0
            },
            "April": {
                "paid": 0,
                "sent": 0
            },
            "May": {
                "paid": 0,
                "sent": 0
            },
            "June": {
                "paid": 0,
                "sent": 0
            },
            "July": {
                "paid": 0,
                "sent": 0
            },
            "August": {
                "paid": 0,
                "sent": 0
            },
            "September": {
                "paid": 0,
                "sent": 0
            },
            "October": {
                "paid": 0,
                "sent": 0
            },
            "November": {
                "paid": 20,
                "sent": 560
            },
            "December": {
                "paid": 0,
                "sent": 0
            }
        }
    }
}
```
