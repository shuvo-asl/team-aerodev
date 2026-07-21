# create tax rate mapping

**POST** `{{url}}/api/tax-rate-mapping/2/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
[
    {
        "from_tax_rate": 1,
        "to_tax_rate": 21
    },
    {
        "from_tax_rate": 2,
        "to_tax_rate": 223
    }
]
```

## Examples

### New Request

**Request:** `POST` `{{url}}/api/tax-rate-mapping/2/`

```json
[
    {
        "from_tax_rate": 1,
        "to_tax_rate": 21
    },
    {
        "from_tax_rate": 2,
        "to_tax_rate": 22
    }
]
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Tax rate mapping successfully created",
    "data": {
        "result": [
            {
                "id": 1,
                "from_company": 1,
                "to_company": 2,
                "from_tax_rate": 1,
                "to_tax_rate": 21
            },
            {
                "id": 2,
                "from_company": 1,
                "to_company": 2,
                "from_tax_rate": 2,
                "to_tax_rate": 22
            }
        ]
    }
}
```

### if same tax rate is tried to map to multiple tax rates

**Request:** `POST` `{{url}}/api/tax-rate-mapping/2/`

```json
[
    {
        "from_tax_rate": 1,
        "to_tax_rate": 21
    },
    {
        "from_tax_rate": 1,
        "to_tax_rate": 22
    }
]
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to create Tax rate mapping",
    "error": null,
    "errors": [
        {
            "from_tax_rate": "A tax rate can be mapped to only one tax rate"
        },
        {
            "from_tax_rate": "A tax rate can be mapped to only one tax rate"
        }
    ]
}
```

### if invalid pk is provided

**Request:** `POST` `{{url}}/api/tax-rate-mapping/2/`

```json
[
    {
        "from_tax_rate": 1,
        "to_tax_rate": 21
    },
    {
        "from_tax_rate": 2,
        "to_tax_rate": 223
    }
]
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to create Tax rate mapping",
    "error": null,
    "errors": [
        {},
        {
            "to_tax_rate": "Invalid pk \"223\" - object does not exist."
        }
    ]
}
```
