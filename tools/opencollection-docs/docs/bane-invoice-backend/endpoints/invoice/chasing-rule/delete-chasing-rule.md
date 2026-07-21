# delete Chasing Rule

**DELETE** `{{url}}/api/chasing_rule/5/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

## Examples

### delete Chasing Rule

**Request:** `DELETE` `{{url}}/api/chasing_rule/4/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Chasing Rule' Successfully Deleted",
    "data": {
        "result": []
    }
}
```
