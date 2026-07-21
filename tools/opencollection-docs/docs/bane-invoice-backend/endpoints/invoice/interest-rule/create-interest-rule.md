# create interest rule

**POST** `{{url}}/api/interest-rule/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "name": "interest-d2",
    "is_cumulative": true,
    "interest_day": 22,
    "interest_type": "fixed",
    "interest_rate": 23,
    "max_repetition": 2,
    "is_default": true 
}
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/interest-rule/`

```json
{
    "name": "interest1",
    "is_cumulative": true,
    "day": 23,
    "interest_type": "fixed",
    "interest_rate": 23,
    "max_repetition": 2
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Interest Rule successfully created",
    "data": {
        "result": {
            "name": "interest1",
            "is_default": false,
            "is_cumulative": true,
            "day": 23,
            "max_repetition": 2,
            "interest_type": "fixed",
            "interest_rate": 23,
            "interest_base": ""
        }
    }
}
```
