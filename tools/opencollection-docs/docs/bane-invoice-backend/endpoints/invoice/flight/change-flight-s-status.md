# Change Flight's Status

**POST** `{{url}}/api/flight/change-status/`

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
    "flight_ids": [1],
    "new_status": "billed"
}
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
