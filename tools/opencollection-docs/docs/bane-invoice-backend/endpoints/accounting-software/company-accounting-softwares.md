# company accounting softwares

**GET** `{{url}}/api/company-accounting-software/?page=1&limit=10`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `page` | `1` | query |
| `limit` | `10` | query |

## Examples

### company inactive accounting softwares

**Request:** `GET` `{{url}}/api/company-accounting-software/?page=1&limit=10&is_active=false`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Accounting Software Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 1,
        "total_page": 1,
        "result": [
            {
                "is_active": false,
                "name": "Xero-Asl",
                "id": 27,
                "accounting_software_id": 30,
                "connected": false,
                "accounting_software_type": "Flow Account"
            }
        ]
    }
}
```

### company active accounting softwares

**Request:** `GET` `{{url}}/api/company-accounting-software/?page=1&limit=10`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Accounting Software Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 1,
        "total_page": 1,
        "result": [
            {
                "is_active": true,
                "name": "xero",
                "id": 26,
                "accounting_software_id": 1,
                "connected": true,
                "accounting_software_type": "xero"
            }
        ]
    }
}
```

### company All accounting softwares

**Request:** `GET` `{{url}}/api/company-accounting-software/?page=1&limit=10`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Accounting Software Successfully Fetched",
    "data": {
        "next": null,
        "previous": null,
        "current_page": 1,
        "total_object": 2,
        "total_page": 1,
        "result": [
            {
                "is_active": true,
                "name": "xero",
                "id": 26,
                "accounting_software_id": 1,
                "connected": true,
                "accounting_software_type": "xero"
            },
            {
                "is_active": false,
                "name": "Xero-Asl",
                "id": 27,
                "accounting_software_id": 30,
                "connected": false,
                "accounting_software_type": "Flow Account"
            }
        ]
    }
}
```
