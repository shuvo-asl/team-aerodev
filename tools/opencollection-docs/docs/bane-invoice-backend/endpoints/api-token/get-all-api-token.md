# get all api token

**GET** `{{url}}/api/api-token/?limit=2&page=1`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `2` | query |
| `page` | `1` | query |

## Examples

### New Request

**Request:** `GET` `{{url}}/api/api-token/?limit=2&page=1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "API Token Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 1,
        "total_page": 1,
        "result": [
            {
                "ip": "192.168.90.234",
                "token": "7bPu586pU01xQrsL",
                "is_active": false,
                "expires_at": "2025-02-22T11:27:02.303619+06:00",
                "id": 1
            }
        ]
    }
}
```
