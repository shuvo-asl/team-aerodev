# Create Invoice

**POST** `{{url}}/api/operator/invoice/`

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
    "operator": 1,
    "billing_flight": 2, 
    "currency": 1
}
```

## Examples

### Create Operator Invoice

**Request:** `POST` `{{url}}/api/chasing_rule/`

```json
{
    "name": "rule 1",
    "reminder_time": "12:00:00",
    "interest_calculate_time": "06:00:00",
    "default": true
}
```

**Response:** `201 Created`

```json
{
    "success": true,
    "data": {
        "id": 1,
        "name": "rule 1",
        "reminder_time": "12:00:00",
        "interest_calculate_time": "06:00:00",
        "calculate_interest_daily": false,
        "daily_interest_rate": 0,
        "default": true
    }
}
```
