# get or create aircraft

**POST** `{{url}}/aircraft/get-or-create`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
        "icao24": "TEST07",
        "purpose_type": "Military",
        "registration_number": "TESTREG08",
        "operator": {
            "short_code": "ETH"
        },
        "aircraft_type":{
            "name": "SU-35 terminator",
            "mtow": 102,
            "mtow_unit": "ton"
        }
}
```

## Examples

### get or create aircraft if aircraft already exists

**Request:** `POST` `{{url}}/aircraft/get-or-create`

```json
{
        "icao24": "TEST01",
        "purpose_type": "Military",
        "registration_number": "TESTREG01",
        "operator": {
            "short_code": "ETH"
        },
        "aircraft_type":{
            "name": "F-15 Eagle",
            "mtow": 100,
            "mtow_unit": "ton"
        }
}
```

**Response:** `200 OK`

```json
{
    "data": {
        "aircraft_type": {
            "is_registration_fulfilled": false,
            "mtow": 100,
            "mtow_unit": "ton",
            "name": "F-15 Eagle",
            "wing_type": null
        },
        "icao24": "TEST01",
        "operator": {
            "address_line_1": "ADDRESS: \n     Ethiopian Airlines, \n     Airport Enterprise Building, Ground Floor, \n     Addis Ababa, Ethiopia \nTELEPHONE :  +251 11 517 4422\nFAX : +251-11- 661 1474 \nEMAIL : CustomerRelations@ethiopianairlines.com",
            "address_line_2": null,
            "alternate_aircraft_registrations": null,
            "business_phone": "+211927773498",
            "business_phone_extension": null,
            "comment": "",
            "email": "sabbir@asl.aero",
            "fax_number": null,
            "iata": null,
            "icao": null,
            "is_blacklisted": false,
            "name": "Ethiopian Airlines",
            "ospl_no": null,
            "postal_code": null,
            "short_code": "ETH",
            "type": "Operator",
            "website": null
        },
        "purpose_type": "Military",
        "registration_number": "TESTREG01"
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```

### get or create aircraft new aircraft

**Request:** `POST` `{{url}}/aircraft/get-or-create`

```json
{
        "icao24": "TEST02",
        "purpose_type": "Military",
        "registration_number": "TESTREG02",
        "operator": {
            "short_code": "ETH"
        },
        "aircraft_type":{
            "name": "F-16 Eagle",
            "mtow": 110,
            "mtow_unit": "ton"
        }
}
```

**Response:** `201 CREATED`

```json
{
    "data": {
        "aircraft_type": {
            "is_registration_fulfilled": false,
            "mtow": 110,
            "mtow_unit": "ton",
            "name": "F-16 Eagle",
            "wing_type": null
        },
        "icao24": "TEST02",
        "operator": {
            "address_line_1": "ADDRESS: \n     Ethiopian Airlines, \n     Airport Enterprise Building, Ground Floor, \n     Addis Ababa, Ethiopia \nTELEPHONE :  +251 11 517 4422\nFAX : +251-11- 661 1474 \nEMAIL : CustomerRelations@ethiopianairlines.com",
            "address_line_2": null,
            "alternate_aircraft_registrations": null,
            "business_phone": "+211927773498",
            "business_phone_extension": null,
            "comment": "",
            "email": "sabbir@asl.aero",
            "fax_number": null,
            "iata": null,
            "icao": null,
            "is_blacklisted": false,
            "name": "Ethiopian Airlines",
            "ospl_no": null,
            "postal_code": null,
            "short_code": "ETH",
            "type": "Operator",
            "website": null
        },
        "purpose_type": "Military",
        "registration_number": "TESTREG02"
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```
