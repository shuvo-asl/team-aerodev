# revenue-trends

**GET** `{{url}}/api/revenue-trends`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### revenue-trends

**Request:** `GET` `{{url}}/api/revenue-trends`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Revenue Trends",
    "data": {
        "result": {
            "weekly_revenue": [
                {
                    "date": "2024-10-16",
                    "amount": 294
                },
                {
                    "date": "2024-10-17",
                    "amount": 623.28
                },
                {
                    "date": "2024-10-20",
                    "amount": 337.5
                },
                {
                    "date": "2024-10-21",
                    "amount": 59.6
                },
                {
                    "date": "2024-10-22",
                    "amount": 528
                },
                {
                    "date": "2024-10-23",
                    "amount": 199
                },
                {
                    "date": "2024-10-28",
                    "amount": 799.56
                },
                {
                    "date": "2024-10-29",
                    "amount": 86
                },
                {
                    "date": "2024-10-31",
                    "amount": 301
                },
                {
                    "date": "2024-11-03",
                    "amount": 14
                },
                {
                    "date": "2024-11-04",
                    "amount": 49
                },
                {
                    "date": "2024-11-12",
                    "amount": 259.8
                }
            ]
        }
    }
}
```
