# delete accounting software

**DELETE** `{{url}}/api/accounting-software/8/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `json`

```json
{
    "name": "flow",
    "credentials": {"api_secret": "very secret key"}
}
```

## Examples

### create accounting software Copy

**Request:** `DELETE` `{{url}}/api/accounting-software/8/`

```json
{
    "name": "flow",
    "credentials": {"api_secret": "very secret key"}
}
```

**Response:** `204 No Content`

```json
{
    "status": "success",
    "message": "Accounting Software Successfully Deleted",
    "data": {
        "result": []
    }
}
```
