# accounting software list

**GET** `{{url}}/api/accounting-software/?limit=10`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `10` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### accounting software list

**Request:** `GET` `{{url}}/api/accounting-software/?limit=10`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Accounting Software Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 1,
        "total_page": 1,
        "result": [
            {
                "id": 7,
                "name": "flow",
                "credentials": {
                    "api_secret": "very secret key"
                }
            }
        ]
    }
}
```
