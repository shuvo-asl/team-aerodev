# delete Email Template

**DELETE** `{{url}}/api/email_template/2/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

## Examples

### delete Email Template

**Request:** `DELETE` `{{url}}/api/email_template/2/`

**Response:** `204 No Content`

```json
{
    "status": "success",
    "message": "Email Template Successfully Deleted",
    "data": {
        "result": []
    }
}
```
