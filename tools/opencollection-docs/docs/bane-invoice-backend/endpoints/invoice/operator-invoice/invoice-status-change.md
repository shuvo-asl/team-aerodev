# Invoice Status Change

**PATCH** `{{url}}/api/invoice-status-change/2/`

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
    "status": "approve"
}
```
