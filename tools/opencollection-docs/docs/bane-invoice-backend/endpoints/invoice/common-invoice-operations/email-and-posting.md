# email and posting

**POST** `{{url}}/api/email-and-posting/`

## **Endpoint:** `POST /email-and-posting/`

Performs email sending and/or accounting software posting of an invoice.

### **Request Body**

#### Common Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `invoice_id` | integer | ✅ | ID of the invoice to process |
| `action_type` | string | ✅ | One of `"email"`, `"posting"`, `"posting_and_email"` |

#### Required if `action_type` is `"email"` or `"posting_and_email"`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `should_send_to_client` | boolean | ✅ | Whether to send the invoice to the client |
| `email_subject` | string | ✅ | Subject of the email |
| `email_body` | string | ✅ | Body of the email |
| `include_invoice_attachments` | boolean | ✅ | Whether to include attached documents |
| `include_auto_generated_invoice` | boolean | ✅ | Whether to include generated invoice PDF |
| `include_payment_url` | boolean | ✅ | Include payment URL in the email |
| `send_myself_a_copy` | boolean | ✅ | Send a copy to the sender |
| `cc` | list of emails | Optional | List of CC recipients |
| `bcc` | list of emails | Optional | List of BCC recipients |

#### Required if `action_type` is `"posting"` or `"posting_and_email"`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `accounting_software_ids` | list of integers | ✅ | IDs of accounting software to post to |
| `xero_organizations` |  |  |  |

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "invoice_id": 469,
    "action_type": "posting_and_email",
    "should_send_to_client": true,
    "accounting_software_ids": [1],
    "email_subject": "test email",
    "email_body": "Test body",
    "include_invoice_attachments": true,
    "include_auto_generated_invoice": true,
    "include_payment_url": true,
    "send_myself_a_copy": false
}
```

## Examples

### posting but invoice is not in eligible status

**Request:** `POST` `{{url}}/api/email-and-posting/`

```json
{
    "invoice_id": 435,
    "action_type": "posting",
    "accounting_software_ids": [1,2]
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to send invoice to accounting software",
    "error": "Invoice must be in either APPROVE or SENT status",
    "errors": null
}
```

### email or email and posting is used but email data is not provided

**Request:** `POST` `{{url}}/api/email-and-posting/`

```json
{
    "invoice_id": 435,
    "action_type": "posting_and_email",
    "should_send_to_client": true,
    "accounting_software_ids": [1, 2]
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to post and send invoice to client",
    "error": null,
    "errors": {
        "email_subject": "This field is required.",
        "email_body": "This field is required.",
        "include_invoice_attachments": "This field is required.",
        "include_auto_generated_invoice": "This field is required.",
        "include_payment_url": "This field is required.",
        "send_myself_a_copy": "This field is required."
    }
}
```

### successfully sent and posted

**Request:** `POST` `{{url}}/api/email-and-posting/`

```json
{
    "invoice_id": 446,
    "action_type": "posting_and_email",
    "should_send_to_client": true,
    "accounting_software_ids": [1],
    "email_subject": "test email",
    "email_body": "Test body",
    "include_invoice_attachments": true,
    "include_auto_generated_invoice": true,
    "include_payment_url": true,
    "send_myself_a_copy": false
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Successfully posted and sent the invoice to client",
    "data": {
        "result": {
            "email_tracking_id": "58e93466-57db-4fac-8f7b-014d4366faf1",
            "accounting_software_tracking_id": "68e5bad5-1280-4523-917a-2f611900e331"
        }
    }
}
```
