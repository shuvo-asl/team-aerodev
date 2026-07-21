# Get All Invoice Chasing Schedule

**GET** `{{url}}/api/invoice-chasing-schedule?limit=10&page=1`

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

### Get All Invoice Chasing Schedule

**Request:** `GET` `{{url}}/api/invoice-chasing-schedule?limit=10&page=1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Chasing Schedule Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 22,
        "total_page": 3,
        "result": [
            {
                "id": 3,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 3,
                "interest_type": "fixed",
                "interest_rate": 21,
                "is_cumulative": false,
                "chased": false,
                "chasing_date": null,
                "invoice": 36,
                "chasing_rule_item": 2,
                "email_template": 1
            },
            {
                "id": 4,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 15,
                "interest_type": "fixed",
                "interest_rate": 23,
                "is_cumulative": true,
                "chased": false,
                "chasing_date": null,
                "invoice": 36,
                "chasing_rule_item": 3,
                "email_template": 1
            },
            {
                "id": 12,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 5,
                "interest_type": "percentage",
                "interest_rate": 2,
                "is_cumulative": false,
                "chased": false,
                "chasing_date": "2024-07-27",
                "invoice": 42,
                "chasing_rule_item": 4,
                "email_template": 2
            },
            {
                "id": 13,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 10,
                "interest_type": "percentage",
                "interest_rate": 5,
                "is_cumulative": false,
                "chased": true,
                "chasing_date": "2024-08-01",
                "invoice": 42,
                "chasing_rule_item": 5,
                "email_template": 3
            },
            {
                "id": 14,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 30,
                "interest_type": "percentage",
                "interest_rate": 5,
                "is_cumulative": true,
                "chased": true,
                "chasing_date": "2024-08-11",
                "invoice": 42,
                "chasing_rule_item": 6,
                "email_template": 2
            },
            {
                "id": 18,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 5,
                "interest_type": "percentage",
                "interest_rate": 2,
                "is_cumulative": false,
                "chased": false,
                "chasing_date": null,
                "invoice": 44,
                "chasing_rule_item": 4,
                "email_template": 2
            },
            {
                "id": 19,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 10,
                "interest_type": "percentage",
                "interest_rate": 5,
                "is_cumulative": false,
                "chased": false,
                "chasing_date": null,
                "invoice": 44,
                "chasing_rule_item": 5,
                "email_template": 3
            },
            {
                "id": 20,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 30,
                "interest_type": "percentage",
                "interest_rate": 5,
                "is_cumulative": true,
                "chased": false,
                "chasing_date": null,
                "invoice": 44,
                "chasing_rule_item": 6,
                "email_template": 2
            },
            {
                "id": 41,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 3,
                "interest_type": "fixed",
                "interest_rate": 21,
                "is_cumulative": false,
                "chased": false,
                "chasing_date": null,
                "invoice": 53,
                "chasing_rule_item": 2,
                "email_template": 1
            },
            {
                "id": 42,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:24.742220+06:00",
                "updated_at": null,
                "day": 15,
                "interest_type": "fixed",
                "interest_rate": 23,
                "is_cumulative": true,
                "chased": false,
                "chasing_date": null,
                "invoice": 53,
                "chasing_rule_item": 3,
                "email_template": 1
            }
        ]
    }
}
```
