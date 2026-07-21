# adsb connection check success

**POST** `{{url}}/api/adsb-connection/`

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{"status": "success", "data": "data"}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/adsb-connection/`

```json
{"status": "success", "data": "data"}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "ADSB connection successful",
    "data": {
        "result": {
            "status": "success",
            "data": "data"
        }
    }
}
```
