# Single Chasing Rule

**GET** `{{url}}/api/chasing_rule/3`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Single Chasing Rule

**Request:** `GET` `{{url}}/api/chasing_rule/3`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chasing Rule Fetched Successfully",
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
