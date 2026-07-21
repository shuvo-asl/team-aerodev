# Get All Client

**GET** `{{url}}/api/client/?all=True`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `all` | `True` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Client

**Request:** `GET` `{{url}}/api/client/?limit=5`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Client Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 15,
        "total_page": 3,
        "result": [
            {
                "id": 2,
                "name": "test",
                "short_code": "heu45",
                "email": "client@gmail.com",
                "phone": "0898897987",
                "billing_address": "jdhfj,jdweoij",
                "days_to_due_date": 14,
                "client_type": "operator",
                "preferred_currency": null
            },
            {
                "id": 3,
                "name": "Harry",
                "short_code": "jfhfif",
                "email": "harry@gmail.com",
                "phone": "786789e9234",
                "billing_address": "fjkg.fherofuire",
                "days_to_due_date": 14,
                "client_type": "general",
                "preferred_currency": null
            },
            {
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
            },
            {
                "id": 5,
                "name": "sam",
                "short_code": "dnlgjkfg",
                "email": "admin@gmail.com",
                "phone": "75r89747",
                "billing_address": "khsjdhfcjf",
                "days_to_due_date": 14,
                "client_type": "agent",
                "preferred_currency": {
                    "id": 2,
                    "prefix": "$",
                    "short_key": "taka",
                    "current_rate": 0,
                    "default": null
                }
            },
            {
                "id": 6,
                "name": "marry",
                "short_code": "dfghefuie",
                "email": "marjhe@gmail.com",
                "phone": "4875983475",
                "billing_address": "oijejhofc,fjorif",
                "days_to_due_date": 14,
                "client_type": "general",
                "preferred_currency": null
            }
        ]
    }
}
```
