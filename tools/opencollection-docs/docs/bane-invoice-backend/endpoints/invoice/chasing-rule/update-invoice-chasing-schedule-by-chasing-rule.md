# update invoice chasing schedule by chasing rule

**POST** `{{url}}/api/update-invoice-chasing-schedule-by-rule/`

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
    "invoice": 51,
    "new_chasing_rules": [22, 21]
}
```

## Examples

### Create Chasing Rule

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

### update invoice chasing schedule by chasing rule

**Request:** `POST` `{{url}}/api/update-invoice-chasing-schedule-by-rule/`

```json
{
    "invoice": 51,
    "new_chasing_rules": [22, 21]
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice Chasing Schedule' Successfully Created",
    "data": {
        "result": {}
    }
}
```
