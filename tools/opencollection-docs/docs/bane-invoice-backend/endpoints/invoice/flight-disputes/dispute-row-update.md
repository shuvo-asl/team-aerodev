# dispute row update

**PATCH** `{{url}}/api/dispute-flights/{{dispute_row_id}}/`

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
    "note": "Client acknowledged--"
}
```
