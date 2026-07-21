# change default status

**PATCH** `{{url}}/api/interest-rule/10/set_default/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "is_default": true
}
```

## Examples

### New Request

**Request:** `PATCH` `{{url}}/api/interest-rule/10/set_default/`

```json
{
    "is_default": true
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Interest Rule's default status has been changed successfully",
    "data": {
        "result": {}
    }
}
```
