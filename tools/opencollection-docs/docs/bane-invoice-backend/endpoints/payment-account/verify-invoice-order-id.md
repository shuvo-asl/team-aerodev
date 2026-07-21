# Verify Invoice Order id

**POST** `{{url}}/api/initiate-payment-process/`

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{
    "gateway_name": "ebl",
    "invoice_id": 1,
    "company_id": 1,
    "token": "fa770c3a-ae1a-4dbc-941a-6ec15f36b936"
}
```
