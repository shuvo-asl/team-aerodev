# Get Chasing Rule Items by rule id

**GET** `{{url}}/api/chasing_rule_items?limit=10&chasing_rule_id=2`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `10` | query |
| `page` | `1` | query |
| `chasing_rule_id` | `2` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Chasing Rule Items

**Request:** `GET` `{{url}}/api/chasing_rule_items/`

**Response:** `200 OK`

```json
{
    "success": true,
    "data": [
        {
            "id": 1,
            "day": 2,
            "interest_rate": 10,
            "schedule_type": "before_due",
            "chasing_rule_id": 1,
            "choose_template": 1
        }
    ]
}
```

### Get All Chasing Rule Items with pagination

**Request:** `GET` `{{url}}/api/chasing_rule_items?limit=2`

**Response:** `200 OK`

```json
{
    "success": true,
    "next": 2,
    "previous": null,
    "current_page": 1,
    "total_object": 3,
    "total_page": 2,
    "data": [
        {
            "id": 1,
            "day": 2,
            "interest_rate": 10,
            "schedule_type": "before_due",
            "chasing_rule_id": 1,
            "choose_template": 1
        },
        {
            "id": 2,
            "day": 2,
            "interest_rate": 10,
            "schedule_type": "before_due",
            "chasing_rule_id": 1,
            "choose_template": 1
        }
    ]
}
```
