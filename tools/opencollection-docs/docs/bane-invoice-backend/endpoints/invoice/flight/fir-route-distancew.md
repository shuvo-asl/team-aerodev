# FIR route distancew

**GET** `{{url}}/api/flight/?limit=5&status=ready_to_bill`

## Auth

Type: `inherit`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `5` | query |
| `search` | `FL0212` | query |
| `flight_type` | `landing` | query |
| `flight_origin_type` | `international` | query |
| `mtow` | `5000` | query |
| `flight_source` | `adsb` | query |
| `operator` | `109` | query |
| `call_sign` | `ABC123` | query |
| `fir_in_route` | `Route A` | query |
| `fir_out_route` | `Route B` | query |
| `fir_in` | `2024-12-02, 2024-12-03` | query |
| `fir_out` | `2024-12-03, 2024-12-03` | query |
| `date_of_operation` | `2024-09-16` | query |
| `status` | `ready_to_bill` | query |
| `status` | `billing` | query |

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Examples

### Get All Flights

**Request:** `GET` `{{url}}/api/flight/?limit=5`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Flight Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 2,
        "total_page": 1,
        "result": [
            {
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
            },
            {
                "id": 1,
                "deleted_at": null,
                "created_at": "2024-12-02T16:05:04.535296+06:00",
                "updated_at": null,
                "call_sign": "ABC123",
                "flight_no": "FL12345",
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
        ]
    }
}
```

### Get All Flights (status wise)

**Request:** `GET` `{{url}}/api/flight/?limit=5&status=ready_to_bill`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Flight Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 4,
        "total_page": 1,
        "result": [
            {
                "id": 4,
                "deleted_at": null,
                "created_at": "2024-12-03T10:39:13.536148+06:00",
                "updated_at": null,
                "call_sign": "ABC123",
                "flight_no": "FL0212",
                "flight_type": "landing",
                "aircraft_registration_no": "N12345",
                "flight_origin_type": "local",
                "src": "JFK",
                "dest": "LAX",
                "mtow": 50000,
                "mtow_unit": "kg",
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
                "company": null,
                "operator": 1
            },
            {
                "id": 3,
                "deleted_at": null,
                "created_at": "2024-12-03T10:39:01.873059+06:00",
                "updated_at": null,
                "call_sign": "ABC123",
                "flight_no": "FL0312",
                "flight_type": "landing",
                "aircraft_registration_no": "N12345",
                "flight_origin_type": "local",
                "src": "JFK",
                "dest": "LAX",
                "mtow": 50000,
                "mtow_unit": "kg",
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
                "company": null,
                "operator": 1
            },
            {
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
            },
            {
                "id": 1,
                "deleted_at": null,
                "created_at": "2024-12-02T16:05:04.535296+06:00",
                "updated_at": "2024-12-02T16:08:17.332803+06:00",
                "call_sign": "ABC123",
                "flight_no": "FL12345",
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
        ]
    }
}
```

### Get All Flights (search)

**Request:** `GET` `{{url}}/api/flight/?limit=5&search=FL0212`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Flight Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 1,
        "total_page": 1,
        "result": [
            {
                "id": 4,
                "deleted_at": null,
                "created_at": "2024-12-03T10:39:13.536148+06:00",
                "updated_at": null,
                "call_sign": "ABC123",
                "flight_no": "FL0212",
                "flight_type": "landing",
                "aircraft_registration_no": "N12345",
                "flight_origin_type": "local",
                "src": "JFK",
                "dest": "LAX",
                "mtow": 50000,
                "mtow_unit": "kg",
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
                "company": null,
                "operator": 1
            }
        ]
    }
}
```

### get ready to bill flights of a client

**Request:** `GET` `{{url}}/api/flight/?operator=1&status=ready_to_bill`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Flight Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 1,
        "total_page": 1,
        "result": [
            {
                "id": 1,
                "call_sign": "ABC123",
                "flight_no": "FL12345",
                "flight_type": "landing",
                "aircraft_registration_no": "N12345",
                "flight_origin_type": "local",
                "mtow": 50000,
                "mtow_unit": "kg",
                "src": "JFK",
                "dest": "LAX",
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
                "operator": 1,
                "operator_name": "Operator",
                "charges_amount": 0
            }
        ]
    }
}
```

### Get All Flights, multiple status

**Request:** `GET` `{{url}}/api/flight/?limit=5&status=ready_to_bill&status=billing`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Flight Successfully Fetched",
    "data": {
        "next": 2,
        "previous": null,
        "current_page": 1,
        "total_object": 11,
        "total_page": 3,
        "result": [
            {
                "id": 23,
                "call_sign": "ABC123",
                "flight_no": "FLI07",
                "flight_type": "landing",
                "aircraft_registration_no": "N12345",
                "flight_origin_type": "local",
                "mtow": 5000,
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
                "status": "billing",
                "fir_in": "2024-12-02T14:00:00+06:00",
                "fir_out": "2024-12-02T15:00:00+06:00",
                "fir_in_route": "Route A",
                "fir_out_route": "Route B",
                "flight_purpose": "cargo_flight",
                "date_of_operation": "2024-12-02",
                "operator": 107,
                "operator_name": "Ismail Hasan Sarker",
                "charges_amount": 2515.25
            },
            {
                "id": 22,
                "call_sign": "ABC123",
                "flight_no": "FLI06",
                "flight_type": "landing",
                "aircraft_registration_no": "N12345",
                "flight_origin_type": "local",
                "mtow": 5000,
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
                "operator": 107,
                "operator_name": "Ismail Hasan Sarker",
                "charges_amount": 2515.25
            },
            {
                "id": 21,
                "call_sign": "ABC123",
                "flight_no": "FLI05",
                "flight_type": "landing",
                "aircraft_registration_no": "N12345",
                "flight_origin_type": "local",
                "mtow": 5000,
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
                "status": "billing",
                "fir_in": "2024-12-02T14:00:00+06:00",
                "fir_out": "2024-12-02T15:00:00+06:00",
                "fir_in_route": "Route A",
                "fir_out_route": "Route B",
                "flight_purpose": "cargo_flight",
                "date_of_operation": "2024-12-02",
                "operator": 107,
                "operator_name": "Ismail Hasan Sarker",
                "charges_amount": 2316.5
            },
            {
                "id": 20,
                "call_sign": "ABC123",
                "flight_no": "FLI04",
                "flight_type": "landing",
                "aircraft_registration_no": "N12345",
                "flight_origin_type": "local",
                "mtow": 5000,
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
                "operator": 107,
                "operator_name": "Ismail Hasan Sarker",
                "charges_amount": 2581.25
            },
            {
                "id": 19,
                "call_sign": "ABC123",
                "flight_no": "FLI03",
                "flight_type": "landing",
                "aircraft_registration_no": "N12345",
                "flight_origin_type": "local",
                "mtow": 5000,
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
                "operator": 107,
                "operator_name": "Ismail Hasan Sarker",
                "charges_amount": 2515.25
            }
        ]
    }
}
```
