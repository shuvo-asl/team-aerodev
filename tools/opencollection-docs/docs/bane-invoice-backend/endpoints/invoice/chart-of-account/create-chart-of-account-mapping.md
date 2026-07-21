# create chart of account mapping

**POST** `{{url}}/api/coa-mapping/2/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
[
    {
        "from_account": 1,
        "to_account": 1653
    },
    {
        "from_account": 1,
        "to_account": 16544
    }
]
```

## Examples

### create chart of account mapping

**Request:** `POST` `{{url}}/api/coa-mapping/2/`

```json
[
    {
        "from_account": 1,
        "to_account": 1653
    },
    {
        "from_account": 2,
        "to_account": 1654
    }
]
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chart of account mapping created successfully",
    "data": {
        "result": [
            {
                "id": 1,
                "from_company": 1,
                "to_company": 2,
                "from_account": 1,
                "to_account": 1653
            },
            {
                "id": 2,
                "from_company": 1,
                "to_company": 2,
                "from_account": 2,
                "to_account": 1654
            }
        ]
    }
}
```

### if one coa is eing mapped to multiple coa

**Request:** `POST` `{{url}}/api/coa-mapping/2/`

```json
[
    {
        "from_account": 1,
        "to_account": 1653
    },
    {
        "from_account": 1,
        "to_account": 1654
    }
]
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to create Chart of account mapping",
    "error": null,
    "errors": [
        {
            "from_account": "A Chart Of account can be mapped to only one Chart Of account"
        },
        {
            "from_account": "A Chart Of account can be mapped to only one Chart Of account"
        }
    ]
}
```

### if invalid coa is provided

**Request:** `POST` `{{url}}/api/coa-mapping/2/`

```json
[
    {
        "from_account": 1,
        "to_account": 1653
    },
    {
        "from_account": 1,
        "to_account": 16544
    }
]
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to create Chart of account mapping",
    "error": null,
    "errors": [
        {},
        {
            "to_account": "Invalid pk \"16544\" - object does not exist."
        }
    ]
}
```
