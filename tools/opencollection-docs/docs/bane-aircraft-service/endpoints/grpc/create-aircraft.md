# create aircraft

**gRPC** (unary) `/bas.BAS/CreateAircraft`

Endpoint: `{{gRPC_url}}`

Proto file: `../../../rpc/bas.proto`

## Auth

Type: `inherit`

## Metadata

| Name | Value |
|---|---|
| `{{auth_param_name}}` | `{{token}}` |

## Message

```json
{
    "icao24": "6560",
    "registration_number": "reg9",
    "aircraft_type_id": 3,
    "operator_id": 4
}
```
