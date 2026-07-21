# get single api token

**GET** `{{url}}/api/api-token/1`

## Auth

Type: `bearer`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/api-token/1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "API Token Fetched Successfully",
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
