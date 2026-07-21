# get a issue type

**GET** `{{url}}/api/issue-types/10`

## Auth

Type: `bearer`

## Body

Type: `text`

```
{
    "name": "server error"
}
```

## Examples

### New Request

**Request:** `GET` `{{url}}/api/issue-types/10`

```json
{
    "name": "server error"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Issue Type Fetched Successfully",
    "data": {
        "result": {
            "id": 10,
            "name": "Slow UI901",
            "handlers": [
                {
                    "id": 3,
                    "name": "Jeff Bezos"
                },
                {
                    "id": 1,
                    "name": "Admin Admin"
                }
            ]
        }
    }
}
```
