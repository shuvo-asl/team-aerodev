# invoice info for payment page

**GET** `{{url}}/api/invoice-info-for-payment-page/6ec8affa-19f9-4c8d-be82-a338ebb63199/`

## Auth

Type: `inherit`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/invoice-info-for-payment-page/248/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Details Fetched Successfully",
    "data": {
        "result": {
            "invoice_no": "INV-000242",
            "due_date": "2025-04-23",
            "due": 20,
            "currency": "AFN",
            "issue_date": "2025-04-08",
            "company_name": "blue origin",
            "company_logo": "http://localhost:5011/api/media/images/system_settings/logo/2025/04/08/ASL_logo_Update_2024_by_ZM_FINAL.png",
            "client": "Kamrul Hasan"
        }
    }
}
```
