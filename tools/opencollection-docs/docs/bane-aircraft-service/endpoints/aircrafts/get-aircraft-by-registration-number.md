# get aircraft by registration number

**GET** `{{url}}/aircraft/registration-number/A7CFD`

## Auth

Type: `bearer`

## Examples

### get aircraft by registration number

**Request:** `GET` `{{url}}/aircraft/registration-number/B7CFD591`

**Response:** `200 OK`

```json
{
    "data": {
        "aircraft_type": "B2 Spirit",
        "mtow": null,
        "mtow_unit": "kg",
        "operator_shortcode": "USF1",
        "purpose_type": null,
        "registration_number": "B7CFD591",
        "wing_type": "Fixed Wing"
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```

### get aircraft by registration number aircraft not found

**Request:** `GET` `{{url}}/aircraft/registration-number/A7CFD2`

**Response:** `404 NOT FOUND`

```json
{
    "error": "Aircraft with given registration number not found",
    "errors": null,
    "message": "Not Found"
}
```
