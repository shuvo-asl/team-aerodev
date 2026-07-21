# get or create aircraft

**POST** `{{url}}/api/get-or-create-aircraft/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
"registration_number": "TESTTEST9",
            "aircraft_type": {
                "name": "KJI1",
                "mtow": 8,
                "mtow_unit": "ton",
                "wing_type": "Fixed Wing",
                "is_registration_fulfilled": false
            },
            "operator": {
                "short_code": "A7CF90",
                "name": "",
                "address_line_1": "",
                "address_line_2": "",
                "email": "rakib2@aerogon.aero",
                "iata": "",
                "icao": "",
                "business_phone": "",
                "business_phone_extension": "",
                "fax_number": "",
                "website": "",
                "postal_code": "",
                "ospl_no": "",
                "comment": "",
                "is_blacklisted": false,
                "alternate_aircraft_registrations": ""
            },
            "purpose_type": "Civil"

}
```

## Examples

### get or create aircraft

**Request:** `POST` `{{url}}/api/get-or-create-aircraft/`

```json
{
    "registration_number": "TESTTEST5",
    "operator": {
        "short_code": "A7CFD"
    },
    "aircraft_type": {
        "name": "KJI"
    }
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Aircraft created successfully",
    "data": {
        "result": {
            "id": 4751,
            "registration_number": "TESTTEST5",
            "aircraft_type": {
                "name": "KJI",
                "mtow": 0,
                "mtow_unit": "",
                "wing_type": "",
                "is_registration_fulfilled": false
            },
            "operator": {
                "short_code": "A7CFD",
                "name": "",
                "address_line_1": "",
                "address_line_2": "",
                "email": "",
                "iata": "",
                "icao": "",
                "business_phone": "",
                "business_phone_extension": "",
                "fax_number": "",
                "website": "",
                "postal_code": "",
                "ospl_no": "",
                "comment": "",
                "is_blacklisted": false,
                "alternate_aircraft_registrations": ""
            },
            "purpose_type": ""
        }
    }
}
```
