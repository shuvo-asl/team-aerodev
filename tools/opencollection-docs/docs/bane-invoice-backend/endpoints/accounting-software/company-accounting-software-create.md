# company accounting software create

**POST** `{{url}}/api/company-accounting-software/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "name": "xero2",
    "accounting_software": 1
}
```

## Examples

### company accounting software create

**Request:** `POST` `{{url}}/api/company-accounting-software/`

```json
{
    "name": "xero2",
    "accounting_software": 1
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Accounting Software Failed To Create",
    "error": "This Accounting Software is already assigned to this company!",
    "errors": null
}
```
