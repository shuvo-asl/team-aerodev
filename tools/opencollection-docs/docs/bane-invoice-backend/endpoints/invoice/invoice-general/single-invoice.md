# Single Invoice

**GET** `{{url}}/api/invoice/161/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Single Invoice

**Request:** `GET` `{{url}}/api/invoice/373/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice Fetched Successfully",
    "data": {
        "result": {
            "id": 373,
            "invoice_items": [
                {
                    "id": 378,
                    "flight_no": null,
                    "deleted_at": null,
                    "created_at": "2025-05-04T11:54:12.731483+06:00",
                    "updated_at": "2025-05-05T13:21:25.315870+06:00",
                    "name": "fv",
                    "description": "jgu",
                    "unit_price": 20,
                    "unit": 1,
                    "sub_total": 20,
                    "discount_rate": null,
                    "discount_amount": 0,
                    "tax_rate": 0,
                    "tax_amount": 0,
                    "total": 20,
                    "coa_name": "200 - Sales",
                    "invoice": 373,
                    "flight": null,
                    "coa": 174
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
                    "id": 22755,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.20.0.1",
                    "changes": {
                        "items": [
                            {
                                "type": "update",
                                "object": 378,
                                "changes": {
                                    "description": {
                                        "to": "jgu",
                                        "from": "trghu"
                                    }
                                },
                                "status": "success"
                            }
                        ]
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-05T13:21:25.318538+06:00"
                },
                {
                    "id": 22636,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.20.0.1",
                    "changes": {
                        "items": [
                            {
                                "type": "update",
                                "object": 378,
                                "changes": {
                                    "description": {
                                        "to": "gn2",
                                        "from": "gn"
                                    }
                                },
                                "status": "success"
                            }
                        ]
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-04T15:31:47.619353+06:00"
                },
                {
                    "id": 22634,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "192.168.10.145",
                    "changes": {},
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-04T12:09:48.836749+06:00"
                },
                {
                    "id": 22616,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "192.168.10.145",
                    "changes": {
                        "due": {
                            "to": "20.00",
                            "from": "95.00"
                        },
                        "amount": {
                            "to": "20.00",
                            "from": "95.00"
                        },
                        "tax_type": {
                            "to": "exclusive",
                            "from": "inclusive"
                        },
                        "payable_amount": {
                            "to": 20,
                            "from": "95.00"
                        },
                        "default_currency_amount": {
                            "to": 20,
                            "from": "95.00"
                        }
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-04T11:54:12.734344+06:00"
                },
                {
                    "id": 22610,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "192.168.10.145",
                    "changes": {
                        "due": {
                            "to": "95.00",
                            "from": "97.00"
                        },
                        "amount": {
                            "to": "95.00",
                            "from": "97.00"
                        },
                        "payable_amount": {
                            "to": 95,
                            "from": "97.00"
                        },
                        "default_currency_amount": {
                            "to": 95,
                            "from": "97.00"
                        }
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-04T11:48:37.796326+06:00"
                },
                {
                    "id": 22608,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "192.168.10.145",
                    "changes": {
                        "due": {
                            "to": "97.00",
                            "from": "100.00"
                        },
                        "amount": {
                            "to": "97.00",
                            "from": "100.00"
                        },
                        "payable_amount": {
                            "to": 97,
                            "from": "100.00"
                        },
                        "default_currency_amount": {
                            "to": 97,
                            "from": "100.00"
                        }
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-04T11:46:13.695090+06:00"
                },
                {
                    "id": 22606,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "192.168.10.145",
                    "changes": {
                        "due": {
                            "to": "100.00",
                            "from": "98.00"
                        },
                        "amount": {
                            "to": "100.00",
                            "from": "98.00"
                        },
                        "payable_amount": {
                            "to": 100,
                            "from": "98.00"
                        },
                        "default_currency_amount": {
                            "to": 100,
                            "from": "98.00"
                        }
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-04T11:45:51.022996+06:00"
                },
                {
                    "id": 22604,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "192.168.10.145",
                    "changes": {
                        "due": {
                            "to": "98.00",
                            "from": "23.00"
                        },
                        "amount": {
                            "to": "98.00",
                            "from": "23.00"
                        },
                        "payable_amount": {
                            "to": 98,
                            "from": "23.00"
                        },
                        "default_currency_amount": {
                            "to": 98,
                            "from": "23.00"
                        }
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-04T11:45:18.793425+06:00"
                },
                {
                    "id": 22602,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.20.0.1",
                    "changes": {},
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-04T11:10:30.201785+06:00"
                },
                {
                    "id": 22598,
                    "type": "update",
                    "model": "Invoice",
                    "object": 373,
                    "user_name": "admin1",
                    "email": "admin1@gmail.com",
                    "impersonated_by": null,
                    "ip": "172.20.0.1",
                    "changes": {
                        "due": {
                            "to": "23.00",
                            "from": "35.80"
                        },
                        "amount": {
                            "to": "23.00",
                            "from": "35.80"
                        },
                        "tax_amount": {
                            "to": "0.00",
                            "from": "3.84"
                        },
                        "payable_amount": {
                            "to": 23,
                            "from": "35.80"
                        },
                        "default_currency_amount": {
                            "to": 23,
                            "from": "35.80"
                        }
                    },
                    "agent_info": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
                    "status": "success",
                    "created_at": "2025-05-04T11:09:34.949978+06:00"
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
            "chasing_schedules": [
                {
                    "id": 536,
                    "invoice": 373,
                    "name": "first rule",
                    "chase_on": "after due date",
                    "is_cumulative": true,
                    "max_repetition": 5,
                    "email_template": 14,
                    "email_template_name": "default",
                    "updated_at": null,
                    "chasing_rule": 13,
                    "custom": false,
                    "chasing_days": [
                        3
                    ]
                }
            ],
            "interest_schedules": [
                {
                    "id": 224,
                    "invoice": 373,
                    "name": "first rule",
                    "is_cumulative": false,
                    "max_repetition": null,
                    "interest_type": "fixed",
                    "interest_rate": 20,
                    "interest_base": "invoice_amount_after_interest",
                    "interest_rule": 20,
                    "start_day": null,
                    "custom": false,
                    "interest_day": 5
                }
            ],
            "deleted_at": null,
            "created_at": "2025-05-04T11:08:49.799809+06:00",
            "updated_at": "2025-05-05T13:21:25.287333+06:00",
            "invoice_no": "INV-000327",
            "invoice_type": "general",
            "is_auto_generated": false,
            "due_date": "2025-06-12",
            "issue_date": "2025-01-15",
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
            "company": 11,
            "pdf_template": 2
        }
    }
}
```
