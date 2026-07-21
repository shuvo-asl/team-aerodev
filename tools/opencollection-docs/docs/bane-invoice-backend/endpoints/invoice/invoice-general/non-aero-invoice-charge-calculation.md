# Non-Aero Invoice Charge Calculation

**POST** `{{url}}/api/invoice-charge/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
{
    "invoice_item_type": "non_aeronautical",
    "items":[
        {
            "id": 453,
            "description": "dsafsdf",
            "units": "15",
            "per_unit_cost": "10"
        }
    ],
    "new_items": [
        {
            "description": "dsafsdf",
            "units": "5",
            "per_unit_cost": "2"
        }
    ],
    "deleted_items": [454]
}
```

## Examples

### Non-Aero Invoice Charge Calculation

**Request:** `POST` `{{url}}/api/invoice-charge/`

```json
{
    "invoice_item_type": "non_aeronautical",
    "items":[
        {
            "id": 453,
            "coa": 1,
            "description": "dsafsdf",
            "units": "15",
            "per_unit_cost": "10"
        }
    ],
    "new_items": [
        {
            "coa": 1,
            "description": "dsafsdf",
            "units": "5",
            "per_unit_cost": "2"
        }
    ],
    "deleted_items": [454]
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice' Charge Calculation Updated",
    "data": {
        "result": {
            "total_amount": 160,
            "invoice_item_type": "non_aeronautical",
            "items": [
                {
                    "id": 453,
                    "coa": 1,
                    "description": "dsafsdf",
                    "units": "15",
                    "per_unit_cost": "10",
                    "amount": 150
                }
            ],
            "new_items": [
                {
                    "coa": 1,
                    "description": "dsafsdf",
                    "units": "5",
                    "per_unit_cost": "2",
                    "amount": 10
                }
            ],
            "deleted_items": [
                454
            ]
        }
    }
}
```
