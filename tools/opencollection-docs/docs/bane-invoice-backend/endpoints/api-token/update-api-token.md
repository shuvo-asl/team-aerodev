# update api token

**PATCH** `{{url}}/api/api-token/1/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "is_active": false
}
```

## Examples

### New Request

**Request:** `PATCH` `{{url}}/api/api-token/1/`

```json
{
    "is_active": false
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "API Token successfully updated",
    "data": {
        "result": {
            "ip": "192.168.90.234",
            "token": "7bPu586pU01xQrsL",
            "is_active": false,
            "expires_at": "2025-02-22T11:27:02.303619+06:00",
            "id": 1
        }
    }
}
```
