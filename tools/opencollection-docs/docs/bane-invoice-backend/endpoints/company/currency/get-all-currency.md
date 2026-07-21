# Get All Currency

**GET** `{{url}}/api/currency/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Currency

**Request:** `GET` `{{url}}/api/currency/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Currency Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 1,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:22+06:00",
                "updated_at": "2024-08-28T12:16:58.329984+06:00",
                "prefix": "$",
                "short_key": "eeee",
                "current_rate": 120,
                "default": true
            },
            {
                "id": 3,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:22.741709+06:00",
                "updated_at": null,
                "prefix": "$",
                "short_key": "BDT1",
                "current_rate": 1,
                "default": null
            },
            {
                "id": 4,
                "deleted_at": null,
                "created_at": "2024-08-20T10:38:22.741709+06:00",
                "updated_at": null,
                "prefix": "$",
                "short_key": "BDT2",
                "current_rate": 1,
                "default": null
            },
            {
                "id": 5,
                "deleted_at": null,
                "created_at": "2024-08-28T10:45:50+06:00",
                "updated_at": null,
                "prefix": "@",
                "short_key": "Dollar",
                "current_rate": 120,
                "default": null
            }
        ]
    }
}
```

### Get All Currency with pagination

**Request:** `GET` `{{url}}/api/currency/?limit=1&page=2`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Currency Successfully Fetched",
    "data": {
        "next": 3,
        "previous": 1,
        "current_page": 2,
        "total_object": 5,
        "total_page": 5,
        "result": [
            {
                "id": 5,
                "deleted_at": null,
                "created_at": "2024-08-28T10:45:50+06:00",
                "updated_at": null,
                "prefix": "@",
                "short_key": "Dollar",
                "current_rate": 120,
                "default": null
            }
        ]
    }
}
```
