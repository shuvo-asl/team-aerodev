# void invoice

**DELETE** `{{url}}/api/invoice/50/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

## Examples

### void invoice

**Request:** `DELETE` `{{url}}/api/invoice/50/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice' Successfully Deleted",
    "data": {
        "result": []
    }
}
```
