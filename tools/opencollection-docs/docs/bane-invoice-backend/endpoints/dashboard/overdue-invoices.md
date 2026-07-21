# overdue-invoices

**GET** `{{url}}/api/overdue-invoices?page=2&limit=5`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `page` | `2` | query |
| `limit` | `5` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### overdue-invoices

**Request:** `GET` `{{url}}/api/overdue-invoices?page=2&limit=5`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Over Due Invoices Successfully Fetched",
    "data": {
        "next": 3,
        "previous": 1,
        "current_page": 2,
        "total_object": 143,
        "total_page": 29,
        "result": [
            {
                "invoice_no": "INV-000217",
                "client": "Baidu",
                "due_date": "2024-11-09",
                "due": 6
            },
            {
                "invoice_no": "INV-000216",
                "client": "Baidu",
                "due_date": "2024-11-09",
                "due": 6
            },
            {
                "invoice_no": "INV-000215",
                "client": "Baidu",
                "due_date": "2024-11-09",
                "due": 2
            },
            {
                "invoice_no": "INV-000211",
                "client": "test123",
                "due_date": "2024-11-06",
                "due": 136
            },
            {
                "invoice_no": "INV-000210",
                "client": "Baidu",
                "due_date": "2024-11-04",
                "due": 6
            }
        ]
    }
}
```
