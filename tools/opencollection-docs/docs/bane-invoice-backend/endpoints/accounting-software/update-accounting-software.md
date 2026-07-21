# update accounting software

**PATCH** `{{url}}/api/accounting-software/3/`

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
    "name": "xero",
    "credentials": 
    {
        "scope": "offline_access openid profile email accounting.transactions accounting.transactions.read accounting.reports.read accounting.journals.read accounting.settings accounting.settings.read accounting.contacts accounting.contacts.read accounting.attachments accounting.attachments.read assets projects files payroll.employees payroll.payruns payroll.payslip payroll.timesheets payroll.settings",
                "version": "2",
                "client_id": "978ABF64FCA2427D99EA034215AEFF3A",
                "endpoint_url": "https://api.xero.com/",
                "redirect_uri": "http://localhost:5011/api/xero/callback",
                "authorize_url": "https://login.xero.com/identity/connect/authorize",
                "client_secret": "GKVvQrGOXbEyucT5uzMhCFF4OZgTY9r_4-DyuFimbA72TrOe",
                "access_token_url": "https://identity.xero.com/connect/token",
                "refresh_token_url": "https://identity.xero.com/connect/token",
                "redirect_frontend_failed_url": "http://localhost:5173/app/accounting_software",
                "redirect_frontend_success_url": "http://localhost:5173/app/accounting_software"
        }
}
```

## Examples

### get accounting soft

**Request:** `GET` `{{url}}/api/accounting-software/4`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Accounting Software Fetched Successfully",
    "data": {
        "result": {
            "id": 4,
            "name": "xero",
            "credentials": {
                "client_id": "gAAAAABm1W2684UEdMOJRZPRELUaLVu97vAhQZmlW_Lo7CIAhKMOk0E1kq4xMlE15a5RNnW-xwsRoCEr2KBoFYWnsN96wHqVIQ=="
            }
        }
    }
}
```
