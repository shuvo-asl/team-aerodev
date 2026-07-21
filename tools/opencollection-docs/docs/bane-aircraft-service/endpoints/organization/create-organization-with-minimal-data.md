# create organization with minimal data

**POST** `{{url}}/organization/quick-create`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "short_code": "AWA",
    "email": "eservation@airastra.com",
    "name": "Air Astra"
}
```

## Examples

### email field is required otherwise 400

**Request:** `POST` `{{url}}/organization/quick-create`

```json
{
    "name": "test op"
}
```

**Response:** `400 BAD REQUEST`

```json
{
    "error": null,
    "errors": {
        "email": "Missing data for required field."
    },
    "message": "Validation Error"
}
```

### create organization with email only

**Request:** `POST` `{{url}}/organization/quick-create`

```json
{
    "email": "email1@gmail.com"
}
```

**Response:** `201 CREATED`

```json
{
    "data": {
        "address_line_1": null,
        "address_line_2": null,
        "air_crafts": [],
        "alternate_aircraft_registrations": null,
        "base_currency_id": null,
        "business_phone": null,
        "business_phone_extension": null,
        "city_id": null,
        "comment": "",
        "created_by": {
            "user_name": "admin"
        },
        "created_by_id": 1,
        "email": "email1@gmail.com",
        "fax_number": null,
        "iata": null,
        "icao": null,
        "id": 14716,
        "is_blacklisted": false,
        "is_deleted": false,
        "logo": null,
        "name": null,
        "ospl_no": null,
        "postal_code": null,
        "short_code": null,
        "type": "Operator",
        "updated_by": {
            "user_name": "admin"
        },
        "updated_by_id": 1,
        "website": null
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```

### create organization with minimal data

**Request:** `POST` `{{url}}/organization/quick-create`

```json
{
        "address_line_1": "address_line_1",
        "address_line_2": "address_line_2",
        "alternate_aircraft_registrations": "uegyfigf",
        "business_phone": "+8801558250668",
        "business_phone_extension": "+8801",
        "comment": "sample ",
        "email": "email3@gmail.com",
        "fax_number": "09388884",
        "iata": "ion",
        "icao": "ipejfr",
        "name": "op name",
        "ospl_no": "9833",
        "postal_code": "9993",
        "short_code": "jko",
        "website": "https://twitter.com"
    }
```

**Response:** `201 CREATED`

```json
{
    "data": {
        "address_line_1": "address_line_1",
        "address_line_2": "address_line_2",
        "air_crafts": [],
        "alternate_aircraft_registrations": "uegyfigf",
        "base_currency_id": null,
        "business_phone": "+8801558250668",
        "business_phone_extension": "+8801",
        "city_id": null,
        "comment": "sample ",
        "created_by": {
            "user_name": "admin"
        },
        "created_by_id": 1,
        "email": "email3@gmail.com",
        "fax_number": "09388884",
        "iata": "ion",
        "icao": "ipejfr",
        "id": 14717,
        "is_blacklisted": false,
        "is_deleted": false,
        "logo": null,
        "name": "op name",
        "ospl_no": "9833",
        "postal_code": "9993",
        "short_code": "jko",
        "type": "Operator",
        "updated_by": {
            "user_name": "admin"
        },
        "updated_by_id": 1,
        "website": "https://twitter.com"
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```

### short code must be unique

**Request:** `POST` `{{url}}/organization/quick-create`

```json
{
    "short_code": "SAA",
    "email": "email10@gmail.com"
}
```

**Response:** `400 BAD REQUEST`

```json
{
    "error": null,
    "errors": {
        "short_code": "Operator with given short code already exists"
    },
    "message": "Validation Error"
}
```

### email must be unique

**Request:** `POST` `{{url}}/organization/quick-create`

```json
{
    "short_code": "SAA1",
    "email": "email@gmail.com"
}
```

**Response:** `400 BAD REQUEST`

```json
{
    "error": null,
    "errors": {
        "email": "Email must be unique"
    },
    "message": "Validation Error"
}
```

### type must be valid if provided

**Request:** `POST` `{{url}}/organization/quick-create`

```json
{
        "address_line_1": "address_line_1",
        "address_line_2": "address_line_2",
        "alternate_aircraft_registrations": "uegyfigf",
        "business_phone": "+8801558250668",
        "business_phone_extension": "+8801",
        "comment": "sample ",
        "email": "email9@gmail.com",
        "fax_number": "09388884",
        "iata": "ion",
        "icao": "ipejfr",
        "name": "op name",
        "ospl_no": "9833",
        "postal_code": "9993",
        "short_code": "jko1",
        "website": "https://twitter.com",
        "type": "Operator5"
    }
```

**Response:** `400 BAD REQUEST`

```json
{
    "error": null,
    "errors": {
        "type": "Must be one of: Operator, Principle, OSP Agent, Agent, Security Agency, Aviation Authority, Miscellaneous."
    },
    "message": "Validation Error"
}
```
