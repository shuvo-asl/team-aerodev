# enable disable interest task

**PATCH** `{{url}}/api/interest-tasks/172/16/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "is_enabled": true
}
```

## Examples

### New Request

**Request:** `PATCH` `{{url}}/api/interest-tasks/172/16/`

```json
{
    "is_enabled": true
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Interest Tasks successfully updated",
    "data": {
        "result": {
            "is_enabled": true,
            "id": 16,
            "is_calculated": false,
            "interest_date": "2025-03-13",
            "day": 2,
            "is_cumulative": true,
            "start_time": "2025-03-13T02:01:00"
        }
    }
}
```
