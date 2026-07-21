# Sync Xero Bank Accounts

**PATCH** `{{url}}/api/xero/sync-bank-accounts/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

## Examples

### Sync Xero Chart of accounts Copy

**Request:** `PATCH` `{{url}}/api/xero/sync-bank-accounts/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Bank Accounts Synced Successfully",
    "data": {
        "result": {
            "number_of_updated_bank_accounts": 9,
            "number_of_created_bank_accounts": 0
        }
    }
}
```
