# create aircraft type

**gRPC** (unary) `/bas.BAS/CreateAircraftType`

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
    "name": "B-7389",
    "mtow": 100,
    "mtow_unit": "ton"
}
```
