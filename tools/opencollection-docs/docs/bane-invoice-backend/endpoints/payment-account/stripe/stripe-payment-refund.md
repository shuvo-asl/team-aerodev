# Stripe Payment Refund

**POST** `{{url}}/api/stripe-payment-refund/`

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
    "company_id": 1,
    "invoice_id": 67,
    "payment_intent_id": "pi_3RH0el4Jc2o38mIb02czZfWv"
}
```
