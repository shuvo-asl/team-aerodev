# Invoice Status Change

**PATCH** `{{url}}/api/invoice-status-change/305/`

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
    "should_send_to_client": true
}
```

## Examples

### Invoice Status Change

**Request:** `PATCH` `{{url}}/api/invoice-status-change/380/`

```json
{
    "status": "sent",
    "should_send_to_client": true,
    "email_subject": "email from invoice status change",
    "email_body": "email body sample",
    "include_attachments": true,
    "include_payment_url": true,
    "send_myself_a_copy": false,
    "cc": [],
    "bcc": []
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice Status' Successfully Updated",
    "data": {
        "result": {
            "id": 380,
            "deleted_at": null,
            "created_at": "2025-05-25T11:10:40.968804+06:00",
            "updated_at": "2025-05-26T10:25:13.587730+06:00",
            "invoice_no": "inv009",
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
                    "currency": 1,
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
                    13
                ]
            },
            "currency": {
                "currency": 1,
                "current_rate": 1,
                "name": "Afghan Afghani",
                "prefix": "Afs",
                "short_key": "AFN",
                "flag": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAANkSURBVHja7JfPixxFFMc/1d0zs5vJzGaNq2BcVBByiQSyavS6LIKg4ElBkYj6B3jw3wgiGgVFUBQ8exBvioTokjUJKF42EaPgZuMmu73TM+kf9eN56M5OT8TuPsjsJQ+K6up6XfWt7/u+7tdKRNhP89hnuwtAAT7QKfppmgXSAOivrKxs+379/p8QNFr5jRcfqadeKb55/b17AmDO8zyWl5drHzrQkKTlRxdqfX69fgVgLgA6xhjSNCUMQ6SIS9kEUAJG+cWslCIok47A9cgrhlJ4jf0EmJ/tkRoN0AkAnHPEcUySJJWopSEDickq52OdoZ0FyIOqtSaOY+I4/l8AxLr6IG0/IMsZyAEYYxgOh4xGoxoA7YJ2l2ewVwTLyfgewqgGgO/5mDIDxhiiKNoDMKmD8ciJyS+DFv69h0EVXiLYGzehONUorWZSiSKz2SSAwWBQy4AjgyAgeGAeF27jzR/O74fbeL2DmI0NMIYou1WzjiM22aQGoiiq14AvHHr7LZJzqyRrVwi8NgDm2jVmnjxJ9/lnCU+/yyiL95hBqXF/G4A4dFkDWmsGgwFpmlYCCI4dpf3wQ4TvnKFzYolDb74GQPjxpyTnL9B/+SWCxUWG2X8cpACinUFb828NaK2r5d3y0Vf/JFg8QmfpOKNvvwOg8/hx7I0t9NU/oOUzqglBZloEvjfJwHA4rAXgdbv4Dx7B6/dIz19g5umn8rz/cRWv38vnul124t9rzhEwN3Nw/DU0xmCMwVpb2dK1i5jNTSTNUEEL1WnnLWghSYbZ3CRdu4h1rrIZZ8m0mWRARHDOVVO3fhm9/hv9U6+QnP2B6IsvAZhZOkH3hedIfrpEtn4ZJ0erxSwexpVEaI1tBECcZveDD3GnXmX25BPMPpN/wNxOyK3vzxJ99jliNE5q1hG5IwuKQX196KH/2mD3/Y/ILv2M+XsrX+S+BeJzq9jBDgqPJnWmtW4yC3zfr2UADAqFC28y/Pqr0vtSUAQoPMDikNoySLuSBqy1+L7fALkpraHuKKxs0RowKfmee1ngnEMpNb06UCmcKwEQkekCQOGcjENwG0Cv16uRYLvRBr3OgVofKQGwAFEU1T600xBAtBs18BIAq4D7gceABaZrW8Avqvgn6BX9NC0FInX353S/AfwzAGTE9qrU0AqGAAAAAElFTkSuQmCC",
                "id": 15,
                "is_default": true
            },
            "pdf_template": 2,
            "invoice_items": [
                {
                    "id": 400,
                    "flight_no": null,
                    "deleted_at": null,
                    "created_at": "2025-05-25T11:10:41.063209+06:00",
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
                    "invoice": 380,
                    "flight": null,
                    "coa": 51
                }
            ],
            "files": [],
            "sent_accounting_software": [],
            "pdf_template_title": "general",
            "log": [
                {
                    "id": 26695,
                    "type": "update",
                    "model": "Invoice",
                    "object": 380,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "is_sent_to_client": {
                            "to": true,
                            "from": false
                        },
                        "items": []
                    },
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-26T10:25:13.599445+06:00"
                },
                {
                    "id": 26692,
                    "type": "update",
                    "model": "Invoice",
                    "object": 380,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "status": {
                            "to": "sent",
                            "from": "approve"
                        },
                        "sent_date": {
                            "to": "2025-05-26T00:00:00",
                            "from": null
                        },
                        "items": []
                    },
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-26T10:25:08.470064+06:00"
                },
                {
                    "id": 26691,
                    "type": "update",
                    "model": "Invoice",
                    "object": 380,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": {
                        "status": {
                            "to": "approve",
                            "from": "draft"
                        },
                        "items": []
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-26T10:25:01.302412+06:00"
                },
                {
                    "id": 26331,
                    "type": "create",
                    "model": "Invoice",
                    "object": 380,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.21.0.1",
                    "changes": null,
                    "agent_info": "PostmanRuntime/7.44.0",
                    "status": "success",
                    "created_at": "2025-05-25T11:10:41.065346+06:00"
                }
            ]
        }
    }
}
```
