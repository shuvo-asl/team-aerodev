# render email template

**POST** `{{url}}/api/render-email-template/1/`

**Description:**

Renders an email template with dynamic data such as invoice details, dates, and operator name.

---

### **Request Parameters**

**Path Parameter:**

- `template_id` (integer): ID of the email template to render.
    

**Request Body (JSON):**

``` json
{
    "invoice_no": "inv 001",
    "operator_name": "name op",
    "due_date": "2025-06-12",
    "paid_amount": 0,
    "due_amount": 20,
    "issue_date": "2025-05-27"
}
 ```

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "invoice_no": "inv001",
    "operator_name": "name op",
    "due_date": "2025-06-12",
    "paid_amount": 0,
    "due_amount": 20,
    "issue_date": "2025-05-27",
    "currency": 1
}
```

## Examples

### render email template

**Request:** `POST` `{{url}}/api/render-email-template/14/`

```json
{
    "invoice_no": "inv 001",
    "operator_name": "name op",
    "due_date": "2025-06-12",
    "paid_amount": 0,
    "due_amount": 20,
    "issue_date": "2025-05-27"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Email Template Rendered Successfully",
    "data": {
        "result": {
            "email_body": "May\nApril\ninv 001\nname op\nJune 12, 2025\n0.00\n20.00\nMay 27, 2025",
            "email_subject": "MayInvoice Ready inv 001"
        }
    }
}
```

### render email template

**Request:** `POST` `{{url}}/api/render-email-template/14/`

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to render Email Template",
    "error": null,
    "errors": {
        "invoice_no": "This field is required.",
        "operator_name": "This field is required.",
        "due_date": "This field is required.",
        "paid_amount": "This field is required.",
        "due_amount": "This field is required.",
        "issue_date": "This field is required."
    }
}
```
