# enable disable periodic tasks

**PATCH** `{{url}}/api/periodic-tasks/18/39/`

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
    "enabled": true
}
```

## Examples

### enable disable periodic tasks

**Request:** `PATCH` `{{url}}/api/periodic-tasks/18/`

```json
{
    "enabled": true
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Periodic Task successfully updated",
    "data": {
        "result": {
            "enabled": true,
            "id": 18,
            "start_time": "2024-03-25T00:01:00+06:00",
            "day": 1,
            "interest_type": "fixed",
            "interest_rate": 23,
            "is_cumulative": true,
            "chased": false,
            "chasing_date": "2024-03-25"
        }
    }
}
```
