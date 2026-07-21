# delete company data mappings

**DELETE** `{{url}}/api/company-data-mapping-pairs/tax-rate/from/1/to/4/`

## Auth

Type: `bearer`

## Examples

### New Request

**Request:** `DELETE` `{{url}}/api/company-data-mapping-pairs/tax-rate/from/1/to/4/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Company mapping pair Deleted Successfully",
    "data": {
        "result": {
            "delete_count": 1
        }
    }
}
```
