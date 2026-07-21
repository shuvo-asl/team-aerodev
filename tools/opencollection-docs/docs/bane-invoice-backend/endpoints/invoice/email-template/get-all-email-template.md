# Get All Email Template

**GET** `{{url}}/api/email_template/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Email Template

**Request:** `GET` `{{url}}/api/email_template/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Email Template Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 85,
                "deleted_at": null,
                "created_at": "2025-04-28T12:00:29+06:00",
                "updated_at": "2025-04-28T14:04:54.239059+06:00",
                "name": "payment notification",
                "subject": "invoice {{INVOICE_NO}} payment",
                "body": "dear {{OPERATOR_NAME}}, \r\nYou paid {{PAID_AMOUNT}}\r\ndue {{DUE_AMOUNT}}",
                "has_attachment": false,
                "is_active": true,
                "has_bank_details": false,
                "has_payment_link": false,
                "company": 11
            },
            {
                "id": 79,
                "deleted_at": null,
                "created_at": "2025-04-17T10:45:46.733678+06:00",
                "updated_at": "2025-04-29T15:16:05.418255+06:00",
                "name": "fvb",
                "subject": "Your Invoice Is Ready3",
                "body": "bg",
                "has_attachment": false,
                "is_active": true,
                "has_bank_details": false,
                "has_payment_link": false,
                "company": 11
            },
            {
                "id": 78,
                "deleted_at": null,
                "created_at": "2025-04-17T10:45:33.430459+06:00",
                "updated_at": "2025-04-17T10:45:36.574798+06:00",
                "name": "gtrd",
                "subject": "Your Invoice Is Ready3",
                "body": "fdvb",
                "has_attachment": false,
                "is_active": false,
                "has_bank_details": false,
                "has_payment_link": false,
                "company": 11
            },
            {
                "id": 77,
                "deleted_at": null,
                "created_at": "2025-04-17T10:34:14.188330+06:00",
                "updated_at": "2025-04-17T10:34:34.445093+06:00",
                "name": "EBL",
                "subject": "Your Invoice Is Ready3",
                "body": "{{INVOICE_NO}}",
                "has_attachment": false,
                "is_active": false,
                "has_bank_details": false,
                "has_payment_link": false,
                "company": 11
            },
            {
                "id": 76,
                "deleted_at": null,
                "created_at": "2025-04-17T10:33:14.118472+06:00",
                "updated_at": "2025-04-17T10:33:19.636444+06:00",
                "name": "xero",
                "subject": "Your Invoice Is Ready3",
                "body": "34rg",
                "has_attachment": false,
                "is_active": false,
                "has_bank_details": false,
                "has_payment_link": false,
                "company": 11
            },
            {
                "id": 67,
                "deleted_at": null,
                "created_at": "2025-04-08T16:25:52.187039+06:00",
                "updated_at": "2025-04-16T10:27:21.255723+06:00",
                "name": "bulk invoice reminder",
                "subject": "reminder regarding unpaid invoices4",
                "body": "Dear {{OPERATOR_NAME}}, \nFollowing invoices needs your attention!",
                "has_attachment": false,
                "is_active": true,
                "has_bank_details": false,
                "has_payment_link": false,
                "company": 11
            },
            {
                "id": 14,
                "deleted_at": null,
                "created_at": "2025-03-10T14:45:51.981297+06:00",
                "updated_at": "2025-04-24T17:01:48.103331+06:00",
                "name": "default",
                "subject": "{{CURRENT_MONTH}}Invoice Ready {{INVOICE_NO}}",
                "body": "{{CURRENT_MONTH}}\n{{PREVIOUS_MONTH}}\n{{INVOICE_NO}}\n{{OPERATOR_NAME}}\n{{DUE_DATE}}\n{{PAID_AMOUNT}}\n{{DUE_AMOUNT}}\n{{ISSUE_DATE}}",
                "has_attachment": true,
                "is_active": true,
                "has_bank_details": false,
                "has_payment_link": true,
                "company": 11
            }
        ]
    }
}
```

### get all active email templates

**Request:** `GET` `{{url}}/api/email_template/?is_active=true`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Email Template Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 85,
                "deleted_at": null,
                "created_at": "2025-04-28T12:00:29+06:00",
                "updated_at": "2025-04-28T14:04:54.239059+06:00",
                "name": "payment notification",
                "subject": "invoice {{INVOICE_NO}} payment",
                "body": "dear {{OPERATOR_NAME}}, \r\nYou paid {{PAID_AMOUNT}}\r\ndue {{DUE_AMOUNT}}",
                "has_attachment": false,
                "is_active": true,
                "has_bank_details": false,
                "has_payment_link": false,
                "company": 11
            },
            {
                "id": 79,
                "deleted_at": null,
                "created_at": "2025-04-17T10:45:46.733678+06:00",
                "updated_at": "2025-04-29T15:16:05.418255+06:00",
                "name": "fvb",
                "subject": "Your Invoice Is Ready3",
                "body": "bg",
                "has_attachment": false,
                "is_active": true,
                "has_bank_details": false,
                "has_payment_link": false,
                "company": 11
            },
            {
                "id": 67,
                "deleted_at": null,
                "created_at": "2025-04-08T16:25:52.187039+06:00",
                "updated_at": "2025-04-16T10:27:21.255723+06:00",
                "name": "bulk invoice reminder",
                "subject": "reminder regarding unpaid invoices4",
                "body": "Dear {{OPERATOR_NAME}}, \nFollowing invoices needs your attention!",
                "has_attachment": false,
                "is_active": true,
                "has_bank_details": false,
                "has_payment_link": false,
                "company": 11
            },
            {
                "id": 14,
                "deleted_at": null,
                "created_at": "2025-03-10T14:45:51.981297+06:00",
                "updated_at": "2025-04-24T17:01:48.103331+06:00",
                "name": "default",
                "subject": "{{CURRENT_MONTH}}Invoice Ready {{INVOICE_NO}}",
                "body": "{{CURRENT_MONTH}}\n{{PREVIOUS_MONTH}}\n{{INVOICE_NO}}\n{{OPERATOR_NAME}}\n{{DUE_DATE}}\n{{PAID_AMOUNT}}\n{{DUE_AMOUNT}}\n{{ISSUE_DATE}}",
                "has_attachment": true,
                "is_active": true,
                "has_bank_details": false,
                "has_payment_link": true,
                "company": 11
            }
        ]
    }
}
```
