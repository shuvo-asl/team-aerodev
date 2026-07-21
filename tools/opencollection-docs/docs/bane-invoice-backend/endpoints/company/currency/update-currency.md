# Update Currency

**PATCH** `{{url}}/api/currency/2/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "current_rate": "5"
}
```

## Examples

### Update Currency

**Request:** `PATCH` `{{url}}/api/currency/2/`

```json
{
    "current_rate": "5"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Currency successfully updated",
    "data": {
        "result": {
            "id": 2,
            "prefix": "$",
            "short_key": "BDT",
            "current_rate": 5,
            "default": null
        }
    }
}
```
