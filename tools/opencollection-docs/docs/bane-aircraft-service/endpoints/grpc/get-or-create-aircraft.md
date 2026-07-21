# get or create aircraft

**gRPC** (unary) `/bas.BAS/GetOrCreateAircraft`

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
        "icao24": "TEST03",
        "purpose_type": "Military",
        "registration_number": "TESTREG012",
        "operator": {
            "short_code": "ETH"
        },
        "aircraft_type":{
            "name": "A-10 warthog",
            "mtow": 100,
            "mtow_unit": "ton"
        }
}
```
