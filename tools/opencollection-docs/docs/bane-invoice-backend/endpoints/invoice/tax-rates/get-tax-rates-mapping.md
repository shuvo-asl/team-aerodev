# get tax rates mapping

**GET** `{{url}}/api/tax-rate-mapping/from-company/1/to-company/2/?limit=2&page=1`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `2` | query |
| `page` | `1` | query |

## Body

Type: `text`

```
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

## Examples

### New Request

**Request:** `GET` `{{url}}/api/tax-rate-mapping/from-company/1/to-company/2/`

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

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Tax rate mapping Successfully Fetched",
    "data": {
        "result": [
            {
                "from_tax_rate": 1,
                "to_tax_rate": 21
            },
            {
                "from_tax_rate": 2,
                "to_tax_rate": 22
            }
        ]
    }
}
```

### paginated mapping list

**Request:** `GET` `{{url}}/api/tax-rate-mapping/from-company/1/to-company/2/?limit=2&page=1`

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

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Tax rate mapping Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 2,
        "total_page": 1,
        "result": [
            {
                "from_tax_rate": 1,
                "to_tax_rate": 21
            },
            {
                "from_tax_rate": 2,
                "to_tax_rate": 22
            }
        ]
    }
}
```
