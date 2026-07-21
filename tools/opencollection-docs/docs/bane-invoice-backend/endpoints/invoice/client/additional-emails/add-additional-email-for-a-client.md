# add additional email for a client

**POST** `{{url}}/api/clients-additional-email/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "client": 40, 
    "emails": ["client7@gmail.com"]
}
```

## Examples

### add additional email for a client

**Request:** `POST` `{{url}}/api/clients-additional-email/`

```json
{
    "client": 40, 
    "emails": ["client7@gmail.com"]
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Client's Additional Email successfully created",
    "data": {
        "result": [
            {
                "id": 10,
                "email": "client7@gmail.com"
            }
        ]
    }
}
```
