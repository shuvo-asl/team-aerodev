# Xero Connect

**GET** `{{url}}/api/xero/connect?accounting_software=5`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `accounting_software` | `5` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Xero Connect

**Request:** `GET` `{{url}}/api/xero/connect`

**Response:** `200 OK`

```json
{
    "success": true,
    "authorization_url": "https://login.xero.com/identity/connect/authorize?response_type=code&client_id=65C6B0BBEE03432EB52AAA51C6F78342&redirect_uri=http%3A%2F%2Flocalhost%3A5011%2Fapi%2Fxero%2Fcallback&scope=offline_access+openid+profile+email+accounting.transactions+accounting.transactions.read+accounting.reports.read+accounting.journals.read+accounting.settings+accounting.settings.read+accounting.contacts+accounting.contacts.read+accounting.attachments+accounting.attachments.read+assets+projects+files+payroll.employees+payroll.payruns+payroll.payslip+payroll.timesheets+payroll.settings&state=l8DhExraQvfI5IIZoVor5mtLccvofM&nonce=pVcNp2BUKVEPFlNfjrKv"
}
```
