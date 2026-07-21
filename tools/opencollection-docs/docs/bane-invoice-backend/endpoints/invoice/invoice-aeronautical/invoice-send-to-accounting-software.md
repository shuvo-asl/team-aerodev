# Invoice Send To Accounting Software

**POST** `{{url}}/api/invoice-send-to-accounting-software/`

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
    "invoice_id": 14,
    "accounting_software_name": ["xero","Afroza Mukta"],
    "xero_organizations": ["51618716-96eb-4fd0-a6de-9735c5f568d0", "f3afa7ee-4d7e-430d-8a58-12b295b61f7e"]
}
```
