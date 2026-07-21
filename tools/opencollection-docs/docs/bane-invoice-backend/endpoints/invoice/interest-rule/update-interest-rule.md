# update interest rule

**PATCH** `{{url}}/api/interest-rule/1/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "is_cumulative": false,
    "interest_base": "invoice_base_amount"
}
```

## Examples

### New Request

**Request:** `PATCH` `{{url}}/api/interest-rule/1/`

```json
{
    "is_cumulative": false,
    "interest_base": "invoice_base_amount"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Interest Rule successfully updated",
    "data": {
        "result": {
            "id": 1,
            "name": "interest1",
            "is_default": false,
            "is_cumulative": false,
            "day": 23,
            "max_repetition": 2,
            "interest_type": "fixed",
            "interest_rate": 23,
            "interest_base": "invoice_base_amount"
        }
    }
}
```
