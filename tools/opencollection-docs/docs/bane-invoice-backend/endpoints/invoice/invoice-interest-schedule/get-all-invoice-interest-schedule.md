# Get All Invoice Interest Schedule

**GET** `{{url}}/api/invoice-interest-schedule?limit=10&page=1`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `10` | query |
| `page` | `1` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Invoice Interest Schedule

**Request:** `GET` `{{url}}/api/invoice-interest-schedule?limit=10&page=1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Interest Schedule Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 1,
        "total_page": 1,
        "result": [
            {
                "id": 1,
                "invoice": 178,
                "name": "abc",
                "is_cumulative": true,
                "max_repetition": 5,
                "interest_type": "fixed",
                "interest_rate": 10,
                "interest_base": "invoice_amount_after_interest",
                "interest_rule": null,
                "updated_at": null,
                "interest_day": 5
            }
        ]
    }
}
```
