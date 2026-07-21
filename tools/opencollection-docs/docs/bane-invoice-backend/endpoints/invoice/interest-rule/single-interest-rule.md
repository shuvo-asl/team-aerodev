# single interest rule

**GET** `{{url}}/api/interest-rule/9/`

## Auth

Type: `bearer`

## Examples

### New Request

**Request:** `GET` `{{url}}/api/interest-rule/9/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Interest Rule Fetched Successfully",
    "data": {
        "result": {
            "id": 9,
            "name": "vxcv",
            "is_default": false,
            "is_cumulative": true,
            "max_repetition": 12,
            "interest_type": "fixed",
            "interest_rate": 230,
            "interest_base": "",
            "interest_day": null
        }
    }
}
```
