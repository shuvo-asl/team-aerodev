# update exchange rate

**PATCH** `{{url}}/api/update-exchange-rate/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### update exchange rate

**Request:** `PATCH` `{{url}}/api/update-exchange-rate/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Exchange rate is being updated..",
    "data": {
        "result": {}
    }
}
```
