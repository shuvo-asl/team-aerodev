# Update Group

**PATCH** `{{url}}/api/groups/34/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
{
    "name":"Caab2",
    "permissions": [
       
    ]
}
```

## Examples

### Update Group

**Request:** `PATCH` `{{url}}/api/groups/34/`

```json
{
    "name":"Caab2",
    "permissions": [
       
    ]
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "User Role successfully updated",
    "data": {
        "result": {
            "id": 34,
            "name": "Caab2"
        }
    }
}
```
