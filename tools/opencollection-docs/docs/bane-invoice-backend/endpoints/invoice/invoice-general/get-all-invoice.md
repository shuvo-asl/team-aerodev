# Get All Invoice

**GET** `{{url}}/api/invoice?limit=10&page=1&invoice_type=general`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `10` | query |
| `page` | `1` | query |
| `search_key` | `` | query |
| `status` | `draft` | query |
| `invoice_type` | `general` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Invoice

**Request:** `GET` `{{url}}/api/invoice/`

**Response:** `200 OK`

```json
{
    "success": true,
    "data": [
        {
            "id": 50,
            "invoice_no": "INV-000010",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-19T17:28:13.305748+06:00",
            "amount": 8553.77,
            "payable_amount": 8553.77,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-09T17:28:13.346847+06:00",
            "updated_at": "2023-11-09T17:28:13.346861+06:00",
            "operator": 1,
            "billing_flight": 59,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 49,
            "invoice_no": "INV-000009",
            "invoice_type": "manual",
            "due_date": "2023-11-19T17:17:46.163754+06:00",
            "amount": 601.77,
            "payable_amount": 601.77,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-09T17:17:46.177835+06:00",
            "updated_at": "2023-11-09T17:17:46.177850+06:00",
            "operator": 1,
            "billing_flight": 58,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 30,
            "invoice_no": "INV-000008",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-18T17:30:24.980466+06:00",
            "amount": 601.77,
            "payable_amount": 601.77,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-08T17:30:25.014816+06:00",
            "updated_at": "2023-11-08T17:30:25.014856+06:00",
            "operator": 1,
            "billing_flight": 58,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 29,
            "invoice_no": "INV-000007",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-18T17:29:55.263523+06:00",
            "amount": 0,
            "payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-08T17:29:55.288535+06:00",
            "updated_at": "2023-11-08T17:29:55.288557+06:00",
            "operator": 1,
            "billing_flight": 57,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 28,
            "invoice_no": "INV-000006",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-18T17:28:56.095730+06:00",
            "amount": 0,
            "payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-08T17:28:56.126748+06:00",
            "updated_at": "2023-11-08T17:28:56.126761+06:00",
            "operator": 1,
            "billing_flight": 56,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 27,
            "invoice_no": "INV-000005",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-18T17:04:22.960398+06:00",
            "amount": 0,
            "payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-08T17:04:23.000884+06:00",
            "updated_at": "2023-11-08T17:04:23.000901+06:00",
            "operator": 1,
            "billing_flight": 55,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 26,
            "invoice_no": "INV-000004",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-16T17:40:45.556444+06:00",
            "amount": 0,
            "payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-06T17:40:45.582984+06:00",
            "updated_at": "2023-11-06T17:40:45.583002+06:00",
            "operator": 1,
            "billing_flight": 54,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 12,
            "invoice_no": "INV-000003",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-16T17:08:57.251908+06:00",
            "amount": 0,
            "payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-06T17:08:57.276042+06:00",
            "updated_at": "2023-11-06T17:08:57.276061+06:00",
            "operator": 1,
            "billing_flight": 40,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 11,
            "invoice_no": "INV-000002",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-16T13:45:29.096345+06:00",
            "amount": 0,
            "payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-06T13:45:29.123667+06:00",
            "updated_at": "2023-11-06T13:45:29.123685+06:00",
            "operator": 1,
            "billing_flight": 39,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 10,
            "invoice_no": "INV-000001",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-02T21:36:20.277267+06:00",
            "amount": 0,
            "payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-10-23T21:36:20.293224+06:00",
            "updated_at": "2023-10-23T21:36:20.293233+06:00",
            "operator": 1,
            "billing_flight": 31,
            "currency": 1,
            "updated_by": null
        }
    ]
}
```

### Get All Invoice with pagination

**Request:** `GET` `{{url}}/api/invoice?limit=2&page=2`

**Response:** `200 OK`

```json
{
    "success": true,
    "next": 3,
    "previous": 1,
    "current_page": 2,
    "total_object": 10,
    "total_page": 5,
    "data": [
        {
            "id": 30,
            "invoice_no": "INV-000008",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-18T17:30:24.980466+06:00",
            "amount": 601.77,
            "payable_amount": 601.77,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-08T17:30:25.014816+06:00",
            "updated_at": "2023-11-08T17:30:25.014856+06:00",
            "operator": 1,
            "billing_flight": 58,
            "currency": 1,
            "updated_by": null
        },
        {
            "id": 29,
            "invoice_no": "INV-000007",
            "invoice_type": "auto_generate",
            "due_date": "2023-11-18T17:29:55.263523+06:00",
            "amount": 0,
            "payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "created_at": "2023-11-08T17:29:55.288535+06:00",
            "updated_at": "2023-11-08T17:29:55.288557+06:00",
            "operator": 1,
            "billing_flight": 57,
            "currency": 1,
            "updated_by": null
        }
    ]
}
```

### Get All Invoice

**Request:** `GET` `{{url}}/api/invoice`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 47,
                "deleted_at": null,
                "created_at": "2024-09-18T18:08:48.558212+06:00",
                "updated_at": null,
                "invoice_no": "INV-000003",
                "invoice_type": "general",
                "is_auto_generated": false,
                "due_date": null,
                "sent_date": null,
                "amount": 70,
                "vat": 5,
                "vat_amount": 3.5,
                "payable_amount": 73.5,
                "last_chased_payable_amount": 0,
                "paid": 0,
                "due": 0,
                "status": "draft",
                "payment_status": "due",
                "references": null,
                "client": 1,
                "currency": {
                    "id": 1,
                    "prefix": "$",
                    "short_key": "Dollar",
                    "current_rate": 120,
                    "default": null
                }
            },
            {
                "id": 46,
                "deleted_at": null,
                "created_at": "2024-09-18T17:56:24.053165+06:00",
                "updated_at": null,
                "invoice_no": "INV-000002",
                "invoice_type": "general",
                "is_auto_generated": false,
                "due_date": null,
                "sent_date": null,
                "amount": 70,
                "vat": 5,
                "vat_amount": 3.5,
                "payable_amount": 73.5,
                "last_chased_payable_amount": 0,
                "paid": 0,
                "due": 0,
                "status": "draft",
                "payment_status": "due",
                "references": null,
                "client": 1,
                "currency": {
                    "id": 1,
                    "prefix": "$",
                    "short_key": "Dollar",
                    "current_rate": 120,
                    "default": null
                }
            },
            {
                "id": 45,
                "deleted_at": null,
                "created_at": "2024-09-18T17:55:36.937769+06:00",
                "updated_at": null,
                "invoice_no": "INV-000001",
                "invoice_type": "general",
                "is_auto_generated": false,
                "due_date": null,
                "sent_date": null,
                "amount": 70,
                "vat": 5,
                "vat_amount": 3.5,
                "payable_amount": 73.5,
                "last_chased_payable_amount": 0,
                "paid": 0,
                "due": 0,
                "status": "draft",
                "payment_status": "due",
                "references": null,
                "client": 1,
                "currency": {
                    "id": 1,
                    "prefix": "$",
                    "short_key": "Dollar",
                    "current_rate": 120,
                    "default": null
                }
            }
        ]
    }
}
```
