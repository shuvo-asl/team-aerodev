# get chasing tasks

**GET** `{{url}}/api/chasing-tasks/?invoice_id=37`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `invoice_id` | `37` | query |

## Examples

### New Request

**Request:** `GET` `{{url}}/api/chasing-tasks/?invoice_id=37`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chasing Tasks Successfully Fetched",
    "data": {
        "result": [
            {
                "enabled": true,
                "id": 44,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 8,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 68,
                "chased": true,
                "chasing_date": "2025-01-27",
                "day": 9,
                "is_cumulative": false,
                "start_time": "2025-01-27"
            },
            {
                "enabled": true,
                "id": 56,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 11,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 38,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 14,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 32,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 20,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 62,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 26,
                "chased": false,
                "chasing_date": null,
                "day": 9,
                "is_cumulative": true,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 54,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 42,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 36,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 30,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 60,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 24,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": true,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 18,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 13,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 66,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 10,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 7,
                "chased": false,
                "chasing_date": null,
                "day": 5,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 4,
                "chased": false,
                "chasing_date": null,
                "day": 3,
                "is_cumulative": true,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 64,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 58,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 76,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 52,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 40,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 34,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 28,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 22,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": true,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 16,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 12,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 9,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            },
            {
                "enabled": true,
                "id": 6,
                "chased": false,
                "chasing_date": null,
                "day": 1,
                "is_cumulative": false,
                "start_time": null
            }
        ]
    }
}
```
