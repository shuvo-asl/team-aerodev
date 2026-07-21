# third party token refresh

**POST** `{{url}}/api/third-party/token/refresh/`

## Auth

Type: `inherit`

## Body

Type: `json`

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MzI3MTczOSwiaWF0IjoxNzUzMjQyOTM5LCJqdGkiOiJkNzczZGVkZjYzMGU0Nzg4OTc3OWVmZjQ4YzczNWFkZiIsInRva2VuX2lkIjoxfQ.fxUl4KwmDHttG6p0LLXQGFeKSiZQsTdwI8MGHRazC4c"
}
```

## Examples

### third party token refresh

**Request:** `POST` `{{url}}/api/third-party/token/refresh/`

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MzI3MTczOSwiaWF0IjoxNzUzMjQyOTM5LCJqdGkiOiJkNzczZGVkZjYzMGU0Nzg4OTc3OWVmZjQ4YzczNWFkZiIsInRva2VuX2lkIjoxfQ.fxUl4KwmDHttG6p0LLXQGFeKSiZQsTdwI8MGHRazC4c"
}
```

**Response:** `200 OK`

```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzMjczMTk2LCJpYXQiOjE3NTMyNDQzOTYsImp0aSI6ImZlYzliOTFlZDE0MTRlNjY5Yzk1MzcyM2E4ZTBmOWZkIiwidG9rZW5faWQiOjF9.q1dl_WiGN5V2Kk_A8WOEhsWl7oJaJjHvSasYDBwLALs",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc1MzI3MTczOSwiaWF0IjoxNzUzMjQyOTM5LCJqdGkiOiJkNzczZGVkZjYzMGU0Nzg4OTc3OWVmZjQ4YzczNWFkZiIsInRva2VuX2lkIjoxfQ.fxUl4KwmDHttG6p0LLXQGFeKSiZQsTdwI8MGHRazC4c"
}
```
