# Update Chasing Rule Items

**PATCH** `{{url}}/api/chasing_rule_items/9/`

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
    "day": 3,
    "interest_rate": 10.00,
    "chasing_rule": 2,
    "email_template": 1,
    "interest_type": "fixed",
    "is_cumulative": false
}
```

## Examples

### Update Chasing Rule Items

**Request:** `PATCH` `{{url}}/api/chasing_rule_items/9/`

```json
{
    "day": 3,
    "interest_rate": 10.00,
    "chasing_rule": 2,
    "email_template": 1,
    "interest_type": "fixed",
    "is_cumulative": false
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chasing Rule Items successfully updated",
    "data": {
        "result": {
            "id": 9,
            "deleted_at": null,
            "created_at": "2024-09-01T11:31:33.681522+06:00",
            "updated_at": "2024-09-01T11:32:15.014500+06:00",
            "day": 3,
            "interest_type": "fixed",
            "interest_rate": 10,
            "is_cumulative": false,
            "chasing_rule": 2,
            "email_template": 1
        }
    }
}
```
