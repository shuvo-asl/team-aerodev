# record failed payments session time out

**POST** `{{url}}/api/record-failed-payment/`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `` | `` | query |

## Body

Type: `json`

```json
{
    "status": "expired",
    "order_id": "INV-000020-ORD-1739760214-b9419e",
    "invoice_id": 24
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/record-failed-payment/`

```json
{
    "status": "expired",
    "order_id": "INV-000020-ORD-1739760214-b9419e",
    "invoice_id": 24
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Failed payment details updated successfully",
    "data": {
        "result": {}
    }
}
```
