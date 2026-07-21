# create accounting software

**POST** `{{url}}/api/accounting-software/`

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
    "name": "test_soft2",
    "accounting_software_type": 1,
    "credentials": 
    {
        "version":"2",
        "client_id":"65C6B0BBEE03432EB52AAA51C6F78342",
        "client_secret":"Y-t5WLOY-YH5qDqwq4osPGi_qwmeGxoXTdNYuUq_Vs6X8_mZ",
        "endpoint_url":"https://api.xero.com/",
        "authorize_url":"https://login.xero.com/identity/connect/authorize",
        "access_token_url":"https://identity.xero.com/connect/token",
        "refresh_token_url":"https://identity.xero.com/connect/token",
        "scope":"offline_access openid profile email accounting.transactions accounting.transactions.read accounting.reports.read accounting.journals.read accounting.settings accounting.settings.read accounting.contacts accounting.contacts.read accounting.attachments accounting.attachments.read assets projects files payroll.employees payroll.payruns payroll.payslip payroll.timesheets payroll.settings",
        "redirect_uri": "http://localhost:5011/api/xero/callback",
        "redirect_frontend_success_url": "http://localhost:3000/success",
        "redirect_frontend_failed_url": "http://localhost:3000/failed"
        }
}
```

## Examples

### get accounting software Copy

**Request:** `POST` `{{url}}/api/accounting-software/`

```json
{
    "name": "flow",
    "credentials": {"api_secret": "very secret key"}
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Accounting Software successfully created",
    "data": {
        "result": {
            "id": 7,
            "name": "flow",
            "credentials": {
                "api_secret": "very secret key"
            }
        }
    }
}
```

### create accounting software

**Request:** `POST` `{{url}}/api/accounting-software/`

```json
{
    "name": "test_soft2",
    "accounting_software_type": 1,
    "credentials": 
    {
        "version":"2",
        "client_id":"65C6B0BBEE03432EB52AAA51C6F78342",
        "client_secret":"Y-t5WLOY-YH5qDqwq4osPGi_qwmeGxoXTdNYuUq_Vs6X8_mZ",
        "endpoint_url":"https://api.xero.com/",
        "authorize_url":"https://login.xero.com/identity/connect/authorize",
        "access_token_url":"https://identity.xero.com/connect/token",
        "refresh_token_url":"https://identity.xero.com/connect/token",
        "scope":"offline_access openid profile email accounting.transactions accounting.transactions.read accounting.reports.read accounting.journals.read accounting.settings accounting.settings.read accounting.contacts accounting.contacts.read accounting.attachments accounting.attachments.read assets projects files payroll.employees payroll.payruns payroll.payslip payroll.timesheets payroll.settings",
        "redirect_uri": "http://localhost:5011/api/xero/callback",
        "redirect_frontend_success_url": "http://localhost:3000/success",
        "redirect_frontend_failed_url": "http://localhost:3000/failed"
        }
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Accounting Software successfully created",
    "data": {
        "result": {
            "id": 4,
            "name": "test_soft2",
            "credentials": {
                "version": "2",
                "client_id": "65C6B0BBEE03432EB52AAA51C6F78342",
                "client_secret": "Y-t5WLOY-YH5qDqwq4osPGi_qwmeGxoXTdNYuUq_Vs6X8_mZ",
                "endpoint_url": "https://api.xero.com/",
                "authorize_url": "https://login.xero.com/identity/connect/authorize",
                "access_token_url": "https://identity.xero.com/connect/token",
                "refresh_token_url": "https://identity.xero.com/connect/token",
                "scope": "offline_access openid profile email accounting.transactions accounting.transactions.read accounting.reports.read accounting.journals.read accounting.settings accounting.settings.read accounting.contacts accounting.contacts.read accounting.attachments accounting.attachments.read assets projects files payroll.employees payroll.payruns payroll.payslip payroll.timesheets payroll.settings",
                "redirect_uri": "http://localhost:5011/api/xero/callback",
                "redirect_frontend_success_url": "http://localhost:3000/success",
                "redirect_frontend_failed_url": "http://localhost:3000/failed"
            },
            "is_active": true,
            "connected": false,
            "accounting_software_type": 1,
            "owner": 3
        }
    }
}
```
