# Company Users

**GET** `{{url}}/api/company-users/?limit=4&page=1`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `4` | query |
| `page` | `1` | query |

## Examples

### Company Users

**Request:** `GET` `{{url}}/api/company-users/?limit=4&page=1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Company Users Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 22,
        "total_page": 6,
        "result": [
            {
                "email": "admin@gmail.com",
                "first_name": "Admin",
                "last_name": "admin",
                "profile_image": ""
            },
            {
                "email": "u16@gmail.com",
                "first_name": "first_name",
                "last_name": "last_name",
                "profile_image": ""
            },
            {
                "email": "u18@gmail.com",
                "first_name": "first_name",
                "last_name": "last_name",
                "profile_image": ""
            },
            {
                "email": "hgsgdf@gmail.com",
                "first_name": "Test",
                "last_name": "some",
                "profile_image": ""
            }
        ]
    }
}
```
