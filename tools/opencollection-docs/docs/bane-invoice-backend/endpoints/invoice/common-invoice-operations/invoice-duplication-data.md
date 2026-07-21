# invoice duplication data

**GET** `{{url}}/api/invoice-duplication-data/28/`

## Auth

Type: `bearer`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/invoice-duplication-data/28/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Duplication data Fetched Successfully",
    "data": {
        "result": {
            "client": 2,
            "invoice_type": "general",
            "due_date": "2025-01-31",
            "currency": 10,
            "references": null,
            "pdf_template": 2,
            "invoice_items": [
                {
                    "id": 29,
                    "flight_no": null,
                    "deleted_at": null,
                    "created_at": "2025-01-16T14:58:49.391286+06:00",
                    "updated_at": null,
                    "name": "",
                    "description": "hi",
                    "unit_price": 67,
                    "unit": 1,
                    "sub_total": 67,
                    "discount_rate": null,
                    "discount_amount": 0,
                    "tax_rate": 0,
                    "tax_amount": 0,
                    "total": 67,
                    "coa_name": "404 - Bank Fees",
                    "invoice": 28,
                    "flight": null,
                    "coa": 63
                }
            ],
            "tax_type": "exclusive",
            "tax_amount": 0,
            "amount": 67,
            "payable_amount": 67,
            "issue_date": "2025-01-16"
        }
    }
}
```
