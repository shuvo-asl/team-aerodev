# send operator performance summary

**POST** `{{url}}/api/dashboard/operator-performance-summary/email/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "email_subject": "test operator performance2",
    "email_body": "sample body",
    "include_invoice_attachments": false,
    "include_auto_generated_invoice": false,
    "include_payment_url": false,
    "send_myself_a_copy": false,
    "to": ["kamrul@asl.aero"],
    "start_date": "2026-05-01",
    "end_date": "2026-05-30"
  }
```
