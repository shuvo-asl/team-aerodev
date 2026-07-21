# get chart of account mappings

**GET** `{{url}}/api/coa-mapping/from-company/1/to-company/2/?limit=2&page=1`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `limit` | `2` | query |
| `page` | `1` | query |

## Examples

### get chart of account mappings

**Request:** `GET` `{{url}}/api/coa-mapping/from-company/1/to-company/2/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chart of account mapping Successfully Fetched",
    "data": {
        "result": [
            {
                "from_account": 1,
                "to_account": 1653
            },
            {
                "from_account": 2,
                "to_account": 1654
            }
        ]
    }
}
```

### paginated coa  mapping list

**Request:** `GET` `{{url}}/api/coa-mapping/from-company/1/to-company/2/?limit=2&page=1`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Chart of account mapping Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 2,
        "total_page": 1,
        "result": [
            {
                "from_account": 1,
                "to_account": 1653
            },
            {
                "from_account": 2,
                "to_account": 1654
            }
        ]
    }
}
```
