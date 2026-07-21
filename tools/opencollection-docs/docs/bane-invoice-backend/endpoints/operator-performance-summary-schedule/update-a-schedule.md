# update a schedule

**PATCH** `{{url}}/api/operator-performance-summary-schedule/3/`

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
  "sent_day": 8
}
```

## Examples

### update a schedule

**Request:** `PATCH` `{{url}}/api/operator-performance-summary-schedule/3/`

```json
{
  "sent_day": 8
}
```

**Response:** `200 OK`

```json
{
  "status": "success",
  "message": "Operator Performance Summary Schedule successfully updated",
  "data": {
    "result": {
      "id": 3,
      "title": "test1",
      "to": [
        "oiewjfi@gmail.com"
      ],
      "cc": [],
      "bcc": [],
      "time": null,
      "previous_month": true,
      "start_day": null,
      "end_day": null,
      "sent_day": 8,
      "created_at": "2026-07-02T05:53:12.003979Z",
      "updated_at": "2026-07-02T05:55:34.224375Z"
    }
  }
}
```
