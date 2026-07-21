# flight count by status

**GET** `{{url}}/api/flight-count-by-status/`

## Auth

Type: `bearer`

## Body

Type: `text`

```
{
    "email": "kamrul@asl.aero",
    "password": "kamrul@123",
    "user_type": "operator"
}
```

## Examples

### flight count by status

**Request:** `GET` `{{url}}/api/flight-count-by-status/`

```json
{
    "email": "kamrul@asl.aero",
    "password": "kamrul@123",
    "user_type": "operator"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Flight count retrieved successfully",
    "data": {
        "result": {
            "incomplete": 281,
            "ready_to_bill": 33,
            "billing": 5
        }
    }
}
```
