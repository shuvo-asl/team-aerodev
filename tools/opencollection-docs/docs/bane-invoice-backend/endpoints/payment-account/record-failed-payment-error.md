# record failed payment error

**POST** `{{url}}/api/record-failed-payment/`

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{
    "status": "error",
    "order_id": "INV-000020-ORD-1739760214-b9419e",
    "invoice_id": 24,
    "response_code": 300,
    "response_message": "failed"
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/record-failed-payment/`

```json
{
    "status": "error",
    "order_id": "INV-000020-ORD-1739760214-b9419e",
    "invoice_id": 24,
    "response_code": 300,
    "response_message": "failed"
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed payment attempt not found",
    "error": "Invalid invoice or order id",
    "errors": null
}
```
