# get additional email of client

**GET** `{{url}}/api/clients-additional-email/?client=40`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `client` | `40` | query |
| `page` | `1` | query |
| `limit` | `2` | query |

## Body

Type: `text`

```
{
    "client": 40, 
    "emails": ["client6@gmail.com"]
}
```

## Examples

### get additional email of client

**Request:** `GET` `{{url}}/api/clients-additional-email/?client=40`

```json
{
    "client": 40, 
    "emails": ["client6@gmail.com"]
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Client's Additional Email Successfully Fetched",
    "data": {
        "result": [
            {
                "id": 9,
                "email": "client6@gmail.com"
            },
            {
                "id": 10,
                "email": "client7@gmail.com"
            }
        ]
    }
}
```
