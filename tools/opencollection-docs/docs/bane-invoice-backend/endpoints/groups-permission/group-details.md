# group details

**GET** `{{url}}/api/groups/33`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### group details

**Request:** `GET` `{{url}}/api/groups/33`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "User Role Fetched Successfully",
    "data": {
        "result": {
            "id": 33,
            "name": "Super Admin jhgeg",
            "permissions": [
                {
                    "id": 9,
                    "name": "Can add group",
                    "codename": "add_group",
                    "content_type": 3
                }
            ]
        }
    }
}
```
