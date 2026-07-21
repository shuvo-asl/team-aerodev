# charges based on rules

**GET** `{{url}}/api/charges-based-on-rules/11/`

## Auth

Type: `bearer`

## Examples

### charges based on rules

**Request:** `GET` `{{url}}/api/charges-based-on-rules/11/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Charges based o rules fetched successfully",
    "data": {
        "result": [
            {
                "max_value": "2 Hour",
                "min": "0.0 Hour",
                "max": "99999.0 Hour",
                "local_cost": "",
                "international_cost": "100.0$ / 1 Hour",
                "static_cost": ""
            },
            {
                "max_value": "2 Hour",
                "min": "100000.0 Hour",
                "max": "199999.0 Hour",
                "local_cost": "",
                "international_cost": "150.0$ / 1 Hour",
                "static_cost": ""
            },
            {
                "max_value": "2 Hour",
                "min": "200000.0 Hour",
                "max": "299999.0 Hour",
                "local_cost": "",
                "international_cost": "200.0$ / 1 Hour",
                "static_cost": ""
            },
            {
                "max_value": "2 Hour",
                "min": "300000.0 Hour",
                "max": "",
                "local_cost": "",
                "international_cost": "250.0$ / 1 Hour",
                "static_cost": ""
            }
        ]
    }
}
```
