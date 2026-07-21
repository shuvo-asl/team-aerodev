# get all groups

**GET** `{{url}}/api/groups?limit=5`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `5` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### get all groups

**Request:** `GET` `{{url}}/api/groups?limit=5`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "User Role Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 8,
        "total_page": 2,
        "result": [
            {
                "id": 33,
                "name": "Super Admin jhgeg"
            },
            {
                "id": 31,
                "name": "ghfh"
            },
            {
                "id": 12,
                "name": "abcd"
            },
            {
                "id": 11,
                "name": "abc"
            },
            {
                "id": 10,
                "name": "test_admin"
            }
        ]
    }
}
```
