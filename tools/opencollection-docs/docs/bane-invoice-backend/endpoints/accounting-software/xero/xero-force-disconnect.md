# Xero Force Disconnect

**POST** `{{url}}/api/xero/disconnect/`

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
    "accounting_software": "8",
    "force_disconnect": true
}
```
