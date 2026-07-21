# Create Permission

**POST** `{{url}}/api/permission/`

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
    "name": "Can Update App Settings",
    "codename": "update_nothing"    
}
```

## Examples

### Create Permission

**Request:** `POST` `{{url}}/api/permission/`

```json
{
    "name": "Can Update App Settings",
    "codename": "update_nothing"    
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Permission' Successfully Created",
    "data": {
        "result": {
            "id": 219,
            "name": "Can Update App Settings",
            "codename": "update_nothing",
            "content_type": 15
        }
    }
}
```
