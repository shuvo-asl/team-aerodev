# Update Flight

**PATCH** `{{url}}/api/flight/113/`

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

    "flight_no": "FL912368",
    "aircraft_registration_no": "vbvb",
    "flight_origin_type": "international",
    "flight_type": "landing",
    "src": "HAAB",
    "dest": "HJJJ",
    "mtow": 5000,
    "mtow_unit": "kg",
    "flight_source_data": "{}",
    "flight_reference_number": "mukta",
    "flight_source": "adsb",
    "fir_in": "2024-12-02T15:00:00+06:00",
    "fir_out": "2024-12-02T15:00:00+06:00",
    "fir_in_route": "some",
    "fir_out_route": "nothing",
    "flight_purpose": "cargo_flight",
    "date_of_operation": "2024-12-05",
    "operator": 40,
    "aircraft_type":"B777",
    "flight_charges": {
    },
    "covered_distance_nm":130,
    "custom_charges": []
}
```

## Examples

### Update Flight Success

**Request:** `PATCH` `{{url}}/api/flight/1/`

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

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Flight successfully updated",
    "data": {
        "result": {
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
    }
}
```

### Update Flight (Duplicate Flight No)

**Request:** `PATCH` `{{url}}/api/flight/1/`

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

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Flight Failed To Update",
    "error": null,
    "errors": {
        "flight_no": "flight with this flight no already exists."
    }
}
```
