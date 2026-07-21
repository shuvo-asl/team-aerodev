# operator dump

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
    "name": "ASL System Operator",
    "email": "asl901@gmail.com",
    "phone": "+08801558250667",
    "billing_address": "Dhaka, Bangladesh",
    "short_code": "ASL5"
}
```

## Examples

### email must be unique

**Request:** `POST` `{{url}}/organizations`

```json
{
    "name": "ASL System Operator",
    "email": "asl3@gmail.com",
    "phone": "+08801558250667",
    "billing_address": "Dhaka, Bangladesh",
    "short_code": "ASL2"
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

### short must be unique

**Request:** `POST` `{{url}}/organizations`

```json
{
    "name": "ASL System Operator",
    "email": "asl901@gmail.com",
    "phone": "+08801558250667",
    "billing_address": "Dhaka, Bangladesh",
    "short_code": "ASL"
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

### sucess

**Request:** `POST` `{{url}}/organizations`

```json
{
    "name": "ASL System Operator",
    "email": "asl901@gmail.com",
    "phone": "+08801558250667",
    "billing_address": "Dhaka, Bangladesh",
    "short_code": "ASL5"
}
```

**Response:** `201 CREATED`

```json
{
    "data": {
        "address_line_2": null,
        "alternate_aircraft_registrations": null,
        "base_currency_id": null,
        "billing_address": "Dhaka, Bangladesh",
        "business_phone_extension": null,
        "city_id": null,
        "comment": "",
        "email": "asl901@gmail.com",
        "fax_number": null,
        "iata": null,
        "icao": null,
        "is_blacklisted": false,
        "is_deleted": false,
        "logo": null,
        "name": "ASL System Operator",
        "ospl_no": null,
        "phone": "+08801558250667",
        "postal_code": null,
        "short_code": "ASL5",
        "type": "Operator",
        "website": null
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```
