# delete clients additional email

**DELETE** `{{url}}/api/clients-additional-email/8/?client=40`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `client` | `40` | query |
| `page` | `1` | query |
| `limit` | `2` | query |

## Body

Type: `text`

```
{
    "client": 40, 
    "emails": ["client6@gmail.com"]
}
```
