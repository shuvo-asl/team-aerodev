# enable disable chasing task

**PATCH** `{{url}}/api/chasing-tasks/37/44/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "enabled": true
}
```

## Examples

### enable disable chasing task

**Request:** `PATCH` `{{url}}/api/chasing-tasks/37/44/`

```json
{
    "enabled": true
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chasing Tasks successfully updated",
    "data": {
        "result": {
            "enabled": true,
            "id": 44,
            "chased": false,
            "chasing_date": null,
            "day": 9,
            "is_cumulative": false,
            "start_time": null
        }
    }
}
```
