# Get All Chasing Rule

**GET** `{{url}}/api/chasing_rule`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `10` | query |
| `page` | `2` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Chasing Rule

**Request:** `GET` `{{url}}/api/chasing_rule`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chasing Rule Successfully Fetched",
    "data": {
        "result": [
            {
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
            },
            {
                "id": 1,
                "name": "fixed interest",
                "is_default": false,
                "chase_on": "after due date",
                "is_cumulative": true,
                "max_repetition": null,
                "email_template": null,
                "chasing_days": []
            }
        ]
    }
}
```
