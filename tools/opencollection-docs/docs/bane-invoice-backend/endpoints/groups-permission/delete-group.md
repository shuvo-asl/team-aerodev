# Delete Group

**DELETE** `{{url}}/api/groups/34/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

## Examples

### Delete Group

**Request:** `DELETE` `{{url}}/api/groups/34/`

**Response:** `204 No Content`

```json
{
    "status": "success",
    "message": "User Role Successfully Deleted",
    "data": {
        "result": []
    }
}
```
