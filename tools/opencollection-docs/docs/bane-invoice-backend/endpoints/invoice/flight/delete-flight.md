# delete Flight

**DELETE** `{{url}}/api/flight/57/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

## Examples

### delete Flight

**Request:** `DELETE` `{{url}}/api/flight/1/`

**Response:** `204 No Content`

```json
{
    "status": "success",
    "message": "Flight Successfully Deleted",
    "data": {
        "result": []
    }
}
```
