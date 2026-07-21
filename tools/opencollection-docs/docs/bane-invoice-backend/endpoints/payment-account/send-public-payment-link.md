# send public payment link

**POST** `{{url}}/api/send-public-payment-link/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "valid_till": "2025-4-12",
    "invoice": 151,
    "amount": 720
}
```

## Examples

### send public payment link

**Request:** `POST` `{{url}}/api/send-public-payment-link/`

```json
{
    "valid_till": "2025-4-12",
    "invoice": 9,
    "amount": 2
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Public Payment Link Sent Successfully",
    "data": {
        "result": {}
    }
}
```
