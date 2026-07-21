# sse ticket events

**GET** `{{url}}/sse/ticket-events/`

## Auth

Type: `bearer`

## Examples

### sse ticket events

**Request:** `GET` `{{url}}/sse/ticket-events/`

**Response:** `200 OK`

```json
data: {"id": 5, "ticket": "TCK-00001", "event_type": "comment_created", "payload": {"text": "example text", "user_id": 1, "attachments": [{"id": 6, "url": "http://localhost:5011/api/media/comment_attachments/bdflag_VnJEINj.jpg"}]}, "created_at": "2026-01-07T07:07:20.356919+00:00"}

data: {"id": 6, "ticket": "TCK-00001", "event_type": "comment_created", "payload": {"text": "example text", "user_id": 1, "attachments": [{"id": 7, "url": "http://localhost:5011/api/media/comment_attachments/bdflag_DgwRRhn.jpg"}]}, "created_at": "2026-01-07T07:08:10.818985+00:00"}
```
