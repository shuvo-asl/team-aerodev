# company list

**GET** `{{url}}/api/companies/`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `page` | `2` | query |
| `limit` | `1` | query |

## Examples

### company list

**Request:** `GET` `{{url}}/api/company-list/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Company Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "name": "Boring Company",
                "is_active": true,
                "is_primary": false
            },
            {
                "id": 2,
                "name": "kamrul",
                "is_active": true,
                "is_primary": true
            }
        ]
    }
}
```
