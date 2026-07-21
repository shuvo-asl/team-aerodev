# Invoice Status Change

**PATCH** `{{url}}/api/invoice-status-change/113/`

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
    "status": "sent",
    "accounting_software_name": ["xero"],
    "xero_organizations": ["51618716-96eb-4fd0-a6de-9735c5f568d0"]
}
```

## Examples

### Invoice Status Change

**Request:** `PATCH` `{{url}}/api/invoice-status-change/252/`

```json
{
    "status": "approve"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice Status' Successfully Updated",
    "data": {
        "result": {
            "id": 252,
            "deleted_at": null,
            "created_at": "2024-11-12T11:36:12.816028+06:00",
            "updated_at": "2024-11-12T16:16:43.494457+06:00",
            "invoice_no": "INV-000226",
            "invoice_type": "general",
            "is_auto_generated": false,
            "due_date": "2024-11-15",
            "issue_date": "2024-11-12",
            "sent_date": null,
            "amount": 92,
            "tax_type": "exclusive",
            "tax_amount": 0,
            "payable_amount": 92,
            "last_chased_payable_amount": 0,
            "paid": 0,
            "due": 92,
            "user_uploaded_pdf": null,
            "status": "approve",
            "payment_status": "due",
            "references": null,
            "client": {
                "id": 45,
                "name": "Arifuzzaman Shoab",
                "short_code": "shoab@asl.aero",
                "email": "shoab@asl.aero",
                "phone": "+8801684806728",
                "billing_address": "Nikunja,Dhaka",
                "days_to_due_date": 3,
                "client_type": "agent",
                "preferred_currency": {
                    "id": 52,
                    "prefix": "$",
                    "short_key": "BDT35",
                    "current_rate": 1,
                    "default": null,
                    "name": "Taka7",
                    "flag": "/api/media/Screenshot_from_2024-09-23_17-52-36.png",
                    "is_active": true
                },
                "status": "active",
                "chasing_rule": null
            },
            "currency": {
                "id": 3,
                "prefix": "!",
                "short_key": "GBP",
                "current_rate": 0.0065,
                "default": null,
                "name": "Great Britian Pound",
                "flag": "/api/media/eric-brehm-JVQ7ElHJj9w-unsplash_ypmG3bN.jpg",
                "is_active": true
            },
            "pdf_template": 19,
            "invoice_items": [
                {
                    "id": 290,
                    "deleted_at": null,
                    "created_at": "2024-11-12T11:36:12.969347+06:00",
                    "updated_at": null,
                    "name": "cxvcxv",
                    "description": "xcvxv",
                    "unit_price": 34,
                    "unit": 3,
                    "sub_total": 102,
                    "discount_rate": null,
                    "discount_amount": 10,
                    "tax_rate": 0,
                    "tax_amount": 0,
                    "total": 92,
                    "coa_name": "270 - Interest Income",
                    "invoice": 252,
                    "flight": null,
                    "coa": 7
                }
            ],
            "files": [
                {
                    "id": 172,
                    "deleted_at": null,
                    "created_at": "2024-11-12T11:36:12.977498+06:00",
                    "updated_at": null,
                    "file": "/api/media/invoices/Group_14.png",
                    "invoice": 252
                },
                {
                    "id": 173,
                    "deleted_at": null,
                    "created_at": "2024-11-12T11:36:12.987065+06:00",
                    "updated_at": null,
                    "file": "/api/media/invoices/face.png",
                    "invoice": 252
                }
            ],
            "sent_accounting_software": [],
            "log": [
                {
                    "id": 18145,
                    "type": "update",
                    "model": "Invoice",
                    "object": 252,
                    "user_name": "admin",
                    "email": "admin@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.20.0.1",
                    "changes": {
                        "paid": {
                            "to": "0.00",
                            "from": null
                        },
                        "status": {
                            "to": "approve",
                            "from": "draft"
                        },
                        "tax_amount": {
                            "to": "0.00",
                            "from": null
                        },
                        "is_auto_generated": {
                            "to": false,
                            "from": null
                        },
                        "last_chased_payable_amount": {
                            "to": "0.00",
                            "from": null
                        }
                    },
                    "agent_info": "PostmanRuntime/7.42.0",
                    "status": "success",
                    "created_at": "2024-11-12T16:16:43.700120+06:00"
                },
                {
                    "id": 18133,
                    "type": "create",
                    "model": "Invoice",
                    "object": 252,
                    "user_name": "admin",
                    "email": "admin@gmail.com",
                    "impersonated_by": null,
                    "ip": "192.168.10.44",
                    "changes": {
                        "due": {
                            "to": "92",
                            "from": null
                        },
                        "paid": {
                            "to": 0,
                            "from": null
                        },
                        "amount": {
                            "to": "92.00",
                            "from": null
                        },
                        "client": {
                            "to": 45,
                            "from": null
                        },
                        "status": {
                            "to": "draft",
                            "from": null
                        },
                        "currency": {
                            "to": 3,
                            "from": null
                        },
                        "due_date": {
                            "to": "2024-11-15T00:00:00",
                            "from": null
                        },
                        "tax_type": {
                            "to": "exclusive",
                            "from": null
                        },
                        "invoice_no": {
                            "to": "INV-000226",
                            "from": null
                        },
                        "issue_date": {
                            "to": "2024-11-12T00:00:00",
                            "from": null
                        },
                        "tax_amount": {
                            "to": "0.00",
                            "from": null
                        },
                        "invoice_type": {
                            "to": "general",
                            "from": null
                        },
                        "pdf_template": {
                            "to": 19,
                            "from": null
                        },
                        "payable_amount": {
                            "to": 92,
                            "from": null
                        },
                        "payment_status": {
                            "to": "due",
                            "from": null
                        },
                        "is_auto_generated": {
                            "to": false,
                            "from": null
                        },
                        "last_chased_payable_amount": {
                            "to": 0,
                            "from": null
                        }
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2024-11-12T11:36:12.971467+06:00"
                }
            ]
        }
    }
}
```
