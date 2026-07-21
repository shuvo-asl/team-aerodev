# Create Group

**POST** `{{url}}/api/groups/`

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
    "name": "Super Test Admin",
    "permissions": [
        "add_group"
    ]
}
```

## Examples

### Create Group

**Request:** `POST` `{{url}}/api/groups/`

```json
{
    "name": "Super Test Admin",
    "permissions": [
        "add_group"
    ]
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "User Role successfully created",
    "data": {
        "result": {
            "id": 34,
            "name": "Super Test Admin"
        }
    }
}
```
