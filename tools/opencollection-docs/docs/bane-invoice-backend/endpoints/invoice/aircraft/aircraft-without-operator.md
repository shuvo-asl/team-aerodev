# aircraft without operator

**GET** `{{url}}/api/bas/aircraft-without-operator/?page=1&limit=10`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `page` | `1` | query |
| `limit` | `10` | query |

## Body

Type: `text`

```
{
    "icao": 745794,
    "registration_number": "yueuh",
    "operator_id": 1,
    "aircraft_type_id": 1
}
```
