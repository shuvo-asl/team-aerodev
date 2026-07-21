# update company accounting softwares

**PATCH** `{{url}}/api/company-accounting-software/1/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "is_active": true
}
```

## Examples

### New Request

**Request:** `PATCH` `{{url}}/api/company-accounting-software/1/`

```json
{
    "is_active": false
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Accounting Software successfully updated",
    "data": {
        "result": {
            "is_active": false,
            "name": "test_soft2",
            "id": 1
        }
    }
}
```
