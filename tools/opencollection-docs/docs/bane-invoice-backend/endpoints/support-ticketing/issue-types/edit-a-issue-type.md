# edit a issue type

**PATCH** `{{url}}/api/issue-types/4/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "name": "server error2",
    "handlers": [1]
}
```

## Examples

### New Request

**Request:** `PATCH` `{{url}}/api/issue-types/4/`

```json
{
    "name": "server error2"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Issue Type successfully updated",
    "data": {
        "result": {
            "id": 4,
            "name": "server error2"
        }
    }
}
```

### edit a issue type

**Request:** `PATCH` `{{url}}/api/issue-types/4/`

```json
{
    "name": "server error2",
    "handlers": [1]
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Issue Type successfully updated",
    "data": {
        "result": {
            "id": 4,
            "name": "server error2",
            "handlers": [
                {
                    "id": 1,
                    "name": "Admin Admin"
                }
            ]
        }
    }
}
```
