# Test Confirm Stripe Payment

**POST** `https://api.stripe.com/v1/payment_intents/pi_3RGvVD4Jc2o38mIb0bJrnHCL/confirm`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer sk_test_51RFyzg4Jc2o38mIb1Bft2OMJtRGLbH4Eu3SE0JPQPvgjt8VRmMrZTBI9hBVZON8IQ896yzKR4x1UssPg3uHIsr5t00SEBPM5s5` |
| `Content-Type` | `application/x-www-form-urlencoded` |

## Body

Type: `form-urlencoded`

```
[{'name': 'payment_method', 'value': 'pm_card_visa'}]
```

## Examples

### Test Confirm Stripe Payment

**Request:** `POST` `https://api.stripe.com/v1/payment_intents/pi_3RGvcE4Jc2o38mIb1eWaOcqP/confirm`

```json
[{'name': 'payment_method', 'value': 'pm_card_visa'}]
```

**Response:** `200 OK`

```json
{
    "id": "pi_3RGvcE4Jc2o38mIb1eWaOcqP",
    "object": "payment_intent",
    "amount": 1185350,
    "amount_capturable": 0,
    "amount_details": {
        "tip": {}
    },
    "amount_received": 1185350,
    "application": null,
    "application_fee_amount": null,
    "automatic_payment_methods": {
        "allow_redirects": "never",
        "enabled": true
    },
    "canceled_at": null,
    "cancellation_reason": null,
    "capture_method": "automatic_async",
    "client_secret": "pi_3RGvcE4Jc2o38mIb1eWaOcqP_secret_TtG4ipYDdD5d3bWbVFHvOPY9f",
    "confirmation_method": "automatic",
    "created": 1745385178,
    "currency": "bdt",
    "customer": null,
    "description": null,
    "last_payment_error": null,
    "latest_charge": "ch_3RGvcE4Jc2o38mIb1LPx6Rul",
    "livemode": false,
    "metadata": {
        "amount": "11853.5",
        "currency": "bdt",
        "invoice_no": "INV-000059",
        "payment_amount": "11850.5",
        "processing_fee": "3.0",
        "tax_amount": "895.5"
    },
    "next_action": null,
    "on_behalf_of": null,
    "payment_method": "pm_1RGvrw4Jc2o38mIbPp65dlf2",
    "payment_method_configuration_details": {
        "id": "pmc_1RFz0E4Jc2o38mIbcVvaEzx2",
        "parent": null
    },
    "payment_method_options": {
        "card": {
            "installments": null,
            "mandate_options": null,
            "network": null,
            "request_three_d_secure": "automatic"
        },
        "link": {
            "persistent_token": null
        }
    },
    "payment_method_types": [
        "card",
        "link"
    ],
    "processing": null,
    "receipt_email": null,
    "review": null,
    "setup_future_usage": null,
    "shipping": null,
    "source": null,
    "statement_descriptor": null,
    "statement_descriptor_suffix": null,
    "status": "succeeded",
    "transfer_data": null,
    "transfer_group": null
}
```
