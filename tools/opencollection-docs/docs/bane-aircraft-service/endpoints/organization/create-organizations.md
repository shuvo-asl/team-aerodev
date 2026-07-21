# create organizations

**POST** `{{url}}/organizations`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `all` | `true` | query |

## Body

Type: `json`

```json
{
    "name": "# 1. Aviation Support Limited (ASL) ",
    "address_line_1": "House - 1 & 3, Level - 3, Road - 21\/C",
    "address_line_2": "Nikunja -2,  Khilkhet, Dhaka",
    "city_id": "1827",
    "logo": "0",
    "base_currency_id": "1",
    "alternate_aircraft_registrations": "",
    "email": "info@asl.aero",
    "iata": "",
    "icao": "2842.0",
    "business_phone": "+88028815575",
    "business_phone_extension": "",
    "fax_number": "",
    "website": "https://www.asl.aero",
    "postal_code": "12292",
    "type": "OSP Agent",
    "ospl_no": "1.0",
    "comment": "",
    "is_blacklisted": false,
    "is_deleted": false
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/organizations`

```json
{
    "name": "# 1. Aviation Support Limited (ASL) ",
    "address_line_1": "House - 1 & 3, Level - 3, Road - 21\/C",
    "address_line_2": "Nikunja -2,  Khilkhet, Dhaka",
    "city_id": "1827",
    "logo": "0",
    "base_currency_id": "1",
    "alternate_aircraft_registrations": "",
    "email": "info@asl.aero",
    "iata": "",
    "icao": "2842.0",
    "business_phone": "+88028815575",
    "business_phone_extension": "",
    "fax_number": "",
    "website": "https://www.asl.aero",
    "postal_code": "12292",
    "type": "OSP Agent",
    "ospl_no": "1.0",
    "comment": "",
    "is_blacklisted": false,
    "is_deleted": false
}
```

**Response:** `201 CREATED`

```json
{
    "data": {
        "address_line_1": "House - 1 & 3, Level - 3, Road - 21/C",
        "address_line_2": "Nikunja -2,  Khilkhet, Dhaka",
        "air_crafts": [],
        "alternate_aircraft_registrations": "",
        "base_currency_id": 1,
        "business_phone": "+88028815575",
        "business_phone_extension": "",
        "city_id": 1827,
        "comment": "",
        "created_by": {
            "user_name": "admin"
        },
        "created_by_id": 1,
        "email": "info@asl.aero",
        "fax_number": "",
        "iata": "",
        "icao": "2842.0",
        "id": 1306,
        "is_blacklisted": false,
        "is_deleted": false,
        "logo": 0,
        "name": "# 1. Aviation Support Limited (ASL) ",
        "ospl_no": "1.0",
        "postal_code": "12292",
        "type": "OSP Agent",
        "updated_by": {
            "user_name": "admin"
        },
        "updated_by_id": 1,
        "website": "https://www.asl.aero"
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```
