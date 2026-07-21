# Create Chasing Rule

**POST** `{{url}}/api/chasing_rule/`

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
    "name": "rule1",
    "chase_on": "after due date",
    "is_cumulative": false,
    "chasing_days": [3, 5, 9],
    "email_template": 1

}
```

## Examples

### Create Chasing Rule

**Request:** `POST` `{{url}}/api/chasing_rule/`

```json
{
    "name": "rule1",
    "chase_on": "after due date",
    "is_cumulative": false,
    "chasing_days": [3, 5, 9],
    "email_template": 1

}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Chasing Rule successfully created",
    "data": {
        "result": {
            "id": 3,
            "name": "rule1",
            "is_default": false,
            "chase_on": "after due date",
            "is_cumulative": false,
            "max_repetition": null,
            "email_template": 1,
            "email_template_name": "example email template",
            "chasing_days": [
                9,
                5,
                3
            ]
        }
    }
}
```
