# Send invoice to client

**PATCH** `{{url}}/api/send-invoice-to-client/142/`

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
    "should_send_to_client": true
}
```

## Examples

### Send invoice to client

**Request:** `PATCH` `{{url}}/api/send-invoice-to-client/380/`

```json
{
    "should_send_to_client": false,
    "email_subject": "email from invoice status change",
    "email_body": "email body sample",
    "include_attachments": true,
    "include_payment_url": true,
    "send_myself_a_copy": true,
    "cc": ["kkamrulhasan2020@gmail.com"],
    "bcc": []
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice sent to client successfully",
    "data": {
        "result": {}
    }
}
```
