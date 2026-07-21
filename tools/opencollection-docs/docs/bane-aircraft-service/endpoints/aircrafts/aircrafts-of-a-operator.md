# aircrafts of a operator

**GET** `{{url}}/aircraft/operator?all=true&short_code=ETH`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `operator_id` | `14709` | query |
| `all` | `true` | query |
| `short_code` | `ETH` | query |

## Examples

### aircrafts of a operator

**Request:** `GET` `{{url}}/aircraft/operator?all=true&short_code=USF1`

**Response:** `200 OK`

```json
{
    "count": 1,
    "data": [
        {
            "aircraft_type": "B2 Spirit",
            "mtow": null,
            "mtow_unit": "kg",
            "operator_shortcode": "USF1",
            "purpose_type": null,
            "registration_number": "B7CFD591",
            "wing_type": "Fixed Wing"
        }
    ],
    "error": null,
    "errors": null,
    "message": "successful",
    "operator_shortcode": "USF1"
}
```

### aircrafts of a operator no aircraft found

**Request:** `GET` `{{url}}/aircraft/operator?all=true&short_code=USF12`

**Response:** `200 OK`

```json
{
    "count": 0,
    "data": [],
    "error": null,
    "errors": null,
    "message": "successful",
    "operator_shortcode": "USF12"
}
```
