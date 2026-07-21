# Aero Create Invoice

**POST** `{{url}}/api/invoice/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

```
[{'name': 'client', 'type': 'text', 'value': '3'}, {'name': 'currency', 'type': 'text', 'value': '1'}, {'name': 'status', 'type': 'text', 'value': 'approve'}, {'name': 'invoice_type', 'type': 'text', 'value': 'aeronautical'}, {'name': 'amount', 'type': 'text', 'value': '2538'}, {'name': 'tax_amount', 'type': 'text', 'value': '0'}, {'name': 'payable_amount', 'type': 'text', 'value': '2538'}, {'name': 'tax_type', 'type': 'text', 'value': 'inclusive'}, {'name': 'items', 'type': 'text', 'value': '\n[{"description":"International ANC — Overfly, NAVISAT (Overfly)","unit":1,"unit_price":2538,"discount_rate":null,"discount_amount":"0.00","sub_total":2538,"tax_rate":1,"tax_amount":"0.00","total":2538,"flight":19186}]'}, {'name': 'pdf_template', 'type': 'text', 'value': '2'}, {'name': 'detach_flights', 'type': 'text', 'value': '[17, 19]', 'disabled': True}, {'name': 'updated_flights', 'type': 'text', 'value': '[\n{\n    "id": 17,\n    "operator": 107,\n    "flight_origin_type": "local",\n    "flight_type": "landing",\n    "src": "JFK",\n    "dest": "LAX",\n    "mtow": 5000,\n    "mtow_unit": "kg",\n    "charges_amount": 2813.38,\n    "flight_source_data": {\n        "source": "other",\n        "details": {\n            "icao24": "abcd12"\n        }\n    },\n    "flight_charges": {\n        "landing": {\n            "parameter_value": 52,\n            "sub_charges": [\n                {\n                    "id": 37,\n                    "flight": 17,\n                    "charge_head": 2,\n                    "head_code": "landing",\n                    "unit": 5000,\n                    "unit_price": 53,\n                    "amount": 265,\n                    "description": "abcd",\n                    "coa": 1,\n                    "head": {\n                        "id": 2,\n                        "deleted_at": null,\n                        "created_at": "2024-10-09T17:30:45.960369+06:00",\n                        "updated_at": null,\n                        "name": "Landing",\n                        "head_code": "landing",\n                        "head_value_type": "per_unit",\n                        "has_rules": true,\n                        "unit_labels": "KG",\n                        "value": "1000",\n                        "currency_type": "both",\n                        "perform": "NULL",\n                        "max_value": "NULL",\n                        "static_percentage": "NULL",\n                        "min_static_cost": "NULL",\n                        "parent": null\n                    },\n                    "checked_value": true,\n                    "head_code_status": true\n                },\n                {\n                    "id": 38,\n                    "flight": 17,\n                    "charge_head": 3,\n                    "head_code": "off_time_landing_takeoff",\n                    "unit": null,\n                    "unit_price": 26.5,\n                    "amount": 26.5,\n                    "description": "abcd",\n                    "coa": 1,\n                    "head": {\n                        "id": 3,\n                        "deleted_at": null,\n                        "created_at": "2024-10-09T17:30:45.960369+06:00",\n                        "updated_at": null,\n                        "name": "Landing or take off after sunset and before sunrise.",\n                        "head_code": "off_time_landing_takeoff",\n                        "head_value_type": "in_percentage",\n                        "has_rules": false,\n                        "unit_labels": "NULL",\n                        "value": "NULL",\n                        "currency_type": "NULL",\n                        "perform": "surcharge",\n                        "max_value": "NULL",\n                        "static_percentage": "10.00",\n                        "min_static_cost": "NULL",\n                        "parent": 2\n                    },\n                    "checked_value": true,\n                    "head_code_status": true\n                },\n                {\n                    "id": 39,\n                    "flight": 17,\n                    "charge_head": 8,\n                    "head_code": "parking_charge",\n                    "unit": 52,\n                    "unit_price": 66.25,\n                    "amount": 198.75,\n                    "description": null,\n                    "coa": 1,\n                    "head": {\n                        "id": 8,\n                        "deleted_at": null,\n                        "created_at": "2024-10-09T17:30:45.960369+06:00",\n                        "updated_at": null,\n                        "name": "Parking Charge",\n                        "head_code": "parking_charge",\n                        "head_value_type": "in_percentage",\n                        "has_rules": false,\n                        "unit_labels": "Hour",\n                        "value": "24",\n                        "currency_type": "NULL",\n                        "perform": "NULL",\n                        "max_value": "NULL",\n                        "static_percentage": "25.00",\n                        "min_static_cost": "NULL",\n                        "parent": 2\n                    },\n                    "checked_value": true,\n                    "head_code_status": true\n                },\n                {\n                    "amount": 298.125,\n                    "checked_value": true,\n                    "head_code": "hanger_charge",\n                    "unit_price": 99.375,\n                    "unit": 52,\n                    "head": {\n                        "unit_labels": ""\n                    },\n                    "coa": 1,\n                    "head_code_status": true\n                }\n            ]\n        },\n        "boarding_bridge_charge": {\n            "parameter_value": 70,\n            "sub_charges": [\n                {\n                    "id": 41,\n                    "flight": 17,\n                    "charge_head": 11,\n                    "head_code": "boarding_bridge_charge",\n                    "unit": 2,\n                    "unit_price": 0,\n                    "amount": 0,\n                    "description": null,\n                    "coa": 1,\n                    "head": {\n                        "id": 11,\n                        "deleted_at": null,\n                        "created_at": "2024-10-09T17:30:45.960369+06:00",\n                        "updated_at": null,\n                        "name": "Boarding Bridge Charge",\n                        "head_code": "boarding_bridge_charge",\n                        "head_value_type": "per_unit",\n                        "has_rules": true,\n                        "unit_labels": "Hour",\n                        "value": "1",\n                        "currency_type": "international",\n                        "perform": "NULL",\n                        "max_value": "2",\n                        "static_percentage": "NULL",\n                        "min_static_cost": "NULL",\n                        "parent": null\n                    },\n                    "checked_value": true,\n                    "head_code_status": true\n                },\n                {\n                    "id": 42,\n                    "flight": 17,\n                    "charge_head": 12,\n                    "head_code": "boarding_bridge_above_2hour_charge",\n                    "unit": 68,\n                    "unit_price": 0,\n                    "amount": 0,\n                    "description": null,\n                    "coa": 1,\n                    "head": {\n                        "id": 12,\n                        "deleted_at": null,\n                        "created_at": "2024-10-09T17:30:45.960369+06:00",\n                        "updated_at": null,\n                        "name": "Boarding Bridge Above 2 Hour Charge",\n                        "head_code": "boarding_bridge_above_2hour_charge",\n                        "head_value_type": "per_unit",\n                        "has_rules": true,\n                        "unit_labels": "Hour",\n                        "value": "0.5",\n                        "currency_type": "international",\n                        "perform": "NULL",\n                        "max_value": "NULL",\n                        "static_percentage": "NULL",\n                        "min_static_cost": "NULL",\n                        "parent": 11\n                    },\n                    "checked_value": true,\n                    "head_code_status": true\n                },\n                {\n                    "id": 43,\n                    "flight": 17,\n                    "charge_head": 13,\n                    "head_code": "discount_charge_frequent_boarding_bridge",\n                    "unit": null,\n                    "unit_price": null,\n                    "amount": 0,\n                    "description": null,\n                    "coa": 1,\n                    "head": {\n                        "id": 13,\n                        "deleted_at": null,\n                        "created_at": "2024-10-09T17:30:45.960369+06:00",\n                        "updated_at": null,\n                        "name": "Discount Charge for the frequent users of Boarding Bridges",\n                        "head_code": "discount_charge_frequent_boarding_bridge",\n                        "head_value_type": "in_percentage",\n                        "has_rules": true,\n                        "unit_labels": "Hour",\n                        "value": "NULL",\n                        "currency_type": "NULL",\n                        "perform": "discount",\n                        "max_value": "NULL",\n                        "static_percentage": "NULL",\n                        "min_static_cost": "NULL",\n                        "parent": 11\n                    },\n                    "checked_value": true,\n                    "head_code_status": true\n                }\n            ]\n        },\n        "navigation_charge": {\n            "parameter_value": 0,\n            "sub_charges": [\n                {\n                    "id": 40,\n                    "flight": 17,\n                    "charge_head": 10,\n                    "head_code": "navigation_charge",\n                    "unit": 5000,\n                    "unit_price": 150,\n                    "amount": 750,\n                    "description": null,\n                    "coa": 1,\n                    "head": {\n                        "id": 10,\n                        "deleted_at": null,\n                        "created_at": "2024-10-09T17:30:45.960369+06:00",\n                        "updated_at": null,\n                        "name": "Navigation Charge",\n                        "head_code": "navigation_charge",\n                        "head_value_type": "fixed",\n                        "has_rules": true,\n                        "unit_labels": "KG",\n                        "value": "1000",\n                        "currency_type": "both",\n                        "perform": "NULL",\n                        "max_value": "NULL",\n                        "static_percentage": "NULL",\n                        "min_static_cost": "NULL",\n                        "parent": null\n                    },\n                    "checked_value": true,\n                    "head_code_status": true\n                }\n            ]\n        },\n        "embarkation_fees": {\n            "parameter_value": 50,\n            "sub_charges": [\n                {\n                    "id": 36,\n                    "flight": 17,\n                    "charge_head": 1,\n                    "head_code": "embarkation_fees",\n                    "unit": 50,\n                    "unit_price": 25,\n                    "amount": 1250,\n                    "description": null,\n                    "coa": 1,\n                    "head": {\n                        "id": 1,\n                        "deleted_at": null,\n                        "created_at": "2024-10-09T17:30:45.960369+06:00",\n                        "updated_at": null,\n                        "name": "Embarkation Fees",\n                        "head_code": "embarkation_fees",\n                        "head_value_type": "per_unit",\n                        "has_rules": false,\n                        "unit_labels": "Passenger",\n                        "value": "1",\n                        "currency_type": "local",\n                        "perform": "NULL",\n                        "max_value": null,\n                        "static_percentage": "NULL",\n                        "min_static_cost": "NULL",\n                        "parent": null\n                    },\n                    "checked_value": true,\n                    "head_code_status": true\n                }\n            ]\n        }\n    },\n    "custom_charges": [\n        {\n            "id": 44,\n            "flight": 17,\n            "charge_head": null,\n            "head_code": "Fine",\n            "unit": 1,\n            "unit_price": 25,\n            "amount": 25,\n            "description": null,\n            "coa": 1\n        }\n    ]\n}\n\n\n\n]', 'disabled': True}, {'name': 'due_date', 'type': 'text', 'value': '2026-8-28'}, {'name': 'issue_date', 'type': 'text', 'value': '2026-5-12'}, {'name': 'invoice_no', 'type': 'text', 'value': 'M10055'}, {'name': 'billing_period_start', 'type': 'text', 'value': ''}, {'name': 'billing_period_end', 'type': 'text', 'value': ''}]
```

## Examples

### Aero Create Invoice

**Request:** `POST` `{{url}}/api/invoice/`

```json
[{'name': 'client', 'type': 'text', 'value': '1'}, {'name': 'currency', 'type': 'text', 'value': '1'}, {'name': 'status', 'type': 'text', 'value': 'approve'}, {'name': 'invoice_type', 'type': 'text', 'value': 'aeronautical'}, {'name': 'amount', 'type': 'text', 'value': '20'}, {'name': 'tax_amount', 'type': 'text', 'value': '0'}, {'name': 'payable_amount', 'type': 'text', 'value': '20'}, {'name': 'tax_type', 'type': 'text', 'value': 'inclusive'}, {'name': 'items', 'type': 'text', 'value': '[\n        {\n            "name": "Alu",\n            "coa": 27,\n            "description": "dsafsdf",\n            "unit": "2",\n            "unit_price": "10",\n            "tax_amount": 0,\n            "tax_rate": 0,\n            "sub_total": "20",\n            "discount_amount": "0",\n            "total": "20",\n            "coa_name": "COA - 227",\n            "flight": 1\n        }\n        \n]'}, {'name': 'pdf_template', 'type': 'text', 'value': '1'}]
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Invoice successfully created",
    "data": {
        "result": {
            "id": 21,
            "invoice_items": [
                {
                    "id": 20,
                    "deleted_at": null,
                    "created_at": "2024-12-05T10:52:25.484246+06:00",
                    "updated_at": null,
                    "name": "Alu",
                    "description": "dsafsdf",
                    "unit_price": 10,
                    "unit": 2,
                    "sub_total": 20,
                    "discount_rate": null,
                    "discount_amount": 0,
                    "tax_rate": 0,
                    "tax_amount": 0,
                    "total": 20,
                    "coa_name": "COA - 227",
                    "invoice": 21,
                    "flight": 1,
                    "coa": 27
                }
            ],
            "client": {
                "id": 1,
                "name": "Operator",
                "short_code": "01",
                "email": "operator@asl.aero",
                "phone": "+8801684806728",
                "billing_address": "airport",
                "days_to_due_date": 14,
                "client_type": "agent",
                "preferred_currency": null,
                "status": "active",
                "chasing_rule": null
            },
            "files": [],
            "log": [
                {
                    "id": 3620,
                    "type": "create",
                    "model": "Invoice",
                    "object": 21,
                    "user_name": "admin",
                    "email": "admin@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.20.0.1",
                    "changes": {
                        "due": {
                            "to": "20",
                            "from": null
                        },
                        "paid": {
                            "to": 0,
                            "from": null
                        },
                        "amount": {
                            "to": "20.00",
                            "from": null
                        },
                        "client": {
                            "to": 1,
                            "from": null
                        },
                        "status": {
                            "to": "approve",
                            "from": null
                        },
                        "currency": {
                            "to": 1,
                            "from": null
                        },
                        "tax_type": {
                            "to": "inclusive",
                            "from": null
                        },
                        "invoice_no": {
                            "to": "INV-000021",
                            "from": null
                        },
                        "tax_amount": {
                            "to": "0.00",
                            "from": null
                        },
                        "invoice_type": {
                            "to": "aeronautical",
                            "from": null
                        },
                        "pdf_template": {
                            "to": 1,
                            "from": null
                        },
                        "payable_amount": {
                            "to": 20,
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
                    "agent_info": "PostmanRuntime/7.43.0",
                    "status": "success",
                    "created_at": "2024-12-05T10:52:25.487443+06:00"
                }
            ],
            "sent_accounting_software": [],
            "currency": {
                "id": 1,
                "prefix": "$",
                "short_key": "USD",
                "current_rate": 1,
                "default": true,
                "name": "Dollar",
                "flag": "http://localhost:5011/api/media/download.png",
                "is_active": true
            },
            "pdf_template_title": "Finance Pdf",
            "deleted_at": null,
            "created_at": "2024-12-05T10:52:25.473465+06:00",
            "updated_at": null,
            "invoice_no": "INV-000021",
            "invoice_type": "aeronautical",
            "is_auto_generated": false,
            "due_date": null,
            "issue_date": null,
            "sent_date": null,
            "amount": 20,
            "tax_type": "inclusive",
            "tax_amount": 0,
            "payable_amount": 20,
            "last_chased_payable_amount": 0,
            "paid": 0,
            "due": 20,
            "status": "approve",
            "payment_status": "due",
            "references": null,
            "company": null,
            "pdf_template": 1
        }
    }
}
```
