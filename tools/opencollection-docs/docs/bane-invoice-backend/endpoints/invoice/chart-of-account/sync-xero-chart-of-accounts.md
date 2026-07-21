# Sync Xero Chart of accounts

**PATCH** `{{url}}/api/xero/sync-coa/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

## Examples

### Sync Xero Chart of accounts

**Request:** `PATCH` `{{url}}/api/xero/sync-coa/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chart of Accounts Synced Successfully",
    "data": {
        "result": {
            "number_of_updated_coa": 53,
            "number_of_created_coa": 0
        }
    }
}
```
