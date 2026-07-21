# Get Single client

**GET** `{{url}}/api/client/2/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get Single client

**Request:** `GET` `{{url}}/api/client/4/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Client Fetched Successfully",
    "data": {
        "result": {
            "id": 4,
            "name": "ron",
            "short_code": "fdgouitjg",
            "email": "dfiuhei@gmail.com",
            "phone": "73486573847",
            "billing_address": "hvjdfg",
            "days_to_due_date": 14,
            "client_type": "operator",
            "preferred_currency": {
                "id": 4,
                "prefix": "$",
                "short_key": "BDD",
                "current_rate": 0,
                "default": null
            }
        }
    }
}
```
