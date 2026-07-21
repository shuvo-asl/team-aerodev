# Update Invoice

**PATCH** `{{url}}/api/invoice/158/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

```
[{'name': 'client', 'type': 'text', 'value': '87'}, {'name': 'currency', 'type': 'text', 'value': '15'}, {'name': 'status', 'type': 'text', 'value': 'sent'}, {'name': 'invoice_type', 'type': 'text', 'value': 'general'}, {'name': 'amount', 'type': 'text', 'value': '47.80'}, {'name': 'tax_amount', 'type': 'text', 'value': '0'}, {'name': 'payable_amount', 'type': 'text', 'value': '47.80'}, {'name': 'tax_type', 'type': 'text', 'value': 'inclusive'}, {'name': 'files_to_add', 'type': 'file', 'value': ['/Users/asl_systems/Downloads/elk.pdf'], 'disabled': True}, {'name': 'files_to_delete', 'type': 'text', 'value': '[1]', 'disabled': True}, {'name': 'items', 'type': 'text', 'value': '[\n                \n {\n                    "name": "Alu 3",\n                    "description": "alu 3",\n                    "unit_price": 5,\n                    "unit": 1,\n                    "sub_total": 5,\n                    "discount_rate": null,\n                    "discount_amount": 0,\n                    "tax_rate": 11,\n                    "tax_amount": 0,\n                    "total": 5,\n                    "invoice": 158,\n                    "coa": 51\n                }\n            ]'}, {'name': 'updated_items', 'type': 'text', 'value': '[\n                    {\n                    "id": 174,\n                    "name": "Alu",\n                    "description": "dsafsdf",\n                    "unit_price": 21.0,\n                    "unit": 2,\n                    "sub_total": 42.0,\n                    "discount_rate": null,\n                    "discount_amount": 4.2,\n                    "tax_amount": 0.0,\n                    "total": 37.8,\n                    "invoice": 158,\n                    "flight": null,\n                    "tax_rate": 11,\n                    "coa": 51\n                },\n                { \n                   "id": 175,\n                    "name": "Alu 2",\n                    "description": "alu 2",\n                    "unit_price": 5,\n                    "unit": 1,\n                    "sub_total": 5,\n                    "discount_rate": null,\n                    "discount_amount": 0,\n                    "tax_rate": 11,\n                    "tax_amount": 0,\n                    "total": 5,\n                    "invoice": 158,\n                    "coa": 51\n                }\n            ]'}, {'name': 'deleted_items', 'type': 'text', 'value': '[]', 'disabled': True}, {'name': 'pdf_template', 'type': 'text', 'value': '1'}, {'name': 'schedules_to_be_deleted', 'type': 'text', 'value': '[7]', 'disabled': True}, {'name': 'due_date', 'type': 'text', 'value': '2025-6-22'}, {'name': 'issue_date', 'type': 'text', 'value': datetime.date(2025, 6, 29)}, {'name': 'invoice_no', 'type': 'text', 'value': 'inv007', 'disabled': True}, {'name': 'accounting_software_ids', 'type': 'text', 'value': '[2]'}, {'name': 'should_send_to_client', 'type': 'text', 'value': 'false'}]
```

## Examples

### Update Invoice

**Request:** `PATCH` `{{url}}/api/invoice/56/`

```json
[{'name': 'client', 'type': 'text', 'value': '1'}, {'name': 'currency', 'type': 'text', 'value': '1'}, {'name': 'status', 'type': 'text', 'value': 'approve'}, {'name': 'invoice_type', 'type': 'text', 'value': 'general'}, {'name': 'amount', 'type': 'text', 'value': '70'}, {'name': 'tax_amount', 'type': 'text', 'value': '6.36'}, {'name': 'payable_amount', 'type': 'text', 'value': '70'}, {'name': 'tax_type', 'type': 'text', 'value': 'inclusive'}, {'name': 'files_to_add', 'type': 'file', 'value': ['/Users/asl_systems/Downloads/INV-000008 (4).pdf']}, {'name': 'files_to_delete', 'type': 'text', 'value': '[1]'}, {'name': 'items', 'type': 'text', 'value': '[\n        {\n            "name": "Alu updated",\n            "coa": 227,\n            "description": "dsafsdf",\n            "unit": "5",\n            "unit_price": "10",\n            "tax_amount": 4.18,\n            "tax_rate": 10,\n            "sub_total": "50",\n            "discount_amount": "4",\n            "total": "46"\n        }\n]'}, {'name': 'updated_items', 'type': 'text', 'value': '[\n        {\n            "id": 34,\n            "invoice": 56,\n            "name": "peyaz updated",\n            "coa": 227,\n            "description": "dsafsdf",\n            "unit": "3",\n            "unit_price": 10,\n            "sub_total": "30",\n            "discount_amount": 6,\n            "total": 24,\n            "tax_amount": 2.18,\n            "tax_rate": 10\n        }\n    ]'}, {'name': 'deleted_items', 'type': 'text', 'value': '[33]'}]
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice' Successfully Updated",
    "data": {
        "result": {
            "id": 56,
            "deleted_at": null,
            "created_at": "2024-09-29T14:28:31.812804+06:00",
            "updated_at": "2024-09-29T14:46:07.890402+06:00",
            "invoice_no": "INV-000010",
            "invoice_type": "general",
            "is_auto_generated": false,
            "due_date": null,
            "issue_date": null,
            "sent_date": null,
            "amount": 70,
            "tax_type": "inclusive",
            "total_tax_amount": 0,
            "payable_amount": 70,
            "last_chased_payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "approve",
            "payment_status": "due",
            "references": null,
            "client": {
                "id": 1,
                "name": "Ismail Hasan Sarker",
                "short_code": "titas",
                "email": "ismail@asl.aero",
                "phone": "01684806728",
                "billing_address": "Joydebpur, post: Duet",
                "days_to_due_date": 15,
                "client_type": "operator",
                "preferred_currency": {
                    "id": 1,
                    "prefix": "$",
                    "short_key": "Dollar",
                    "current_rate": 120,
                    "default": true,
                    "name": "dollar",
                    "flag": null,
                    "is_active": true
                },
                "status": "inactive"
            },
            "currency": {
                "id": 1,
                "prefix": "$",
                "short_key": "Dollar",
                "current_rate": 120,
                "default": true,
                "name": "dollar",
                "flag": null,
                "is_active": true
            },
            "invoice_items": [
                {
                    "id": 34,
                    "deleted_at": null,
                    "created_at": "2024-09-29T14:28:31.935425+06:00",
                    "updated_at": "2024-09-29T14:46:07.964410+06:00",
                    "name": "peyaz updated",
                    "description": "dsafsdf",
                    "unit_price": 10,
                    "unit": 3,
                    "sub_total": 30,
                    "discount_rate": null,
                    "discount_amount": 6,
                    "tax_rate": 10,
                    "tax_amount": 2.18,
                    "total": 24,
                    "invoice": 56,
                    "flight": null,
                    "coa": 227
                },
                {
                    "id": 36,
                    "deleted_at": null,
                    "created_at": "2024-09-29T14:46:07.955498+06:00",
                    "updated_at": null,
                    "name": "Alu updated",
                    "description": "dsafsdf",
                    "unit_price": 10,
                    "unit": 5,
                    "sub_total": 50,
                    "discount_rate": null,
                    "discount_amount": 4,
                    "tax_rate": 10,
                    "tax_amount": 4.18,
                    "total": 46,
                    "invoice": 56,
                    "flight": null,
                    "coa": 227
                }
            ],
            "log": [
                {
                    "id": 5660,
                    "deleted_at": null,
                    "created_at": "2024-09-29T14:46:07.951908+06:00",
                    "updated_at": null,
                    "type": "update",
                    "model": "Invoice",
                    "object": 56,
                    "user_name": "admin",
                    "impersonated_by": null,
                    "ip": "192.168.65.1",
                    "email": "",
                    "changes": {
                        "status": {
                            "to": "approve",
                            "from": "draft"
                        },
                        "updated_at": {
                            "to": "2024-09-29T08:46:07.890402Z",
                            "from": null
                        }
                    },
                    "agent_info": "PostmanRuntime/7.42.0",
                    "status": "success"
                },
                {
                    "id": 5658,
                    "deleted_at": null,
                    "created_at": "2024-09-29T14:45:04.828977+06:00",
                    "updated_at": null,
                    "type": "update",
                    "model": "Invoice",
                    "object": 56,
                    "user_name": "admin",
                    "impersonated_by": null,
                    "ip": "192.168.65.1",
                    "email": "",
                    "changes": {
                        "status": {
                            "to": "approve",
                            "from": "draft"
                        },
                        "updated_at": {
                            "to": "2024-09-29T08:45:04.820878Z",
                            "from": null
                        }
                    },
                    "agent_info": "PostmanRuntime/7.42.0",
                    "status": "success"
                },
                {
                    "id": 5657,
                    "deleted_at": null,
                    "created_at": "2024-09-29T14:44:26.079699+06:00",
                    "updated_at": null,
                    "type": "update",
                    "model": "Invoice",
                    "object": 56,
                    "user_name": "admin",
                    "impersonated_by": null,
                    "ip": "192.168.65.1",
                    "email": "",
                    "changes": {
                        "status": {
                            "to": "approve",
                            "from": "draft"
                        },
                        "updated_at": {
                            "to": "2024-09-29T08:44:26.008525Z",
                            "from": null
                        }
                    },
                    "agent_info": "PostmanRuntime/7.42.0",
                    "status": "success"
                },
                {
                    "id": 5656,
                    "deleted_at": null,
                    "created_at": "2024-09-29T14:39:25.407539+06:00",
                    "updated_at": null,
                    "type": "update",
                    "model": "Invoice",
                    "object": 56,
                    "user_name": "admin",
                    "impersonated_by": null,
                    "ip": "192.168.65.1",
                    "email": "",
                    "changes": {
                        "status": {
                            "to": "approve",
                            "from": "draft"
                        },
                        "updated_at": {
                            "to": "2024-09-29T08:39:25.278369Z",
                            "from": null
                        }
                    },
                    "agent_info": "PostmanRuntime/7.42.0",
                    "status": "success"
                },
                {
                    "id": 5651,
                    "deleted_at": null,
                    "created_at": "2024-09-29T14:28:31.924374+06:00",
                    "updated_at": null,
                    "type": "create",
                    "model": "Invoice",
                    "object": 56,
                    "user_name": "admin",
                    "impersonated_by": null,
                    "ip": "192.168.65.1",
                    "email": "",
                    "changes": {},
                    "agent_info": "PostmanRuntime/7.42.0",
                    "status": "success"
                }
            ]
        }
    }
}
```

### Update Invoice with email sending

**Request:** `PATCH` `{{url}}/api/invoice/395/`

```json
[{'name': 'client', 'type': 'text', 'value': '30'}, {'name': 'currency', 'type': 'text', 'value': '15'}, {'name': 'status', 'type': 'text', 'value': 'sent'}, {'name': 'invoice_type', 'type': 'text', 'value': 'general'}, {'name': 'amount', 'type': 'text', 'value': '37.80'}, {'name': 'tax_amount', 'type': 'text', 'value': '4.05'}, {'name': 'payable_amount', 'type': 'text', 'value': '37.80'}, {'name': 'tax_type', 'type': 'text', 'value': 'inclusive'}, {'name': 'files_to_add', 'type': 'file', 'value': ['/Users/asl_systems/Downloads/elk.pdf']}, {'name': 'files_to_delete', 'type': 'text', 'value': '[1]'}, {'name': 'items', 'type': 'text', 'value': '[\n                {\n                    "id": 308,\n                    "flight_no": null,\n                    "deleted_at": null,\n                    "created_at": "2025-04-21T16:59:51.655349+06:00",\n                    "updated_at": null,\n                    "name": "Alu",\n                    "description": "dsafsdf",\n                    "unit_price": 21.0,\n                    "unit": 2,\n                    "sub_total": 42.0,\n                    "discount_rate": null,\n                    "discount_amount": 4.2,\n                    "tax_rate": 12.0,\n                    "tax_amount": 4.05,\n                    "total": 37.8,\n                    "coa_name": "881 - Owner A Funds Introduced",\n                    "invoice": 305,\n                    "flight": null,\n                    "coa": 51\n                }\n            ]', 'disabled': True}, {'name': 'updated_items', 'type': 'text', 'value': ' [\n                {\n                    "id": 415,\n                    "flight_no": null,\n                    "deleted_at": null,\n                    "created_at": "2025-05-26T09:35:05.243037+06:00",\n                    "updated_at": null,\n                    "name": "Alu",\n                    "description": "dsafsdf",\n                    "unit_price": 21.0,\n                    "unit": 2,\n                    "sub_total": 42.0,\n                    "discount_rate": null,\n                    "discount_amount": 4.2,\n                    "tax_rate": 12.0,\n                    "tax_amount": 4.05,\n                    "total": 37.8,\n                    "coa_name": "881 - Owner A Funds Introduced",\n                    "invoice": 395,\n                    "flight": null,\n                    "coa": 51\n                }\n            ]'}, {'name': 'deleted_items', 'type': 'text', 'value': '[]', 'disabled': True}, {'name': 'pdf_template', 'type': 'text', 'value': '2'}, {'name': 'schedules_to_be_deleted', 'type': 'text', 'value': '[7]'}, {'name': 'due_date', 'type': 'text', 'value': '2025-6-12'}, {'name': 'issue_date', 'type': 'text', 'value': datetime.date(2025, 1, 15)}, {'name': 'invoice_no', 'type': 'text', 'value': 'inv00803'}, {'name': 'should_send_to_client', 'type': 'text', 'value': 'true'}, {'name': 'email_subject', 'type': 'text', 'value': 'subject'}, {'name': 'email_body', 'type': 'text', 'value': 'body'}, {'name': 'include_attachments', 'type': 'text', 'value': 'true'}, {'name': 'include_payment_url', 'type': 'text', 'value': 'false'}, {'name': 'send_me_a_copy', 'type': 'text', 'value': 'true', 'disabled': True}, {'name': 'cc', 'type': 'text', 'value': '[]'}, {'name': 'bcc', 'type': 'text', 'value': '[]'}]
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice successfully updated",
    "data": {
        "result": {
            "id": 395,
            "invoice_items": [
                {
                    "id": 415,
                    "flight_no": null,
                    "deleted_at": null,
                    "created_at": "2025-05-26T09:35:05.243037+06:00",
                    "updated_at": "2025-05-26T10:20:47.964900+06:00",
                    "name": "Alu",
                    "description": "dsafsdf",
                    "unit_price": 21,
                    "unit": 2,
                    "sub_total": 42,
                    "discount_rate": null,
                    "discount_amount": 4.2,
                    "tax_rate": 12,
                    "tax_amount": 4.05,
                    "total": 37.8,
                    "coa_name": "881 - Owner A Funds Introduced",
                    "invoice": 395,
                    "flight": null,
                    "coa": 51
                }
            ],
            "client": {
                "id": 30,
                "name": "Kamrul Hasan",
                "short_code": "N/A",
                "email": "kamrul@asl.aero",
                "phone": "+8801558250667",
                "billing_address": "Dhaka",
                "days_to_due_date": 15,
                "client_type": "agent",
                "preferred_currency": {
                    "current_rate": 1,
                    "name": "Afghan Afghani",
                    "prefix": "Afs",
                    "short_key": "AFN",
                    "flag": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAANkSURBVHja7JfPixxFFMc/1d0zs5vJzGaNq2BcVBByiQSyavS6LIKg4ElBkYj6B3jw3wgiGgVFUBQ8exBvioTokjUJKF42EaPgZuMmu73TM+kf9eN56M5OT8TuPsjsJQ+K6up6XfWt7/u+7tdKRNhP89hnuwtAAT7QKfppmgXSAOivrKxs+379/p8QNFr5jRcfqadeKb55/b17AmDO8zyWl5drHzrQkKTlRxdqfX69fgVgLgA6xhjSNCUMQ6SIS9kEUAJG+cWslCIok47A9cgrhlJ4jf0EmJ/tkRoN0AkAnHPEcUySJJWopSEDickq52OdoZ0FyIOqtSaOY+I4/l8AxLr6IG0/IMsZyAEYYxgOh4xGoxoA7YJ2l2ewVwTLyfgewqgGgO/5mDIDxhiiKNoDMKmD8ciJyS+DFv69h0EVXiLYGzehONUorWZSiSKz2SSAwWBQy4AjgyAgeGAeF27jzR/O74fbeL2DmI0NMIYou1WzjiM22aQGoiiq14AvHHr7LZJzqyRrVwi8NgDm2jVmnjxJ9/lnCU+/yyiL95hBqXF/G4A4dFkDWmsGgwFpmlYCCI4dpf3wQ4TvnKFzYolDb74GQPjxpyTnL9B/+SWCxUWG2X8cpACinUFb828NaK2r5d3y0Vf/JFg8QmfpOKNvvwOg8/hx7I0t9NU/oOUzqglBZloEvjfJwHA4rAXgdbv4Dx7B6/dIz19g5umn8rz/cRWv38vnul124t9rzhEwN3Nw/DU0xmCMwVpb2dK1i5jNTSTNUEEL1WnnLWghSYbZ3CRdu4h1rrIZZ8m0mWRARHDOVVO3fhm9/hv9U6+QnP2B6IsvAZhZOkH3hedIfrpEtn4ZJ0erxSwexpVEaI1tBECcZveDD3GnXmX25BPMPpN/wNxOyK3vzxJ99jliNE5q1hG5IwuKQX196KH/2mD3/Y/ILv2M+XsrX+S+BeJzq9jBDgqPJnWmtW4yC3zfr2UADAqFC28y/Pqr0vtSUAQoPMDikNoySLuSBqy1+L7fALkpraHuKKxs0RowKfmee1ngnEMpNb06UCmcKwEQkekCQOGcjENwG0Cv16uRYLvRBr3OgVofKQGwAFEU1T600xBAtBs18BIAq4D7gceABaZrW8Avqvgn6BX9NC0FInX353S/AfwzAGTE9qrU0AqGAAAAAElFTkSuQmCC",
                    "id": 15,
                    "is_default": true
                },
                "status": "active",
                "chasing_rule": [
                    {
                        "id": 13,
                        "name": "first rule",
                        "is_default": false,
                        "chase_on": "after due date",
                        "is_cumulative": true,
                        "max_repetition": 5,
                        "email_template": 14,
                        "email_template_name": "default",
                        "chasing_days": [
                            3
                        ]
                    }
                ],
                "interest_rule": [
                    {
                        "id": 20,
                        "name": "first rule",
                        "is_default": false,
                        "is_cumulative": false,
                        "max_repetition": null,
                        "interest_type": "fixed",
                        "interest_rate": 20,
                        "interest_base": "invoice_amount_after_interest",
                        "start_day": null,
                        "interest_day": 5
                    }
                ]
            },
            "files": [],
            "log": [
                {
                    "id": 26690,
                    "type": "update",
                    "model": "Invoice",
                    "object": 395,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "items": [
                            {
                                "type": "update",
                                "object": 415,
                                "changes": {},
                                "status": "success",
                                "item": "Alu"
                            }
                        ]
                    },
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-26T10:20:53.915061+06:00"
                },
                {
                    "id": 26687,
                    "type": "update",
                    "model": "Invoice",
                    "object": 395,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "status": {
                            "to": "sent",
                            "from": "approve"
                        },
                        "items": [
                            {
                                "type": "update",
                                "object": 415,
                                "changes": {},
                                "status": "success",
                                "item": "Alu"
                            }
                        ]
                    },
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-26T10:20:47.963982+06:00"
                },
                {
                    "id": 26676,
                    "type": "update",
                    "model": "Invoice",
                    "object": 395,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "items": [
                            {
                                "type": "update",
                                "object": 415,
                                "changes": {},
                                "status": "success",
                                "item": "Alu"
                            }
                        ]
                    },
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-26T10:16:32.172212+06:00"
                },
                {
                    "id": 26674,
                    "type": "update",
                    "model": "Invoice",
                    "object": 395,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "status": {
                            "to": "approve",
                            "from": "draft"
                        },
                        "items": [
                            {
                                "type": "update",
                                "object": 415,
                                "changes": {},
                                "status": "success",
                                "item": "Alu"
                            }
                        ]
                    },
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-26T10:06:50.628247+06:00"
                },
                {
                    "id": 26673,
                    "type": "update",
                    "model": "Invoice",
                    "object": 395,
                    "user_name": "admin",
                    "email": "admin@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "status": {
                            "to": "draft",
                            "from": "sent"
                        },
                        "items": []
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-26T10:06:47.609181+06:00"
                },
                {
                    "id": 26671,
                    "type": "update",
                    "model": "Invoice",
                    "object": 395,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "is_sent_to_client": {
                            "to": true,
                            "from": false
                        },
                        "items": [
                            {
                                "type": "update",
                                "object": 415,
                                "changes": {},
                                "status": "success",
                                "item": "Alu"
                            }
                        ]
                    },
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-26T09:59:01.477854+06:00"
                },
                {
                    "id": 26668,
                    "type": "update",
                    "model": "Invoice",
                    "object": 395,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "status": {
                            "to": "sent",
                            "from": "draft"
                        },
                        "sent_date": {
                            "to": "2025-05-26T00:00:00",
                            "from": null
                        },
                        "items": [
                            {
                                "type": "update",
                                "object": 415,
                                "changes": {},
                                "status": "success",
                                "item": "Alu"
                            }
                        ]
                    },
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-26T09:58:56.114093+06:00"
                },
                {
                    "id": 26664,
                    "type": "create",
                    "model": "Invoice",
                    "object": 395,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": null,
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-26T09:35:05.244907+06:00"
                }
            ],
            "sent_accounting_software": [],
            "currency": {
                "current_rate": 1,
                "name": "Afghan Afghani",
                "prefix": "Afs",
                "short_key": "AFN",
                "flag": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAANkSURBVHja7JfPixxFFMc/1d0zs5vJzGaNq2BcVBByiQSyavS6LIKg4ElBkYj6B3jw3wgiGgVFUBQ8exBvioTokjUJKF42EaPgZuMmu73TM+kf9eN56M5OT8TuPsjsJQ+K6up6XfWt7/u+7tdKRNhP89hnuwtAAT7QKfppmgXSAOivrKxs+379/p8QNFr5jRcfqadeKb55/b17AmDO8zyWl5drHzrQkKTlRxdqfX69fgVgLgA6xhjSNCUMQ6SIS9kEUAJG+cWslCIok47A9cgrhlJ4jf0EmJ/tkRoN0AkAnHPEcUySJJWopSEDickq52OdoZ0FyIOqtSaOY+I4/l8AxLr6IG0/IMsZyAEYYxgOh4xGoxoA7YJ2l2ewVwTLyfgewqgGgO/5mDIDxhiiKNoDMKmD8ciJyS+DFv69h0EVXiLYGzehONUorWZSiSKz2SSAwWBQy4AjgyAgeGAeF27jzR/O74fbeL2DmI0NMIYou1WzjiM22aQGoiiq14AvHHr7LZJzqyRrVwi8NgDm2jVmnjxJ9/lnCU+/yyiL95hBqXF/G4A4dFkDWmsGgwFpmlYCCI4dpf3wQ4TvnKFzYolDb74GQPjxpyTnL9B/+SWCxUWG2X8cpACinUFb828NaK2r5d3y0Vf/JFg8QmfpOKNvvwOg8/hx7I0t9NU/oOUzqglBZloEvjfJwHA4rAXgdbv4Dx7B6/dIz19g5umn8rz/cRWv38vnul124t9rzhEwN3Nw/DU0xmCMwVpb2dK1i5jNTSTNUEEL1WnnLWghSYbZ3CRdu4h1rrIZZ8m0mWRARHDOVVO3fhm9/hv9U6+QnP2B6IsvAZhZOkH3hedIfrpEtn4ZJ0erxSwexpVEaI1tBECcZveDD3GnXmX25BPMPpN/wNxOyK3vzxJ99jliNE5q1hG5IwuKQX196KH/2mD3/Y/ILv2M+XsrX+S+BeJzq9jBDgqPJnWmtW4yC3zfr2UADAqFC28y/Pqr0vtSUAQoPMDikNoySLuSBqy1+L7fALkpraHuKKxs0RowKfmee1ngnEMpNb06UCmcKwEQkekCQOGcjENwG0Cv16uRYLvRBr3OgVofKQGwAFEU1T600xBAtBs18BIAq4D7gceABaZrW8Avqvgn6BX9NC0FInX353S/AfwzAGTE9qrU0AqGAAAAAElFTkSuQmCC",
                "id": 15,
                "is_default": true
            },
            "pdf_template_title": "general",
            "chasing_schedules": [],
            "interest_schedules": [],
            "deleted_at": null,
            "created_at": "2025-05-26T09:35:05+06:00",
            "updated_at": "2025-05-26T10:20:53.904373+06:00",
            "invoice_no": "inv00803",
            "invoice_type": "general",
            "is_auto_generated": false,
            "due_date": "2025-06-12",
            "issue_date": "2025-01-15",
            "sent_date": "2025-05-26",
            "amount": 37.8,
            "default_currency_amount": 37.8,
            "tax_type": "inclusive",
            "tax_amount": 4.05,
            "payable_amount": 37.8,
            "last_chased_payable_amount": 0,
            "paid": 0,
            "due": 37.8,
            "status": "sent",
            "payment_status": "due",
            "references": null,
            "should_send_to_client": true,
            "is_sent_to_client": true,
            "company": 11,
            "pdf_template": 2
        }
    }
}
```
