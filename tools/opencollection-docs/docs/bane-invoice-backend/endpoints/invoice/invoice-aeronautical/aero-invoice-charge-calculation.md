# Aero Invoice Charge Calculation

**POST** `{{url}}/api/flight-charge-calculation/`

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
    "flight_origin_type":"international",
    "flight_type": "landing",
    "call_sign": "abc",
    "mtow": 5000,
    "charges": {
        "embarkation_fees":{
            "parameter_value": 50,
            "sub_charges":{
                "embarkation_fees": true
            }
        },
        "landing":{
            "parameter_value": 52,
            "sub_charges":{
                "off_time_landing_takeoff": true,
                "training_purpose_discount": false,
                "test_flight_discount": false,
                "security_others_international": false,
                "security_others_local": false,
                "parking_charge": true,
                "hanger_charge": false,
                "landing": true
            }
        },
        "navigation_charge":{
            "sub_charges":{
                "navigation_charge": true
            }
        },
        "boarding_bridge_charge":{
            "parameter_value": 58,
            "sub_charges":{
                "boarding_bridge_charge": true,
                "boarding_bridge_above_2hour_charge": true,
                "discount_charge_frequent_boarding_bridge": true
            }
        }
    }
}
```

## Examples

### Aero Invoice Charge Calculation

**Request:** `POST` `{{url}}/api/invoice-charge/`

```json
{
    "invoice_item_type": "aeronautical",
    "flight_origin_type": "international",
    "charges": {
        "embarkation_fees":{
            "parameter_value": 50,
            "sub_charges":[
                {"embarkation_fees": true, "coa": 1}
            ]
        },
        "landing":{
            "parameter_value": 52,
            "sub_charges":[
                {"landing": true, "coa": 1},
                {"off_time_landing_takeoff": true, "coa": 1},
                {"training_purpose_discount": true, "coa": 1},
                {"test_flight_discount": true, "coa": 1},
                {"security_others_international": true , "coa": 1},
                {"security_others_local": true , "coa": 1},
                {"parking_charge": true , "coa": 1},
                {"hanger_charge": false , "coa": 1}
            ]
        },
        "navigation_charge":{
            "sub_charges":[
                {"navigation_charge": true, "coa": 1}
            ]
        },
        "boarding_bridge_charge":{
            "parameter_value": 70,
            "sub_charges":[
                {"boarding_bridge_charge": true , "coa": 1},
                {"boarding_bridge_above_2hour_charge": true , "coa": 1},
                {"discount_charge_frequent_boarding_bridge": true , "coa": 1}
            ]
        }
    }
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice' Charge Calculation Updated",
    "data": {
        "result": {
            "final_charge": 33517,
            "charges": {
                "embarkation_fees": {
                    "total_charge": 25000,
                    "sub_charges": [
                        {
                            "head_code": "embarkation_fees",
                            "coa": 1,
                            "per_unit_cost": 500,
                            "units": 50,
                            "amount": 25000,
                            "charging_head": 1,
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
                    "total_charge": 575,
                    "sub_charges": [
                        {
                            "head_code": "landing",
                            "coa": 1,
                            "per_unit_cost": null,
                            "units": 25091,
                            "amount": 0,
                            "charging_head": 2,
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
                            "head_code": "off_time_landing_takeoff",
                            "coa": 1,
                            "per_unit_cost": 0,
                            "units": null,
                            "amount": 0,
                            "charging_head": 3,
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
                            "head_code": "training_purpose_discount",
                            "coa": 1,
                            "per_unit_cost": 0,
                            "units": null,
                            "amount": 0,
                            "charging_head": 4,
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
                            "head_code": "test_flight_discount",
                            "coa": 1,
                            "per_unit_cost": 0,
                            "units": null,
                            "amount": 0,
                            "charging_head": 5,
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
                            "head_code": "security_others_international",
                            "coa": 1,
                            "per_unit_cost": 200,
                            "units": null,
                            "amount": 200,
                            "charging_head": 14,
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
                            "head_code": "security_others_local",
                            "coa": 1,
                            "per_unit_cost": 375,
                            "units": null,
                            "amount": 375,
                            "charging_head": 15,
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
                            "head_code": "parking_charge",
                            "coa": 1,
                            "per_unit_cost": 0,
                            "units": 52,
                            "amount": 0,
                            "charging_head": 8,
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
                            "head_code": "hanger_charge",
                            "coa": 1,
                            "per_unit_cost": 0,
                            "units": 0,
                            "amount": 0,
                            "charging_head": 9,
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
                    "parameter_value": 52
                },
                "navigation_charge": {
                    "total_charge": 0,
                    "sub_charges": [
                        {
                            "head_code": "navigation_charge",
                            "coa": 1,
                            "per_unit_cost": null,
                            "units": 25091,
                            "amount": 0,
                            "charging_head": 10,
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
                    ]
                },
                "boarding_bridge_charge": {
                    "total_charge": 7942,
                    "sub_charges": [
                        {
                            "head_code": "boarding_bridge_charge",
                            "coa": 1,
                            "per_unit_cost": 100,
                            "units": 2,
                            "amount": 200,
                            "charging_head": 11,
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
                            "head_code": "boarding_bridge_above_2hour_charge",
                            "coa": 1,
                            "per_unit_cost": 60,
                            "units": 68,
                            "amount": 8160,
                            "charging_head": 12,
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
                            "head_code": "discount_charge_frequent_boarding_bridge",
                            "coa": 1,
                            "per_unit_cost": null,
                            "units": null,
                            "amount": 418,
                            "charging_head": 13,
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
                    "parameter_value": 70
                }
            }
        }
    }
}
```

### Aero Invoice Charge Calculation without coa

**Request:** `POST` `{{url}}/api/invoice-charge/`

```json
{
    "invoice_item_type": "aeronautical",
    "flight_origin_type":"international",
    "charges": {
        "embarkation_fees":{
            "parameter_value": 50,
            "sub_charges":{
                "embarkation_fees": true
            }
        },
        "landing":{
            "parameter_value": 52,
            "sub_charges":{
                "off_time_landing_takeoff": true,
                "training_purpose_discount": false,
                "test_flight_discount": false,
                "security_others_international": false,
                "security_others_local": false,
                "parking_charge": true,
                "hanger_charge": false,
                "landing": true
            }
        },
        "navigation_charge":{
            "sub_charges":{
                "navigation_charge": true
            }
        },
        "boarding_bridge_charge":{
            "parameter_value": 70,
            "sub_charges":{
                "boarding_bridge_charge": true,
                "boarding_bridge_above_2hour_charge": true,
                "discount_charge_frequent_boarding_bridge": false
            }
        }
    }
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "'Invoice' Charge Calculation Updated",
    "data": {
        "result": {
            "final_charge": 33572.2875,
            "charges": {
                "embarkation_fees": {
                    "total_charge": 25000,
                    "sub_charges": [
                        {
                            "head_code": "embarkation_fees",
                            "coa": null,
                            "per_unit_cost": 500,
                            "units": 50,
                            "amount": 25000,
                            "charging_head": 1,
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
                    "total_charge": 212.2875,
                    "sub_charges": [
                        {
                            "head_code": "off_time_landing_takeoff",
                            "coa": null,
                            "per_unit_cost": 11.475,
                            "units": null,
                            "amount": 11.475,
                            "charging_head": 3,
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
                            "head_code": "training_purpose_discount",
                            "coa": null,
                            "per_unit_cost": 0,
                            "units": 0,
                            "amount": 0,
                            "charging_head": 4,
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
                            "head_code": "test_flight_discount",
                            "coa": null,
                            "per_unit_cost": 0,
                            "units": 0,
                            "amount": 0,
                            "charging_head": 5,
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
                            "head_code": "security_others_international",
                            "coa": null,
                            "per_unit_cost": 0,
                            "units": 0,
                            "amount": 0,
                            "charging_head": 14,
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
                            "head_code": "security_others_local",
                            "coa": null,
                            "per_unit_cost": 0,
                            "units": 0,
                            "amount": 0,
                            "charging_head": 15,
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
                            "head_code": "parking_charge",
                            "coa": null,
                            "per_unit_cost": 28.6875,
                            "units": 52,
                            "amount": 86.0625,
                            "charging_head": 8,
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
                            "head_code": "hanger_charge",
                            "coa": null,
                            "per_unit_cost": 0,
                            "units": 0,
                            "amount": 0,
                            "charging_head": 9,
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
                        },
                        {
                            "head_code": "landing",
                            "coa": null,
                            "per_unit_cost": 6.75,
                            "units": 16046,
                            "amount": 114.75,
                            "charging_head": 2,
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
                        }
                    ],
                    "parameter_value": 52
                },
                "navigation_charge": {
                    "total_charge": 0,
                    "sub_charges": [
                        {
                            "head_code": "navigation_charge",
                            "coa": null,
                            "per_unit_cost": null,
                            "units": 16046,
                            "amount": 0,
                            "charging_head": 10,
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
                    ]
                },
                "boarding_bridge_charge": {
                    "total_charge": 8360,
                    "sub_charges": [
                        {
                            "head_code": "boarding_bridge_charge",
                            "coa": null,
                            "per_unit_cost": 100,
                            "units": 2,
                            "amount": 200,
                            "charging_head": 11,
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
                            "head_code": "boarding_bridge_above_2hour_charge",
                            "coa": null,
                            "per_unit_cost": 60,
                            "units": 68,
                            "amount": 8160,
                            "charging_head": 12,
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
                            "head_code": "discount_charge_frequent_boarding_bridge",
                            "coa": null,
                            "per_unit_cost": 0,
                            "units": 0,
                            "amount": 0,
                            "charging_head": 13,
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
                    "parameter_value": 70
                }
            }
        }
    }
}
```
