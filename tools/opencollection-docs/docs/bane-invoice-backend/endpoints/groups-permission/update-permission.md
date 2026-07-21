# Update Permission

**PATCH** `{{url}}/api/permission/219/`

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
    "name": "Can View App Settings",
    "codename": "view_app_settings"    
}
```

## Examples

### Update Permission

**Request:** `PATCH` `{{url}}/api/permission/219/`

```json
{
    "name": "Can View App Settings",
    "codename": "view_app_settings"    
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Permission' Successfully Updated",
    "data": {
        "result": {
            "id": 219,
            "name": "Can View App Settings",
            "codename": "view_app_settings",
            "content_type": 15
        }
    }
}
```
