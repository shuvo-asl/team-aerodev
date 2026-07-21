# Get API Token

**POST** `{{url}}/api-token`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "host": "172.16.0.2"
}
```

## Examples

### Get API Token

**Request:** `POST` `{{url}}/api-token`

```json
{
    "host": "172.29.0.1",
    "days": 2
}
```

**Response:** `201 CREATED`

```json
{
    "data": {
        "token": "f904b1079bba69bc"
    },
    "error": null,
    "errors": null,
    "message": "successful"
}
```
