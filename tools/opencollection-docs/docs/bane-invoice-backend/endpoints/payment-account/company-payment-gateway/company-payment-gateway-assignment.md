# company payment gateway assignment

**POST** `{{url}}/api/company-payment-gateway/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "payment_gateway_model": 1
}
```

## Examples

### company payment gateway assignment

**Request:** `POST` `{{url}}/api/company-payment-gateway/`

```json
{
    "payment_gateway_model": 1
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Payment Gateway Failed To Create",
    "error": "This Payment Gateway is already assigned to this company!",
    "errors": null
}
```
