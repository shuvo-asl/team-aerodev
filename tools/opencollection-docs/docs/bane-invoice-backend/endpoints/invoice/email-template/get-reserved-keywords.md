# Get reserved keywords

**GET** `{{url}}/api/reserved_keywords/`

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
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "test",
            "subject": "demo",
            "text": "text",
            "attach_copy_invoice": false,
            "attach_customer_statement": false
        }
    ]
}
```
