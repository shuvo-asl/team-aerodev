# bulk-flight-details

**GET** `{{url}}/api/flight/bulk-flight-details/?flight_ids=1,2,3,4`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `flight_ids` | `1,2,3,4` | query |

## Examples

### bulk-flight-details

**Request:** `GET` `{{url}}/api/flight/bulk-flight-details/?flight_ids=1,2,3,4`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Bulk flight details retrieved successfully",
    "data": {
        "result": [
            {
                "id": 1,
                "icao": "f123",
                "flight_source": "manual",
                "tracking_start": null,
                "tracking_end": null,
                "company": 1,
                "source_reference_id": "1",
                "call_sign": "c123",
                "flight_no": "f123",
                "flight_type": "overfly",
                "aircraft_registration_no": "12345",
                "flight_origin_type": "international",
                "mtow": 4000,
                "mtow_unit": "kg",
                "covered_distance_nm": 0,
                "src": "DTKA",
                "dest": "NTGA",
                "flight_source_data": null,
                "status": "billed",
                "fir_in": null,
                "fir_out": null,
                "fir_in_route": null,
                "fir_out_route": null,
                "flight_purpose": "passenger_flight",
                "date_of_operation": "2026-01-14",
                "operator": 1,
                "operator_name": "Saudi Arabian Airlines",
                "charges_amount": 160,
                "notes": null,
                "log": [
                    {
                        "id": 328,
                        "type": "update",
                        "model": "Flight",
                        "object": 1,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "status": {
                                "to": "billing",
                                "from": "ready_to_bill"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:14:47.058585Z"
                    },
                    {
                        "id": 326,
                        "type": "update",
                        "model": "Flight",
                        "object": 1,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "attachment": {
                                "operation": "attach",
                                "invoice_no": "103"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:14:47.034387Z"
                    },
                    {
                        "id": 320,
                        "type": "update",
                        "model": "Flight",
                        "object": 1,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "status": {
                                "to": "ready_to_bill",
                                "from": "billing"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:10:26.430881Z"
                    },
                    {
                        "id": 318,
                        "type": "update",
                        "model": "Flight",
                        "object": 1,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "attachment": {
                                "operation": "detach",
                                "invoice_no": "102"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:10:26.408639Z"
                    },
                    {
                        "id": 314,
                        "type": "update",
                        "model": "Flight",
                        "object": 1,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "status": {
                                "to": "billing",
                                "from": "ready_to_bill"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:10:04.310128Z"
                    },
                    {
                        "id": 313,
                        "type": "update",
                        "model": "Flight",
                        "object": 1,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "attachment": {
                                "operation": "attach",
                                "invoice_no": "102"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:10:04.284860Z"
                    },
                    {
                        "id": 288,
                        "type": "create",
                        "model": "Flight",
                        "object": 1,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": null,
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/146.0",
                        "status": "success",
                        "created_at": "2026-01-14T20:00:08.829960Z"
                    }
                ],
                "invoice_id": 3,
                "invoice_no": "INV-103",
                "payment_status": "due",
                "flight_state": null,
                "flight_charges_amount": 160,
                "flight_charges": {},
                "custom_charges": [
                    {
                        "id": 1,
                        "flight": 1,
                        "charge_head": 10,
                        "head_code": "navigation_charge",
                        "unit": 4000,
                        "unit_price": 40,
                        "amount": 160,
                        "description": "",
                        "coa": 54
                    }
                ]
            },
            {
                "id": 2,
                "icao": "f123",
                "flight_source": "manual",
                "tracking_start": null,
                "tracking_end": null,
                "company": 1,
                "source_reference_id": "2",
                "call_sign": "c123",
                "flight_no": "f123",
                "flight_type": "overfly",
                "aircraft_registration_no": "12345",
                "flight_origin_type": "international",
                "mtow": 4000,
                "mtow_unit": "kg",
                "covered_distance_nm": 0,
                "src": "EKYT",
                "dest": "EDPA",
                "flight_source_data": null,
                "status": "billed",
                "fir_in": null,
                "fir_out": null,
                "fir_in_route": null,
                "fir_out_route": null,
                "flight_purpose": "passenger_flight",
                "date_of_operation": "2026-01-14",
                "operator": 1,
                "operator_name": "Saudi Arabian Airlines",
                "charges_amount": 160,
                "notes": null,
                "log": [
                    {
                        "id": 311,
                        "type": "update",
                        "model": "Flight",
                        "object": 2,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "status": {
                                "to": "billing",
                                "from": "ready_to_bill"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:10:04.274093Z"
                    },
                    {
                        "id": 309,
                        "type": "update",
                        "model": "Flight",
                        "object": 2,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "attachment": {
                                "operation": "attach",
                                "invoice_no": "102"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:10:04.242469Z"
                    },
                    {
                        "id": 290,
                        "type": "create",
                        "model": "Flight",
                        "object": 2,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": null,
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/146.0",
                        "status": "success",
                        "created_at": "2026-01-14T20:00:47.952795Z"
                    }
                ],
                "invoice_id": 2,
                "invoice_no": "INV-102",
                "payment_status": "due",
                "flight_state": null,
                "flight_charges_amount": 160,
                "flight_charges": {},
                "custom_charges": [
                    {
                        "id": 2,
                        "flight": 2,
                        "charge_head": 10,
                        "head_code": "navigation_charge",
                        "unit": 4000,
                        "unit_price": 40,
                        "amount": 160,
                        "description": "",
                        "coa": 54
                    }
                ]
            },
            {
                "id": 3,
                "icao": "f123",
                "flight_source": "manual",
                "tracking_start": null,
                "tracking_end": null,
                "company": 1,
                "source_reference_id": "3",
                "call_sign": "c123",
                "flight_no": "f123",
                "flight_type": "landing",
                "aircraft_registration_no": "12345",
                "flight_origin_type": "international",
                "mtow": 4000,
                "mtow_unit": "kg",
                "covered_distance_nm": 0,
                "src": null,
                "dest": null,
                "flight_source_data": null,
                "status": "billing",
                "fir_in": null,
                "fir_out": null,
                "fir_in_route": null,
                "fir_out_route": null,
                "flight_purpose": "passenger_flight",
                "date_of_operation": "2026-01-14",
                "operator": 1,
                "operator_name": "Saudi Arabian Airlines",
                "charges_amount": 160,
                "notes": null,
                "log": [
                    {
                        "id": 306,
                        "type": "update",
                        "model": "Flight",
                        "object": 3,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "status": {
                                "to": "billing",
                                "from": "ready_to_bill"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:07:58.290634Z"
                    },
                    {
                        "id": 305,
                        "type": "update",
                        "model": "Flight",
                        "object": 3,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "attachment": {
                                "operation": "attach",
                                "invoice_no": "101"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:07:58.278674Z"
                    },
                    {
                        "id": 299,
                        "type": "update",
                        "model": "Flight",
                        "object": 3,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "charges_amount": {
                                "to": 21,
                                "from": 212
                            },
                            "flight_origin_type": {
                                "to": "international",
                                "from": "domestic"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/146.0",
                        "status": "success",
                        "created_at": "2026-01-14T20:05:40.760838Z"
                    },
                    {
                        "id": 292,
                        "type": "create",
                        "model": "Flight",
                        "object": 3,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": null,
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/146.0",
                        "status": "success",
                        "created_at": "2026-01-14T20:01:45.324362Z"
                    }
                ],
                "invoice_id": 1,
                "invoice_no": "INV-101",
                "payment_status": "due",
                "flight_state": null,
                "flight_charges_amount": 160,
                "flight_charges": {},
                "custom_charges": [
                    {
                        "id": 3,
                        "flight": 3,
                        "charge_head": 2,
                        "head_code": "landing",
                        "unit": 4000,
                        "unit_price": 40,
                        "amount": 160,
                        "description": "",
                        "coa": 54
                    }
                ]
            },
            {
                "id": 4,
                "icao": "f123",
                "flight_source": "manual",
                "tracking_start": null,
                "tracking_end": null,
                "company": 1,
                "source_reference_id": "4",
                "call_sign": "c123",
                "flight_no": "f123",
                "flight_type": "landing",
                "aircraft_registration_no": "12345",
                "flight_origin_type": "international",
                "mtow": 4000,
                "mtow_unit": "kg",
                "covered_distance_nm": 0,
                "src": null,
                "dest": null,
                "flight_source_data": null,
                "status": "billing",
                "fir_in": null,
                "fir_out": null,
                "fir_in_route": null,
                "fir_out_route": null,
                "flight_purpose": "passenger_flight",
                "date_of_operation": "2026-01-14",
                "operator": 1,
                "operator_name": "Saudi Arabian Airlines",
                "charges_amount": 160,
                "notes": null,
                "log": [
                    {
                        "id": 303,
                        "type": "update",
                        "model": "Flight",
                        "object": 4,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "status": {
                                "to": "billing",
                                "from": "ready_to_bill"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:07:58.260342Z"
                    },
                    {
                        "id": 301,
                        "type": "update",
                        "model": "Flight",
                        "object": 4,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "attachment": {
                                "operation": "attach",
                                "invoice_no": "101"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                        "status": "success",
                        "created_at": "2026-01-14T20:07:58.233422Z"
                    },
                    {
                        "id": 298,
                        "type": "update",
                        "model": "Flight",
                        "object": 4,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": {
                            "charges_amount": {
                                "to": 21,
                                "from": 212
                            },
                            "flight_origin_type": {
                                "to": "international",
                                "from": "domestic"
                            }
                        },
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/146.0",
                        "status": "success",
                        "created_at": "2026-01-14T20:05:28.609689Z"
                    },
                    {
                        "id": 294,
                        "type": "create",
                        "model": "Flight",
                        "object": 4,
                        "user_name": "devs",
                        "email": "devs@aerogon.aero",
                        "impersonated_by": null,
                        "ip": "103.218.25.242",
                        "changes": null,
                        "agent_info": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:146.0) Gecko/20100101 Firefox/146.0",
                        "status": "success",
                        "created_at": "2026-01-14T20:02:15.856937Z"
                    }
                ],
                "invoice_id": 1,
                "invoice_no": "INV-101",
                "payment_status": "due",
                "flight_state": null,
                "flight_charges_amount": 160,
                "flight_charges": {},
                "custom_charges": [
                    {
                        "id": 4,
                        "flight": 4,
                        "charge_head": 2,
                        "head_code": "landing",
                        "unit": 4000,
                        "unit_price": 40,
                        "amount": 160,
                        "description": "",
                        "coa": 54
                    }
                ]
            }
        ]
    }
}
```
