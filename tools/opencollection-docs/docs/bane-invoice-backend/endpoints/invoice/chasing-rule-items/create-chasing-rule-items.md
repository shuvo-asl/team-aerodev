# Create Chasing Rule Items

**POST** `{{url}}/api/chasing_rule_items/`

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
    "day": 7,
    "interest_rate": 5,
    "chasing_rule": 11,
    "email_template": 2,
    "interest_type": "fixed",
    "is_cumulative": false
}
```

## Examples

### Create Chasing Rule Items

**Request:** `POST` `{{url}}/api/chasing_rule_items/`

```json
{
    "day": 2,
    "interest_rate": 10.00,
    "chasing_rule": 2,
    "email_template": 1,
    "interest_type": "fixed",
    "is_cumulative": false
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Chasing Rule Items successfully created",
    "data": {
        "result": {
            "id": 9,
            "deleted_at": null,
            "created_at": "2024-09-01T11:31:33.681522+06:00",
            "updated_at": null,
            "day": 2,
            "interest_type": "fixed",
            "interest_rate": 10,
            "is_cumulative": false,
            "chasing_rule": 2,
            "email_template": 1
        }
    }
}
```
