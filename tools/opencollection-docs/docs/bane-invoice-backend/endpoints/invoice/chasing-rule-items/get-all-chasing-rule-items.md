# Get All Chasing Rule Items

**GET** `{{url}}/api/chasing_rule_items`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `10` | query |
| `page` | `1` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Chasing Rule Items

**Request:** `GET` `{{url}}/api/chasing_rule_items`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chasing Rule Items Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 2,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 3,
                "interest_type": "fixed",
                "interest_rate": 21,
                "is_cumulative": false,
                "chasing_rule": 2,
                "email_template": 1
            },
            {
                "id": 3,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 15,
                "interest_type": "fixed",
                "interest_rate": 23,
                "is_cumulative": true,
                "chasing_rule": 2,
                "email_template": 1
            },
            {
                "id": 4,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 5,
                "interest_type": "percentage",
                "interest_rate": 2,
                "is_cumulative": false,
                "chasing_rule": 3,
                "email_template": 2
            },
            {
                "id": 5,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 10,
                "interest_type": "percentage",
                "interest_rate": 5,
                "is_cumulative": false,
                "chasing_rule": 3,
                "email_template": 3
            },
            {
                "id": 6,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 30,
                "interest_type": "percentage",
                "interest_rate": 5,
                "is_cumulative": true,
                "chasing_rule": 3,
                "email_template": 2
            }
        ]
    }
}
```

### Get All Chasing Rule Items with pagination

**Request:** `GET` `{{url}}/api/chasing_rule_items?limit=10&page=1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chasing Rule Items Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 5,
        "total_page": 1,
        "result": [
            {
                "id": 2,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 3,
                "interest_type": "fixed",
                "interest_rate": 21,
                "is_cumulative": false,
                "chasing_rule": 2,
                "email_template": 1
            },
            {
                "id": 3,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 15,
                "interest_type": "fixed",
                "interest_rate": 23,
                "is_cumulative": true,
                "chasing_rule": 2,
                "email_template": 1
            },
            {
                "id": 4,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 5,
                "interest_type": "percentage",
                "interest_rate": 2,
                "is_cumulative": false,
                "chasing_rule": 3,
                "email_template": 2
            },
            {
                "id": 5,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 10,
                "interest_type": "percentage",
                "interest_rate": 5,
                "is_cumulative": false,
                "chasing_rule": 3,
                "email_template": 3
            },
            {
                "id": 6,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:23.838066+06:00",
                "updated_at": null,
                "day": 30,
                "interest_type": "percentage",
                "interest_rate": 5,
                "is_cumulative": true,
                "chasing_rule": 3,
                "email_template": 2
            }
        ]
    }
}
```
