# adsb connection check failed

**POST** `{{url}}/api/adsb-connection/`

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{
    "status": "failed"
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/adsb-connection/`

```json
{
    "status": "failed"
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed connection",
    "error": "failed",
    "errors": null
}
```
