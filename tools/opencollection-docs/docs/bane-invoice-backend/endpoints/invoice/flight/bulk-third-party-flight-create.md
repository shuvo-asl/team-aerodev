# Bulk Third Party Flight Create

**POST** `{{url}}/api/third-party-flight-dump/`

## Auth

Type: `bearer`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
[
  {
    "flight_sector_id": 3706,
    "icao24": "A35AFF",
    "flight_start": "2025-08-03T10:39:52+06:00",
    "flight_end": "2025-08-03T10:50:13+06:00",
    "mvt_type": "AIR",
    "callsign": "SIA325",
    "mode_a": "7662",
    "mode_a_category": "INTERNATIONAL",
    "origin": "EDDF",
    "destination": "WSSS",
    "route_source": "SENSOR",
    "fir_entry_time": "2025-08-03T10:42:04+06:00",
    "fir_entry_source": "ESTIMATED",
    "fir_exit_time": "2025-08-03T10:42:04+06:00",
    "fir_exit_source": "ESTIMATED",
    "flight_state": "LIVE"
  },
  {
    "flight_sector_id": 3743,
    "icao24": "06A108",
    "flight_start": "2025-08-03T10:45:58+06:00",
    "flight_end": "2025-08-03T10:50:14+06:00",
    "mvt_type": "AIR",
    "callsign": "QTR890",
    "mode_a": "3206",
    "mode_a_category": "INTERNATIONAL",
    "origin": "OTHH",
    "destination": "ZSHC",
    "route_source": "SENSOR",
    "fir_entry_time": "2025-08-03T10:47:23+06:00",
    "fir_entry_source": "SENSOR",
    "flight_state": "LIVE"
  }
]
```

## Examples

### Create Flight (Access denied)

**Request:** `POST` `{{url}}/api/flight/`

```json
{
  "call_sign": "ABC123",
  "flight_no": "FL12345",
  "flight_type": "landing",
  "aircraft_registration_no": "N12345",
  "flight_origin_type": "local",
  "src": "JFK",
  "dest": "LAX",
  "mtow": "50000.00",
  "mtow_unit": "kg",
  "flight_source_data": {
    "source": "ADSB",
    "details": {
      "icao24": "abcd12"
    }
  },
  "flight_reference_number": "REF123456",
  "flight_source": "adsb",
  "status": "incomplete",
  "fir_in": "2024-09-16T08:00:00Z",
  "fir_out": "2024-09-16T09:00:00Z",
  "fir_in_route": "Route A",
  "fir_out_route": "Route B",
  "flight_purpose": "cargo_flight",
  "date_of_operation": "2024-09-16",
  "operator": 1
}
```

**Response:** `403 Forbidden`

```json
{
    "status": "failed",
    "message": "Access Denied",
    "error": "You do not have permission to perform this action.",
    "errors": []
}
```

### Create Flight(Flight no duplicate)

**Request:** `POST` `{{url}}/api/flight/`

```json
{
  "call_sign": "ABC123",
  "flight_no": "FL12345",
  "flight_type": "landing",
  "aircraft_registration_no": "N12345",
  "flight_origin_type": "local",
  "src": "JFK",
  "dest": "LAX",
  "mtow": "50000.00",
  "mtow_unit": "kg",
  "flight_source_data": {
    "source": "ADSB",
    "details": {
      "icao24": "abcd12"
    }
  },
  "flight_reference_number": "REF123456",
  "flight_source": "adsb",
  "status": "incomplete",
  "fir_in": "2024-09-16T08:00:00Z",
  "fir_out": "2024-09-16T09:00:00Z",
  "fir_in_route": "Route A",
  "fir_out_route": "Route B",
  "flight_purpose": "cargo_flight",
  "date_of_operation": "2024-09-16",
  "operator": 1
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Flight Failed To Create",
    "error": null,
    "errors": {
        "flight_no": "flight with this flight no already exists."
    }
}
```

### Create Flight Success

**Request:** `POST` `{{url}}/api/flight/`

```json
{
  "call_sign": "ABC123",
  "flight_no": "FL123456",
  "flight_type": "landing",
  "aircraft_registration_no": "N12345",
  "flight_origin_type": "local",
  "src": "JFK",
  "dest": "LAX",
  "mtow": "50000.00",
  "mtow_unit": "kg",
  "flight_source_data": {
    "source": "ADSB",
    "details": {
      "icao24": "abcd12"
    }
  },
  "flight_reference_number": "REF123456",
  "flight_source": "adsb",
  "status": "incomplete",
  "fir_in": "2024-09-16T08:00:00Z",
  "fir_out": "2024-09-16T09:00:00Z",
  "fir_in_route": "Route A",
  "fir_out_route": "Route B",
  "flight_purpose": "cargo_flight",
  "date_of_operation": "2024-09-16",
  "operator": 1
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Flight successfully created",
    "data": {
        "result": {
            "id": 2,
            "deleted_at": null,
            "created_at": "2024-12-02T16:07:03.536083+06:00",
            "updated_at": null,
            "call_sign": "ABC123",
            "flight_no": "FL123456",
            "flight_type": "landing",
            "aircraft_registration_no": "N12345",
            "flight_origin_type": "local",
            "src": "JFK",
            "dest": "LAX",
            "mtow": 50000,
            "mtow_unit": "kg",
            "flight_source_data": {
                "source": "ADSB",
                "details": {
                    "icao24": "abcd12"
                }
            },
            "flight_reference_number": "REF123456",
            "flight_source": "adsb",
            "status": "ready_to_bill",
            "fir_in": "2024-09-16T14:00:00+06:00",
            "fir_out": "2024-09-16T15:00:00+06:00",
            "fir_in_route": "Route A",
            "fir_out_route": "Route B",
            "flight_purpose": "cargo_flight",
            "date_of_operation": "2024-09-16",
            "company": null,
            "operator": 1
        }
    }
}
```

### Create Flight

**Request:** `POST` `{{url}}/api/flight/`

```json
{
  "call_sign": "ABC123",
  "flight_no": "FL1012",
  "flight_type": "landing",
  "aircraft_registration_no": "N12345",
  "flight_origin_type": "local",
  "src": "JFK",
  "dest": "LAX",
  "mtow": "4999.00",
  "mtow_unit": "kg",
  "flight_source_data": {
    "source": "other",
    "details": {
      "icao24": "abcd12"
    }
  },
  "flight_reference_number": "REF123456",
  "flight_source": "other",
  "status": "incomplete",
  "fir_in": "2024-12-02T08:00:00Z",
  "fir_out": "2024-12-02T09:00:00Z",
  "fir_in_route": "Route A",
  "fir_out_route": "Route B",
  "flight_purpose": "cargo_flight",
  "date_of_operation": "2024-12-02",
  "operator": 109,
  "flight_charges":{
        "embarkation_fees":{
            "parameter_value": 50,
            "sub_charges":[
                {"head_code":"embarkation_fees", "head_code_status": true, "coa": 1}
            ]
        },
        "landing":{
            "parameter_value": 52,
            "sub_charges":[
                {"head_code":"landing", "head_code_status": true, "coa": 1, "description": "abcd"},
                {"head_code":"off_time_landing_takeoff", "head_code_status": true, "coa": 1, "description": "abcd"},
                {"head_code":"training_purpose_discount", "head_code_status": false, "coa": 1},
                {"head_code":"test_flight_discount", "head_code_status": false, "coa": 1},
                {"head_code":"security_others_international", "head_code_status": false , "coa": 1},
                {"head_code":"security_others_local", "head_code_status": false , "coa": 1},
                {"head_code":"parking_charge", "head_code_status": true , "coa": 1},
                {"head_code":"hanger_charge", "head_code_status": false , "coa": 1}
            ]
        },
        "navigation_charge":{
            "sub_charges":[
                {"head_code":"navigation_charge", "head_code_status": true, "coa": 1}
            ]
        },
        "boarding_bridge_charge":{
            "parameter_value": 70,
            "sub_charges":[
                {"head_code":"boarding_bridge_charge", "head_code_status": true , "coa": 1},
                {"head_code":"boarding_bridge_above_2hour_charge", "head_code_status": true , "coa": 1},
                {"head_code":"discount_charge_frequent_boarding_bridge", "head_code_status": true , "coa": 1}
            ]
        }
    },
  "custom_charges":[
    {"head_code": "Fine", "unit": 1, "unit_price": 25.0, "amount": 25.0}
  ]
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Flight successfully created",
    "data": {
        "result": {
            "id": 28,
            "call_sign": "ABC123",
            "flight_no": "FL1012",
            "flight_type": "landing",
            "aircraft_registration_no": "N12345",
            "flight_origin_type": "local",
            "mtow": 4999,
            "mtow_unit": "kg",
            "src": "JFK",
            "dest": "LAX",
            "flight_source_data": {
                "source": "other",
                "details": {
                    "icao24": "abcd12"
                }
            },
            "flight_reference_number": "REF123456",
            "flight_source": "other",
            "status": "ready_to_bill",
            "fir_in": "2024-12-02T14:00:00+06:00",
            "fir_out": "2024-12-02T15:00:00+06:00",
            "fir_in_route": "Route A",
            "fir_out_route": "Route B",
            "flight_purpose": "cargo_flight",
            "date_of_operation": "2024-12-02",
            "operator": 109,
            "operator_name": "ATUL",
            "charges_amount": 2515.25
        }
    }
}
```

### Create Flight (Minimul Data)

**Request:** `POST` `{{url}}/api/flight/`

```json
{
  "mtow": 5000,
  "flight_type": "landing",
  "flight_origin_type": "domestic",
  "icao": "usb201",
  "flight_source": "manual",
  "tracking_start": "2025-07-20T12:00:00Z"

}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Flight successfully created",
    "data": {
        "result": {
            "id": 40,
            "icao": "usb201",
            "flight_source": "manual",
            "tracking_start": "2025-07-20T18:00:00+06:00",
            "tracking_end": null,
            "company": 1,
            "source_reference_id": null,
            "call_sign": null,
            "flight_no": null,
            "flight_type": "landing",
            "aircraft_registration_no": null,
            "flight_origin_type": "domestic",
            "mtow": 5000,
            "mtow_unit": "kg",
            "src": null,
            "dest": null,
            "flight_source_data": null,
            "status": "incomplete",
            "fir_in": null,
            "fir_out": null,
            "fir_in_route": null,
            "fir_out_route": null,
            "flight_purpose": null,
            "date_of_operation": null,
            "operator": null,
            "charges_amount": 26.25,
            "notes": null,
            "log": [
                {
                    "id": 49510,
                    "type": "create",
                    "model": "Flight",
                    "object": 40,
                    "user_name": "admin",
                    "email": "admin@gmail.com",
                    "impersonated_by": null,
                    "ip": "192.168.65.1",
                    "changes": null,
                    "agent_info": "PostmanRuntime/7.44.1",
                    "status": "success",
                    "created_at": "2025-07-21T15:59:17.692446+06:00"
                }
            ],
            "invoice_id": null,
            "invoice_no": null,
            "payment_status": null,
            "flight_charges_amount": 26.25,
            "flight_charges": {
                "landing": {
                    "total_charge": 26.25,
                    "parameter_value": 0,
                    "sub_charges": [
                        {
                            "id": 73,
                            "flight": 40,
                            "charge_head": 2,
                            "head_code": "landing",
                            "unit": 5000,
                            "unit_price": 5.25,
                            "amount": 26.25,
                            "description": null,
                            "coa": null,
                            "head": {
                                "id": 2,
                                "deleted_at": null,
                                "created_at": "2024-10-09T17:30:45.960369+06:00",
                                "updated_at": null,
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
                    ]
                }
            },
            "custom_charges": []
        }
    }
}
```
