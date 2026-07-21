# get aicraft by icao

**gRPC** (unary) `/bas.BAS/GetAircraftBYICAO24`

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
    "icao24": "04012B"
}
```
