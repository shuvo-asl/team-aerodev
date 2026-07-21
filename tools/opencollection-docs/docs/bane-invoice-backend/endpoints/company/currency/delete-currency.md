# Delete Currency

**DELETE** `{{url}}/api/currency/2/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `text`

## Examples

### Delete Currency

**Request:** `DELETE` `{{url}}/api/currency/2/`

**Response:** `204 No Content`

```json
{
    "status": "success",
    "message": "Currency Successfully Deleted",
    "data": {
        "result": []
    }
}
```
