# Single Invoice

**GET** `{{url}}/api/invoice/111/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Non-Aero Single Invoice

**Request:** `GET` `{{url}}/api/invoice/187/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice' Successfully Retrieved",
    "data": {
        "result": {
            "id": 187,
            "client_details": {
                "id": 1,
                "name": "test",
                "short_code": "titas",
                "email": "ismail@asl.aero",
                "phone": "+8801684806728",
                "billing_address": "West Bhurulia 256/13, Gazipur Sadar, Gazipur, Dhaka",
                "created_at": "2024-01-23T15:34:49.531386+06:00",
                "updated_at": "2024-02-08T17:27:50.513010+06:00",
                "is_active": true,
                "client_type": "operator"
            },
            "invoice_no": "INV-000072",
            "invoice_type": "manual",
            "invoice_item_type": "non_aeronautical",
            "due_date": null,
            "sent_date": null,
            "amount": 80,
            "vat": 15,
            "vat_amount": 12,
            "payable_amount": 92,
            "last_chased_payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "is_bundled": false,
            "references": null,
            "created_at": "2024-02-12T10:34:49.420954+06:00",
            "updated_at": "2024-02-12T10:34:49.437562+06:00",
            "client": {
                "id": 1,
                "name": "test",
                "short_code": "titas",
                "email": "ismail@asl.aero",
                "phone": "+8801684806728",
                "billing_address": "West Bhurulia 256/13, Gazipur Sadar, Gazipur, Dhaka",
                "created_at": "2024-01-23T15:34:49.531386+06:00",
                "updated_at": "2024-02-08T17:27:50.513010+06:00",
                "is_active": true,
                "client_type": "operator"
            },
            "billing_flight": {
                "id": 124,
                "aircraft_registration_number": "bbt",
                "call_sign": "223P",
                "flight_no": null,
                "flight_type": "landing",
                "flight_origin_type": "international",
                "src": null,
                "dest": null,
                "mtow": 10642,
                "reference": null,
                "requests": null,
                "arrival_time": null,
                "departure_time": null,
                "status": "pending",
                "created_at": "2024-02-12T10:34:49.402369+06:00",
                "updated_at": "2024-02-12T10:34:49.402407+06:00"
            },
            "currency": {
                "id": 1,
                "prefix": "$",
                "short_key": "USD",
                "rate": 1,
                "default": null,
                "is_active": true
            },
            "updated_by": null,
            "log": [
                {
                    "id": 8749,
                    "action_type": "create",
                    "action_model": "<class 'invoice.models.Invoice'>",
                    "action_object": 187,
                    "action_user": "admin@gmail.com",
                    "action_IP": "192.168.65.1",
                    "action_datetime": "2024-02-12T10:34:49.465142+06:00",
                    "action_agent_info": "PostmanRuntime/7.36.1",
                    "action_status": "success"
                }
            ],
            "items": [
                {
                    "id": 453,
                    "head_code": null,
                    "units": 4,
                    "per_unit_cost": 4,
                    "amount": 16,
                    "description": "4",
                    "created_at": "2024-02-12T10:34:49.427900+06:00",
                    "updated_at": "2024-02-12T10:34:49.427948+06:00",
                    "invoice": 187,
                    "charging_head": null,
                    "coa": 4
                },
                {
                    "id": 454,
                    "head_code": null,
                    "units": 4,
                    "per_unit_cost": 4,
                    "amount": 16,
                    "description": "4",
                    "created_at": "2024-02-12T10:34:49.436279+06:00",
                    "updated_at": "2024-02-12T10:34:49.436311+06:00",
                    "invoice": 187,
                    "charging_head": null,
                    "coa": 4
                }
            ],
            "total_amount": 32
        }
    }
}
```

### Aero Single Invoice

**Request:** `GET` `{{url}}/api/invoice/186/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice' Successfully Retrieved",
    "data": {
        "result": {
            "id": 186,
            "client_details": {
                "id": 1,
                "name": "test",
                "short_code": "titas",
                "email": "ismail@asl.aero",
                "phone": "+8801684806728",
                "billing_address": "West Bhurulia 256/13, Gazipur Sadar, Gazipur, Dhaka",
                "created_at": "2024-01-23T15:34:49.531386+06:00",
                "updated_at": "2024-02-08T17:27:50.513010+06:00",
                "is_active": true,
                "client_type": "operator"
            },
            "invoice_no": "INV-000071",
            "invoice_type": "manual",
            "invoice_item_type": "aeronautical",
            "due_date": null,
            "sent_date": null,
            "amount": 33585.85,
            "vat": 15,
            "vat_amount": 5037.88,
            "payable_amount": 38623.73,
            "last_chased_payable_amount": 0,
            "paid": 0,
            "due": 0,
            "status": "draft",
            "payment_status": "due",
            "is_bundled": false,
            "references": null,
            "created_at": "2024-02-12T10:32:42.968743+06:00",
            "updated_at": "2024-02-12T10:32:43.348001+06:00",
            "client": {
                "id": 1,
                "name": "test",
                "short_code": "titas",
                "email": "ismail@asl.aero",
                "phone": "+8801684806728",
                "billing_address": "West Bhurulia 256/13, Gazipur Sadar, Gazipur, Dhaka",
                "created_at": "2024-01-23T15:34:49.531386+06:00",
                "updated_at": "2024-02-08T17:27:50.513010+06:00",
                "is_active": true,
                "client_type": "operator"
            },
            "billing_flight": {
                "id": 123,
                "aircraft_registration_number": "bbt",
                "call_sign": "223P",
                "flight_no": null,
                "flight_type": "landing",
                "flight_origin_type": "international",
                "src": null,
                "dest": null,
                "mtow": 16332,
                "reference": null,
                "requests": null,
                "arrival_time": null,
                "departure_time": null,
                "status": "pending",
                "created_at": "2024-02-12T10:32:42.949508+06:00",
                "updated_at": "2024-02-12T10:32:42.949547+06:00"
            },
            "currency": {
                "id": 1,
                "prefix": "$",
                "short_key": "USD",
                "rate": 1,
                "default": null,
                "is_active": true
            },
            "updated_by": null,
            "log": [
                {
                    "id": 8748,
                    "action_type": "create",
                    "action_model": "<class 'invoice.models.Invoice'>",
                    "action_object": 186,
                    "action_user": "admin@gmail.com",
                    "action_IP": "192.168.65.1",
                    "action_datetime": "2024-02-12T10:32:43.403526+06:00",
                    "action_agent_info": "PostmanRuntime/7.36.1",
                    "action_status": "success"
                }
            ],
            "final_charge": 33585.85,
            "charges": {
                "embarkation_fees": {
                    "total_charge": 25000,
                    "sub_charges": [
                        {
                            "id": 440,
                            "head_code": "embarkation_fees",
                            "units": 50,
                            "per_unit_cost": 500,
                            "amount": 25000,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.091587+06:00",
                            "updated_at": "2024-02-12T10:32:43.091620+06:00",
                            "invoice": 186,
                            "charging_head": 1,
                            "coa": 1,
                            "head": {
                                "id": 1,
                                "name": "Embarkation Fees",
                                "head_code": "embarkation_fees",
                                "head_value_type": "per_unit",
                                "has_rules": false,
                                "unit_labels": "Passenger",
                                "value": "1",
                                "currency_type": "local",
                                "perform": "NULL",
                                "max_value": null,
                                "static_percentage": "NULL",
                                "min_static_cost": "NULL",
                                "parent": null
                            }
                        }
                    ],
                    "parameter_value": 50
                },
                "landing": {
                    "total_charge": 643.85,
                    "sub_charges": [
                        {
                            "id": 441,
                            "head_code": "landing",
                            "units": 16332,
                            "per_unit_cost": 6.75,
                            "amount": 114.75,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.108408+06:00",
                            "updated_at": "2024-02-12T10:32:43.108441+06:00",
                            "invoice": 186,
                            "charging_head": 2,
                            "coa": 1,
                            "head": {
                                "id": 2,
                                "name": "Landing",
                                "head_code": "landing",
                                "head_value_type": "per_unit",
                                "has_rules": true,
                                "unit_labels": "KG",
                                "value": "1000",
                                "currency_type": "both",
                                "perform": "NULL",
                                "max_value": "NULL",
                                "static_percentage": "NULL",
                                "min_static_cost": "NULL",
                                "parent": null
                            }
                        },
                        {
                            "id": 442,
                            "head_code": "off_time_landing_takeoff",
                            "units": null,
                            "per_unit_cost": 11.475,
                            "amount": 11.475,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.125627+06:00",
                            "updated_at": "2024-02-12T10:32:43.125658+06:00",
                            "invoice": 186,
                            "charging_head": 3,
                            "coa": 1,
                            "head": {
                                "id": 3,
                                "name": "Landing or take off after sunset and before sunrise.",
                                "head_code": "off_time_landing_takeoff",
                                "head_value_type": "in_percentage",
                                "has_rules": false,
                                "unit_labels": "NULL",
                                "value": "NULL",
                                "currency_type": "NULL",
                                "perform": "surcharge",
                                "max_value": "NULL",
                                "static_percentage": "10.00",
                                "min_static_cost": "NULL",
                                "parent": 2
                            }
                        },
                        {
                            "id": 443,
                            "head_code": "training_purpose_discount",
                            "units": null,
                            "per_unit_cost": 57.375,
                            "amount": 57.375,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.143833+06:00",
                            "updated_at": "2024-02-12T10:32:43.143866+06:00",
                            "invoice": 186,
                            "charging_head": 4,
                            "coa": 1,
                            "head": {
                                "id": 4,
                                "name": "Training Purpose Discount",
                                "head_code": "training_purpose_discount",
                                "head_value_type": "in_percentage",
                                "has_rules": false,
                                "unit_labels": "NULL",
                                "value": "NULL",
                                "currency_type": "NULL",
                                "perform": "discount",
                                "max_value": "NULL",
                                "static_percentage": "50.00",
                                "min_static_cost": "NULL",
                                "parent": 2
                            }
                        },
                        {
                            "id": 444,
                            "head_code": "test_flight_discount",
                            "units": null,
                            "per_unit_cost": 86.062,
                            "amount": 86.062,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.168313+06:00",
                            "updated_at": "2024-02-12T10:32:43.168347+06:00",
                            "invoice": 186,
                            "charging_head": 5,
                            "coa": 1,
                            "head": {
                                "id": 5,
                                "name": "Test Fly Discount",
                                "head_code": "test_flight_discount",
                                "head_value_type": "in_percentage",
                                "has_rules": false,
                                "unit_labels": "NULL",
                                "value": "NULL",
                                "currency_type": "NULL",
                                "perform": "discount",
                                "max_value": "NULL",
                                "static_percentage": "75.00",
                                "min_static_cost": "NULL",
                                "parent": 2
                            }
                        },
                        {
                            "id": 445,
                            "head_code": "security_others_international",
                            "units": null,
                            "per_unit_cost": 200,
                            "amount": 200,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.185092+06:00",
                            "updated_at": "2024-02-12T10:32:43.185128+06:00",
                            "invoice": 186,
                            "charging_head": 14,
                            "coa": 1,
                            "head": {
                                "id": 14,
                                "name": "Security & Others For International",
                                "head_code": "security_others_international",
                                "head_value_type": "in_percentage",
                                "has_rules": false,
                                "unit_labels": "NULL",
                                "value": "NULL",
                                "currency_type": "international",
                                "perform": "NULL",
                                "max_value": "NULL",
                                "static_percentage": "15.00",
                                "min_static_cost": "200.00",
                                "parent": 2
                            }
                        },
                        {
                            "id": 446,
                            "head_code": "security_others_local",
                            "units": null,
                            "per_unit_cost": 375,
                            "amount": 375,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.201839+06:00",
                            "updated_at": "2024-02-12T10:32:43.201872+06:00",
                            "invoice": 186,
                            "charging_head": 15,
                            "coa": 1,
                            "head": {
                                "id": 15,
                                "name": "Security & Others For Local",
                                "head_code": "security_others_local",
                                "head_value_type": "in_percentage",
                                "has_rules": false,
                                "unit_labels": "NULL",
                                "value": "NULL",
                                "currency_type": "local",
                                "perform": "NULL",
                                "max_value": "NULL",
                                "static_percentage": "15.00",
                                "min_static_cost": "375.00",
                                "parent": 2
                            }
                        },
                        {
                            "id": 447,
                            "head_code": "parking_charge",
                            "units": 52,
                            "per_unit_cost": 28.688,
                            "amount": 86.062,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.217517+06:00",
                            "updated_at": "2024-02-12T10:32:43.217554+06:00",
                            "invoice": 186,
                            "charging_head": 8,
                            "coa": 1,
                            "head": {
                                "id": 8,
                                "name": "Parking Charge",
                                "head_code": "parking_charge",
                                "head_value_type": "in_percentage",
                                "has_rules": false,
                                "unit_labels": "Hour",
                                "value": "24",
                                "currency_type": "NULL",
                                "perform": "NULL",
                                "max_value": "NULL",
                                "static_percentage": "25.00",
                                "min_static_cost": "NULL",
                                "parent": 2
                            }
                        },
                        {
                            "id": 448,
                            "head_code": "hanger_charge",
                            "units": 0,
                            "per_unit_cost": 0,
                            "amount": 0,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.233769+06:00",
                            "updated_at": "2024-02-12T10:32:43.233802+06:00",
                            "invoice": 186,
                            "charging_head": 9,
                            "coa": 1,
                            "head": {
                                "id": 9,
                                "name": "Hanger Charge",
                                "head_code": "hanger_charge",
                                "head_value_type": "in_percentage",
                                "has_rules": false,
                                "unit_labels": "Hour",
                                "value": "24",
                                "currency_type": "NULL",
                                "perform": "NULL",
                                "max_value": "NULL",
                                "static_percentage": "50.00",
                                "min_static_cost": "NULL",
                                "parent": 8
                            }
                        }
                    ],
                    "parameter_value": 16332
                },
                "navigation_charge": {
                    "total_charge": 0,
                    "sub_charges": [
                        {
                            "id": 449,
                            "head_code": "navigation_charge",
                            "units": 16332,
                            "per_unit_cost": null,
                            "amount": 0,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.249639+06:00",
                            "updated_at": "2024-02-12T10:32:43.249674+06:00",
                            "invoice": 186,
                            "charging_head": 10,
                            "coa": 1,
                            "head": {
                                "id": 10,
                                "name": "Navigation Charge",
                                "head_code": "navigation_charge",
                                "head_value_type": "fixed",
                                "has_rules": true,
                                "unit_labels": "KG",
                                "value": "1000",
                                "currency_type": "both",
                                "perform": "NULL",
                                "max_value": "NULL",
                                "static_percentage": "NULL",
                                "min_static_cost": "NULL",
                                "parent": null
                            }
                        }
                    ],
                    "parameter_value": 16332
                },
                "boarding_bridge_charge": {
                    "total_charge": 7942,
                    "sub_charges": [
                        {
                            "id": 450,
                            "head_code": "boarding_bridge_charge",
                            "units": 2,
                            "per_unit_cost": 100,
                            "amount": 200,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.314729+06:00",
                            "updated_at": "2024-02-12T10:32:43.314763+06:00",
                            "invoice": 186,
                            "charging_head": 11,
                            "coa": 1,
                            "head": {
                                "id": 11,
                                "name": "Boarding Bridge Charge",
                                "head_code": "boarding_bridge_charge",
                                "head_value_type": "per_unit",
                                "has_rules": true,
                                "unit_labels": "Hour",
                                "value": "1",
                                "currency_type": "international",
                                "perform": "NULL",
                                "max_value": "2",
                                "static_percentage": "NULL",
                                "min_static_cost": "NULL",
                                "parent": null
                            }
                        },
                        {
                            "id": 451,
                            "head_code": "boarding_bridge_above_2hour_charge",
                            "units": 68,
                            "per_unit_cost": 60,
                            "amount": 8160,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.331037+06:00",
                            "updated_at": "2024-02-12T10:32:43.331073+06:00",
                            "invoice": 186,
                            "charging_head": 12,
                            "coa": 1,
                            "head": {
                                "id": 12,
                                "name": "Boarding Bridge Above 2 Hour Charge",
                                "head_code": "boarding_bridge_above_2hour_charge",
                                "head_value_type": "per_unit",
                                "has_rules": true,
                                "unit_labels": "Hour",
                                "value": "0.5",
                                "currency_type": "international",
                                "perform": "NULL",
                                "max_value": "NULL",
                                "static_percentage": "NULL",
                                "min_static_cost": "NULL",
                                "parent": 11
                            }
                        },
                        {
                            "id": 452,
                            "head_code": "discount_charge_frequent_boarding_bridge",
                            "units": null,
                            "per_unit_cost": null,
                            "amount": 418,
                            "description": null,
                            "created_at": "2024-02-12T10:32:43.346368+06:00",
                            "updated_at": "2024-02-12T10:32:43.346405+06:00",
                            "invoice": 186,
                            "charging_head": 13,
                            "coa": 1,
                            "head": {
                                "id": 13,
                                "name": "Discount Charge for the frequent users of Boarding Bridges",
                                "head_code": "discount_charge_frequent_boarding_bridge",
                                "head_value_type": "in_percentage",
                                "has_rules": true,
                                "unit_labels": "Hour",
                                "value": "NULL",
                                "currency_type": "NULL",
                                "perform": "discount",
                                "max_value": "NULL",
                                "static_percentage": "NULL",
                                "min_static_cost": "NULL",
                                "parent": 11
                            }
                        }
                    ],
                    "parameter_value": 2
                }
            }
        }
    }
}
```
