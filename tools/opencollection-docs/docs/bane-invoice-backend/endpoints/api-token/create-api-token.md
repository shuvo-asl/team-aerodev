# create api token

**POST** `{{url}}/api/api-token/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "ip": "localhost",
    "validity_in_days": 30
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/api-token/`

```json
{
    "ip": "192.168.90.234",
    "validity_in_days": 23
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "API Token successfully created",
    "data": {
        "result": {
            "ip": "192.168.90.234",
            "token": "7bPu586pU01xQrsL",
            "is_active": true,
            "expires_at": "2025-02-22T11:27:02.303619+06:00"
        }
    }
}
```
