# generate third party jwt token pairs

**POST** `{{url}}/api/third-party/token/`

# 🔐 Third-Party Token Exchange API

**POST**

/api/third-party/token/

This endpoint allows a third-party system to exchange a valid external token for access and refresh tokens used in your system. The third-party token must be pre-issued.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| token | string | ✅ Yes | The third-party token issued earlier |

#### Example

``` bash
{
  "token": "example-third-party-token"
}

 ```

## 🔒 Authentication

This endpoint does **not** require authentication.

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{
    "token": "123"
}
```

## Examples

### success

**Request:** `POST` `{{url}}/api/third-party/token/`

```json
{
    "token": "123"
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Tokens Generated Successfully",
    "data": {
        "result": {
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzMjcxNzM5LCJpYXQiOjE3NTMyNDI5MzksImp0aSI6IjY2ZjZhNjMwZGIxZDQxMGZiZmY1NjkyMmRiYTJhMTc0IiwidG9rZW5faWQiOjF9.IunRwm9UP6YeOmUThb9JFPeVZ_3NaZNCANvvzOSDGZc",
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MzI3MTczOSwiaWF0IjoxNzUzMjQyOTM5LCJqdGkiOiJkNzczZGVkZjYzMGU0Nzg4OTc3OWVmZjQ4YzczNWFkZiIsInRva2VuX2lkIjoxfQ.fxUl4KwmDHttG6p0LLXQGFeKSiZQsTdwI8MGHRazC4c"
        }
    }
}
```

### if token is expired

**Request:** `POST` `{{url}}/api/third-party/token/`

```json
{
    "token": "123"
}
```

**Response:** `403 Forbidden`

```json
{
    "status": "failed",
    "message": "Token Expired",
    "error": "Token Expired",
    "errors": null
}
```

### if request made from ip that is not in token

**Request:** `POST` `{{url}}/api/third-party/token/`

```json
{
    "token": "123"
}
```

**Response:** `403 Forbidden`

```json
{
    "status": "failed",
    "message": "IP Mismatch",
    "error": "IP Mismatch",
    "errors": null
}
```

### if token  is deactivated

**Request:** `POST` `{{url}}/api/third-party/token/`

```json
{
    "token": "123"
}
```

**Response:** `403 Forbidden`

```json
{
    "status": "failed",
    "message": "Invalid Token",
    "error": "Invalid Token",
    "errors": null
}
```
