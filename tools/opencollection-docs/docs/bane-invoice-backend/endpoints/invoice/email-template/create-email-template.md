# Create Email Template

**POST** `{{url}}/api/email_template/`

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
    "name": "test",
    "subject": "demo",
    "body": "Hi Mr. {{B_operator_name}},\r\n\r\nWe are glad to inform you that your refund request is accepted. This is your invoice no: {{B_invoice_no}}.\r\n\r\nThanks for connecting with us.",
    "has_bank_details": false,
    "has_payment_link": true,
    "include_auto_generated_invoice": true,
    "include_invoice_attachments": true
}
```

## Examples

### Create Email Template

**Request:** `POST` `{{url}}/api/email_template/`

```json
{
    "name": "test",
    "subject": "demo",
    "body": "Hi Mr. {{B_operator_name}},\r\n\r\nWe are glad to inform you that your refund request is accepted. This is your invoice no: {{B_invoice_no}}.\r\n\r\nThanks for connecting with us.",
    "has_bank_details": false,
    "has_payment_link": true,
    "include_auto_generated_invoice": true,
    "include_invoice_attachments": true
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Email Template successfully created",
    "data": {
        "result": {
            "id": 131,
            "deleted_at": null,
            "created_at": "2025-05-29T12:03:07.374914+06:00",
            "updated_at": null,
            "name": "test",
            "subject": "demo",
            "body": "Hi Mr. {{B_operator_name}},\r\n\r\nWe are glad to inform you that your refund request is accepted. This is your invoice no: {{B_invoice_no}}.\r\n\r\nThanks for connecting with us.",
            "is_active": true,
            "has_bank_details": false,
            "has_payment_link": true,
            "include_auto_generated_invoice": true,
            "include_invoice_attachments": true,
            "company": 11
        }
    }
}
```
