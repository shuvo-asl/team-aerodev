# Invoice Create

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
[{'name': 'client', 'type': 'text', 'value': '2'}, {'name': 'currency', 'type': 'text', 'value': '2'}, {'name': 'status', 'type': 'text', 'value': 'draft'}, {'name': 'invoice_type', 'type': 'text', 'value': 'general'}, {'name': 'amount', 'type': 'text', 'value': '50'}, {'name': 'tax_amount', 'type': 'text', 'value': '0'}, {'name': 'payable_amount', 'type': 'text', 'value': '50'}, {'name': 'tax_type', 'type': 'text', 'value': 'exclusive'}, {'name': 'items', 'type': 'text', 'value': '[{"name":"item1","coa":65,"description":"description","unit":1,"unit_price":20,"discount_rate":null,"discount_amount":"0.00","sub_total":20,"tax_rate":13,"tax_amount":"0.00","total":20,"coa_name":"200 - Sales","tax_id":13},{"name":"item2","coa":65,"description":"description2","unit":1,"unit_price":30,"discount":"0","sub_total":30,"tax_rate":13,"tax_amount":"0.00","total":30,"discount_amount":"0.00","coa_name":"200 - Sales","tax_id":13,"discount_rate":null}]'}, {'name': 'files_to_add', 'type': 'file', 'value': []}, {'name': 'pdf_template', 'type': 'text', 'value': '5'}, {'name': 'issue_date', 'type': 'text', 'value': datetime.date(2025, 8, 13)}, {'name': 'interest rules', 'type': 'text', 'value': '[26]'}, {'name': 'chasing_rules', 'type': 'text', 'value': '[11]'}, {'name': 'due_date', 'type': 'text', 'value': '2025-8-28'}, {'name': 'pdf_template', 'type': 'text', 'value': '13'}, {'name': 'invoice_no', 'type': 'text', 'value': '03'}, {'name': 'prefix', 'type': 'text', 'value': 'inv-'}]
```

## Examples

### create invoice with sent status

**Request:** `POST` `{{url}}/api/invoice/`

```json
[{'name': 'client', 'type': 'text', 'value': '30'}, {'name': 'currency', 'type': 'text', 'value': '15'}, {'name': 'status', 'type': 'text', 'value': 'sent'}, {'name': 'invoice_type', 'type': 'text', 'value': 'general'}, {'name': 'amount', 'type': 'text', 'value': '37.80'}, {'name': 'tax_amount', 'type': 'text', 'value': '4.05'}, {'name': 'payable_amount', 'type': 'text', 'value': '37.80'}, {'name': 'tax_type', 'type': 'text', 'value': 'inclusive'}, {'name': 'items', 'type': 'text', 'value': '[\n        {\n            "name": "Alu",\n            "coa": 51,\n            "description": "dsafsdf",\n            "unit": "2",\n            "unit_price": "21",\n            "tax_amount": 4.05,\n            "tax_rate": 12,\n            "sub_total": "42",\n            "discount_amount": "4.2",\n            "total": "37.8",\n            "coa_name": "COA - 227"\n        }\n    ]'}, {'name': 'files_to_add', 'type': 'file', 'value': []}, {'name': 'pdf_template', 'type': 'text', 'value': '1'}, {'name': 'issue_date', 'type': 'text', 'value': datetime.date(2025, 1, 15)}, {'name': 'chasing_rules', 'type': 'text', 'value': '45', 'disabled': True}, {'name': 'chasing_rules', 'type': 'text', 'value': '46', 'disabled': True}, {'name': 'due_date', 'type': 'text', 'value': '2025-6-12'}, {'name': 'pdf_template', 'type': 'text', 'value': '2'}, {'name': 'invoice_no', 'type': 'text', 'value': 'inv00806'}, {'name': 'should_send_to_client', 'type': 'text', 'value': 'true'}, {'name': 'email_subject', 'type': 'text', 'value': 'from invoice create'}, {'name': 'email_body', 'type': 'text', 'value': 'email body'}, {'name': 'include_attachments', 'type': 'text', 'value': 'true'}, {'name': 'include_payment_url', 'type': 'text', 'value': 'true'}, {'name': 'cc[0]', 'type': 'text', 'value': 'kamrul@asl.aero'}, {'name': 'cc[1]', 'type': 'text', 'value': 'test@gmail.com'}]
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Invoice successfully created",
    "data": {
        "result": {
            "id": 401,
            "invoice_items": [
                {
                    "id": 421,
                    "flight_no": null,
                    "deleted_at": null,
                    "created_at": "2025-05-27T14:18:08.351781+06:00",
                    "updated_at": null,
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
                    "invoice": 401,
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
                    "id": 27195,
                    "type": "update",
                    "model": "Invoice",
                    "object": 401,
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
                                "type": "create",
                                "object": 421,
                                "changes": {},
                                "status": "success",
                                "item": "Alu"
                            }
                        ]
                    },
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-27T14:18:08.767684+06:00"
                },
                {
                    "id": 27191,
                    "type": "create",
                    "model": "Invoice",
                    "object": 401,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": null,
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-27T14:18:08.353667+06:00"
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
            "created_at": "2025-05-27T14:18:08.258952+06:00",
            "updated_at": "2025-05-27T14:18:08.755227+06:00",
            "invoice_no": "inv00806",
            "invoice_type": "general",
            "is_auto_generated": false,
            "due_date": "2025-06-12",
            "issue_date": "2025-01-15",
            "sent_date": "2025-05-27",
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

### Invoice Create

**Request:** `POST` `{{url}}/api/invoice/`

```json
[{'name': 'client', 'type': 'text', 'value': '17'}, {'name': 'currency', 'type': 'text', 'value': '86'}, {'name': 'status', 'type': 'text', 'value': 'draft'}, {'name': 'invoice_type', 'type': 'text', 'value': 'general'}, {'name': 'amount', 'type': 'text', 'value': '20'}, {'name': 'tax_amount', 'type': 'text', 'value': '0'}, {'name': 'payable_amount', 'type': 'text', 'value': '20'}, {'name': 'tax_type', 'type': 'text', 'value': 'exclusive'}, {'name': 'items', 'type': 'text', 'value': '[{"name":"","coa":721,"description":"des","unit":1,"unit_price":20,"discount_rate":null,"discount_amount":"0.00","sub_total":20,"tax_rate":107,"tax_amount":"0.00","total":20,"coa_name":"200 - Sales","tax_id":107}]'}, {'name': 'files_to_add', 'type': 'file', 'value': []}, {'name': 'pdf_template', 'type': 'text', 'value': '1'}, {'name': 'issue_date', 'type': 'text', 'value': datetime.date(2025, 8, 13)}, {'name': 'interest rules', 'type': 'text', 'value': '[19]'}, {'name': 'chasing_rules', 'type': 'text', 'value': '[17]'}, {'name': 'due_date', 'type': 'text', 'value': '2025-8-28'}, {'name': 'pdf_template', 'type': 'text', 'value': '13'}, {'name': 'invoice_no', 'type': 'text', 'value': '010134'}, {'name': 'prefix', 'type': 'text', 'value': 'inv-', 'disabled': True}]
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Invoice successfully created",
    "data": {
        "result": {
            "id": 275,
            "invoice_items": [
                {
                    "id": 407,
                    "flight_no": null,
                    "description": "des",
                    "tax_rate_name": "Tax on Sales",
                    "tax_rate_rate": 0,
                    "deleted_at": "3000-01-01T00:00:00+06:00",
                    "created_at": "2025-08-18T09:32:05.434802+06:00",
                    "updated_at": null,
                    "name": "",
                    "unit_price": 20,
                    "unit": 1,
                    "sub_total": 20,
                    "discount_rate": null,
                    "discount_amount": 0,
                    "tax_rate_old": 0,
                    "tax_amount": 0,
                    "total": 20,
                    "coa_name": "200 - Sales",
                    "invoice": 275,
                    "flight": null,
                    "tax_rate": 107,
                    "coa": 721
                }
            ],
            "client": {
                "id": 17,
                "name": "US Bangla",
                "short_code": "USB",
                "email": "kamrul@asl.aero",
                "phone": "+8801558250667",
                "billing_address": "Dhaka, Bangladesh",
                "days_to_due_date": 15,
                "client_type": "operator",
                "preferred_currency": {
                    "current_rate": 1,
                    "name": "Bangladeshi Taka",
                    "prefix": "৳",
                    "short_key": "BDT",
                    "flag": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAANsSURBVHja7JdBixxFFMd/VdXrZBd3Jll33YBJFlbdQ1BCggFvBhECEs+5eBI9CH4JLwZPHvYk5APk4MmLp4h4USOaBbOsqEQHs8gquO72zPZMV9V7HrpnticzmR0RZi958Pp1dVe9+le99+96bVSV4xTLMctjAAZwQK2005QIdBOg/trNd/92ZrrzW2P47K31hQRoWGN59bnLUwWwufMLQCMBakEi3ZDzT5aiKKYfHQBFy1ZhTeWZKe8GY9q79t6Z/ujiemp2nm7wALUEQETIfJdOyI9E3ugqZ1rK6r5iFZp1Q3PesFszE68+8zleIgAJgNdI5jtkvjN24OqecrUprLQUJ8Wzi8DvdcPtM5athclAPOES8mIHCgAhBlp5RnsMgDfuR17/TVADYkAq71YO4O0/4MtnLLfWHHIEDmcdoboDQYW0c0A7z/pxqvq42oxc+1HI7aP5FIFXfoI0N9xaS8ZzXw15zKs74NnPW7Tz4R14fld587tAZwKWdoBr9+CLRsLPpx69DYKQhQoAHyNp94DMdwc6LmbC9Q3BHwhqqw6rvBhkTK6G6xuGjy46/pwFjAHVwvYAqOCrOeAlsN9t0/UlC8pBL29H1raFGEH7c+hhn1674jwAa9vw7HLC/XMPxazs6yXgY6iEQCJp5wAvfqD/uZ2IbclAwk0iDji7Y2mfHh23PMyQOFsNgaeVZ31Ufb6mgbgX+a8lgwLtlmM3G52MMy6hceLJQRoGiUQZXOvWSSWq4KohmEByC1sNO+SvzwITyX04PI59DKgqojKg3zwNdxeUJAjIZOqi8P2i8u0SQ/56qqqEMtwWIMY4EsCDWeXDSw4Xq5NoqdX2oU2C8sFLjgdzOhZAjwW2R8MiSXVI7y7Ce1ccJ3JFRVGRUqvtwtZy5cYlw+bJ0b56WixaBnPAuQRhdLZ9smppZI73vw6IgfhQPlgFp7B+wbF+wQ2dkKPKIC8VGsYYcZowrkK+ed7y1fIM79yLXNmO1MtPRnsG7ixbPn7Bcee0ZSLKaDFnH4CIYMzRab75lOHGZcfnZy0raXEi/lo3bCwZmvXJaWKMQaqHkaqWRcPRsjNn+HTV8H/EYBDRCgBRjIH52tzUSjKtAIigpHvplItihTKfl4EXgaUpI/gL+MGU/wTzpZ2mdIHUPP45PW4A/w4AuDdJwrlEk1YAAAAASUVORK5CYII=",
                    "id": 86,
                    "is_default": true
                },
                "status": "active",
                "chasing_rule": [
                    {
                        "id": 17,
                        "name": "chase in 3 days interval",
                        "is_default": false,
                        "chase_on": "after due date",
                        "is_cumulative": true,
                        "max_repetition": 10,
                        "email_template": 63,
                        "email_template_name": "default",
                        "chasing_days": [
                            3
                        ]
                    }
                ],
                "interest_rule": [
                    {
                        "id": 19,
                        "name": "calculate interest after day 20",
                        "is_default": false,
                        "is_cumulative": false,
                        "max_repetition": null,
                        "interest_type": "percentage",
                        "interest_rate": 15,
                        "interest_base": "invoice_base_amount",
                        "start_day": null,
                        "interest_day": 20
                    }
                ]
            },
            "files": [],
            "log": [
                {
                    "id": 60145,
                    "type": "delete",
                    "model": "Invoice",
                    "object": 275,
                    "user_name": "finance",
                    "email": "finance@asl.aero",
                    "impersonated_by": null,
                    "ip": "172.18.0.1",
                    "changes": null,
                    "agent_info": "PostmanRuntime/7.45.0",
                    "status": "success",
                    "created_at": "2025-08-18T09:32:05.436254+06:00"
                }
            ],
            "sent_accounting_software": [],
            "currency": {
                "current_rate": 1,
                "name": "Bangladeshi Taka",
                "prefix": "৳",
                "short_key": "BDT",
                "flag": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAANsSURBVHja7JdBixxFFMd/VdXrZBd3Jll33YBJFlbdQ1BCggFvBhECEs+5eBI9CH4JLwZPHvYk5APk4MmLp4h4USOaBbOsqEQHs8gquO72zPZMV9V7HrpnticzmR0RZi958Pp1dVe9+le99+96bVSV4xTLMctjAAZwQK2005QIdBOg/trNd/92ZrrzW2P47K31hQRoWGN59bnLUwWwufMLQCMBakEi3ZDzT5aiKKYfHQBFy1ZhTeWZKe8GY9q79t6Z/ujiemp2nm7wALUEQETIfJdOyI9E3ugqZ1rK6r5iFZp1Q3PesFszE68+8zleIgAJgNdI5jtkvjN24OqecrUprLQUJ8Wzi8DvdcPtM5athclAPOES8mIHCgAhBlp5RnsMgDfuR17/TVADYkAq71YO4O0/4MtnLLfWHHIEDmcdoboDQYW0c0A7z/pxqvq42oxc+1HI7aP5FIFXfoI0N9xaS8ZzXw15zKs74NnPW7Tz4R14fld587tAZwKWdoBr9+CLRsLPpx69DYKQhQoAHyNp94DMdwc6LmbC9Q3BHwhqqw6rvBhkTK6G6xuGjy46/pwFjAHVwvYAqOCrOeAlsN9t0/UlC8pBL29H1raFGEH7c+hhn1674jwAa9vw7HLC/XMPxazs6yXgY6iEQCJp5wAvfqD/uZ2IbclAwk0iDji7Y2mfHh23PMyQOFsNgaeVZ31Ufb6mgbgX+a8lgwLtlmM3G52MMy6hceLJQRoGiUQZXOvWSSWq4KohmEByC1sNO+SvzwITyX04PI59DKgqojKg3zwNdxeUJAjIZOqi8P2i8u0SQ/56qqqEMtwWIMY4EsCDWeXDSw4Xq5NoqdX2oU2C8sFLjgdzOhZAjwW2R8MiSXVI7y7Ce1ccJ3JFRVGRUqvtwtZy5cYlw+bJ0b56WixaBnPAuQRhdLZ9smppZI73vw6IgfhQPlgFp7B+wbF+wQ2dkKPKIC8VGsYYcZowrkK+ed7y1fIM79yLXNmO1MtPRnsG7ixbPn7Bcee0ZSLKaDFnH4CIYMzRab75lOHGZcfnZy0raXEi/lo3bCwZmvXJaWKMQaqHkaqWRcPRsjNn+HTV8H/EYBDRCgBRjIH52tzUSjKtAIigpHvplItihTKfl4EXgaUpI/gL+MGU/wTzpZ2mdIHUPP45PW4A/w4AuDdJwrlEk1YAAAAASUVORK5CYII=",
                "id": 86,
                "is_default": true
            },
            "pdf_template_title": "general pdf template",
            "chasing_schedules": [
                {
                    "id": 283,
                    "invoice": 275,
                    "name": "chase in 3 days interval",
                    "chase_on": "after due date",
                    "is_cumulative": true,
                    "max_repetition": 10,
                    "email_template": 63,
                    "email_template_name": "default",
                    "updated_at": null,
                    "chasing_rule": 17,
                    "custom": false,
                    "chasing_days": [
                        3
                    ]
                }
            ],
            "interest_schedules": [],
            "interest_amount": null,
            "deleted_at": "3000-01-01T00:00:00+06:00",
            "created_at": "2025-08-18T09:32:05.251685+06:00",
            "updated_at": null,
            "invoice_no": "010134",
            "prefix": "#",
            "invoice_type": "general",
            "is_auto_generated": false,
            "due_date": "2025-08-28",
            "issue_date": "2025-08-13",
            "sent_date": null,
            "amount": 20,
            "default_currency_amount": 20,
            "tax_type": "exclusive",
            "tax_amount": 0,
            "payable_amount": 20,
            "last_chased_payable_amount": 0,
            "paid": 0,
            "due": 20,
            "status": "draft",
            "payment_status": "due",
            "references": null,
            "should_send_to_client": true,
            "is_sent_to_client": false,
            "reference_invoice_data": null,
            "has_changes": false,
            "company": 40,
            "pdf_template": 13,
            "email_tracking_id": null,
            "accounting_software_tracking_id": null
        }
    }
}
```

### Invoice Create

**Request:** `POST` `{{url}}/api/invoice/`

```json
[{'name': 'client', 'type': 'text', 'value': '2'}, {'name': 'currency', 'type': 'text', 'value': '2'}, {'name': 'status', 'type': 'text', 'value': 'draft'}, {'name': 'invoice_type', 'type': 'text', 'value': 'general'}, {'name': 'amount', 'type': 'text', 'value': '50'}, {'name': 'tax_amount', 'type': 'text', 'value': '0'}, {'name': 'payable_amount', 'type': 'text', 'value': '50'}, {'name': 'tax_type', 'type': 'text', 'value': 'exclusive'}, {'name': 'items', 'type': 'text', 'value': '[{"name":"item1","coa":65,"description":"description","unit":1,"unit_price":20,"discount_rate":null,"discount_amount":"0.00","sub_total":20,"tax_rate":13,"tax_amount":"0.00","total":20,"coa_name":"200 - Sales","tax_id":13},{"name":"item2","coa":65,"description":"description2","unit":1,"unit_price":30,"discount":"0","sub_total":30,"tax_rate":13,"tax_amount":"0.00","total":30,"discount_amount":"0.00","coa_name":"200 - Sales","tax_id":13,"discount_rate":null}]'}, {'name': 'files_to_add', 'type': 'file', 'value': []}, {'name': 'pdf_template', 'type': 'text', 'value': '5'}, {'name': 'issue_date', 'type': 'text', 'value': datetime.date(2025, 8, 13)}, {'name': 'interest rules', 'type': 'text', 'value': '[26]'}, {'name': 'chasing_rules', 'type': 'text', 'value': '[11]'}, {'name': 'due_date', 'type': 'text', 'value': '2025-8-28'}, {'name': 'pdf_template', 'type': 'text', 'value': '13'}, {'name': 'invoice_no', 'type': 'text', 'value': '05'}, {'name': 'prefix', 'type': 'text', 'value': ''}]
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Invoice successfully created",
    "data": {
        "result": {
            "id": 696,
            "invoice_items": [
                {
                    "id": 735,
                    "flight_no": null,
                    "description": "description",
                    "tax_rate_name": "Tax on Sales",
                    "tax_rate_rate": 0,
                    "deleted_at": "3000-01-01T00:00:00+06:00",
                    "created_at": "2025-08-27T11:48:45.857151+06:00",
                    "updated_at": null,
                    "name": "item1",
                    "unit_price": 20,
                    "unit": 1,
                    "sub_total": 20,
                    "discount_rate": null,
                    "discount_amount": 0,
                    "tax_rate_old": 0,
                    "tax_amount": 0,
                    "total": 20,
                    "coa_name": "200 - Sales",
                    "invoice": 696,
                    "flight": null,
                    "tax_rate": 13,
                    "coa": 65
                },
                {
                    "id": 736,
                    "flight_no": null,
                    "description": "description2",
                    "tax_rate_name": "Tax on Sales",
                    "tax_rate_rate": 0,
                    "deleted_at": "3000-01-01T00:00:00+06:00",
                    "created_at": "2025-08-27T11:48:45.861405+06:00",
                    "updated_at": null,
                    "name": "item2",
                    "unit_price": 30,
                    "unit": 1,
                    "sub_total": 30,
                    "discount_rate": null,
                    "discount_amount": 0,
                    "tax_rate_old": 0,
                    "tax_amount": 0,
                    "total": 30,
                    "coa_name": "200 - Sales",
                    "invoice": 696,
                    "flight": null,
                    "tax_rate": 13,
                    "coa": 65
                }
            ],
            "client": {
                "id": 2,
                "name": "client",
                "short_code": "cl13",
                "email": "kamrul@asl.aero",
                "phone": "+12125552368",
                "billing_address": "fr",
                "days_to_due_date": 2,
                "client_type": "operator",
                "preferred_currency": null,
                "status": "active",
                "chasing_rule": [
                    {
                        "id": 11,
                        "name": "proper rule",
                        "is_default": false,
                        "chase_on": "after due date",
                        "is_cumulative": false,
                        "max_repetition": null,
                        "email_template": 1,
                        "email_template_name": "default",
                        "chasing_days": [
                            6,
                            4,
                            3
                        ]
                    }
                ],
                "interest_rule": []
            },
            "files": [],
            "log": [
                {
                    "id": 53587,
                    "type": "delete",
                    "model": "Invoice",
                    "object": 696,
                    "user_name": "admin",
                    "email": "admin@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.18.0.1",
                    "changes": null,
                    "agent_info": "PostmanRuntime/7.45.0",
                    "status": "success",
                    "created_at": "2025-08-27T11:48:45.859339+06:00"
                }
            ],
            "sent_accounting_software": [],
            "currency": {
                "current_rate": 0.008224,
                "name": "United States Dollar",
                "prefix": "$",
                "short_key": "USD",
                "flag": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAALESURBVHja7Jc/aBNxFMc/l0STtqYtihgkYLOYitjuFuwiUgfBUOgSOqS6CNqmRRqLmyjBBDQ4FLRL/TOokEEhgyC4O7RSB0MHWxEtWLGtrW2Su/s9h8ZeUlF7rV4XHzy+995v+d77vnf3fpqIsJ3mYpvtPwENcAPeMjppJlD0APXHj9/44nZvrhh3d45tsvYuAk9GdwM0nTiRkZmZb3L9+jPbuBUDmjyA1zAUIyMviMXaSaVzDPSfJJ3O0V+JqRz9A1acSufQgC+XrlpvJRXCVua06nNXYz36m0kArwtAKUVPTzvJ5FPifR0kk0/pW4/x6jje10GhoEOhaHmx7OtzP50XQDfWOIbb2lISjz+SqakFicVGN4yx2OhWJQh7AAzDJB7vYHDwEclkF4nExnBo6DGz3Rfs959/F8aHGQDKBBSJxEOuXeuit/cemUz3hhBA6d82NfxSKlkStLZekcnJeTl2LC35/Jwt/CsS6LpJT88d7oycJRod5sH9c0Sjw9z/A4Lw8egp0MptLmI9V8br8prPB8WCJYGuK27fPkPk9E2y2T5ORzJks71EIqtxZC2uznd23kJ8y9Vj9zv7MZKGjlROQSg0JKHQZZmYmJVgMLFhDAYTW5YAIBwMJmR8/JPU1Z2XsTF7OL3nkH0PtMj7g20ChDUgHAhczC8tlTAM03ZD52ue258CjwfNX8eBty+bNSBsmmbe5XL2z6yUwu12N3sApve34jFMpKQ7swPs3IGxw2NNgTINRARRpv1tQtbFld3+q3VT3CjTsAgE34/j8/kclWBlZQVqa1cJTO89TI3XiyyvOCNBbQ3LpaK1E5pKVX/B/jkDDaWkQoKPr2hoaHBUgoWFBWhsXCXwLtBCY73fUQJzXxfXKmDqfpPPMu8oAfEDBUwN2AccAfY6vJbPAq+18p3AX0YnrQgsav8vp9tN4PsALYQJa7MTgzkAAAAASUVORK5CYII=",
                "id": 2,
                "is_default": false
            },
            "pdf_template_title": "frr",
            "chasing_schedules": [
                {
                    "id": 874,
                    "invoice": 696,
                    "name": "proper rule",
                    "chase_on": "after due date",
                    "is_cumulative": false,
                    "max_repetition": null,
                    "email_template": 1,
                    "email_template_name": "default",
                    "updated_at": null,
                    "chasing_rule": 11,
                    "custom": false,
                    "chasing_days": [
                        6,
                        4,
                        3
                    ]
                }
            ],
            "interest_schedules": [],
            "interest_amount": null,
            "deleted_at": "3000-01-01T00:00:00+06:00",
            "created_at": "2025-08-27T11:48:45.770281+06:00",
            "updated_at": null,
            "invoice_no": "05",
            "prefix": "",
            "invoice_type": "general",
            "is_auto_generated": false,
            "due_date": "2025-08-28",
            "issue_date": "2025-08-13",
            "sent_date": null,
            "amount": 50,
            "default_currency_amount": 6079.77,
            "tax_type": "exclusive",
            "tax_amount": 0,
            "payable_amount": 50,
            "last_chased_payable_amount": 0,
            "paid": 0,
            "due": 50,
            "status": "draft",
            "payment_status": "due",
            "references": null,
            "should_send_to_client": true,
            "is_sent_to_client": false,
            "reference_invoice_data": null,
            "has_changes": false,
            "company": 1,
            "pdf_template": 13,
            "email_tracking_id": null,
            "accounting_software_tracking_id": null
        }
    }
}
```
