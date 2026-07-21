# create ticket

**POST** `{{url}}/api/tickets/`

## Auth

Type: `bearer`

## Body

Type: `multipart-form`

```
[{'name': 'issue_type', 'type': 'text', 'value': '1'}, {'name': 'subject', 'type': 'text', 'value': 'example subject'}, {'name': 'description', 'type': 'text', 'value': 'example description'}, {'name': 'attachments[0]', 'type': 'file', 'value': ['postman-cloud:///1ef7eff2-7e20-49a0-aa44-c41b878eb3de']}, {'name': 'attachments[1]', 'type': 'file', 'value': ['/home/asl/Pictures/logo.jpeg']}]
```

## Examples

### create ticket

**Request:** `POST` `{{url}}/api/tickets/`

```json
[{'name': 'issue_type', 'type': 'text', 'value': '1'}, {'name': 'subject', 'type': 'text', 'value': 'example subject'}, {'name': 'description', 'type': 'text', 'value': 'example description'}, {'name': 'attachments[0]', 'type': 'file', 'value': ['postman-cloud:///1ef7eff2-7e20-49a0-aa44-c41b878eb3de']}, {'name': 'attachments[1]', 'type': 'file', 'value': ['/home/asl/Pictures/logo.jpeg']}]
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Ticket successfully created",
    "data": {
        "result": {
            "id": 30,
            "reference_id": "TCK-00030",
            "issue_type": 1,
            "subject": "example subject",
            "status": "pending",
            "priority": "medium",
            "client": 19,
            "assigned_to": null,
            "created_at": "2025-05-15T09:53:01.467603+06:00",
            "issue_type_name": "Payment",
            "client_name": "AIR OP",
            "assigned_to_name": ""
        }
    }
}
```

### create ticket

**Request:** `POST` `{{url}}/api/tickets/`

```json
[{'name': 'issue_type', 'type': 'text', 'value': '1'}, {'name': 'subject', 'type': 'text', 'value': 'example subject'}, {'name': 'description', 'type': 'text', 'value': 'example description'}, {'name': 'attachments[0]', 'type': 'file', 'value': ['postman-cloud:///1ef7eff2-7e20-49a0-aa44-c41b878eb3de']}, {'name': 'attachments[1]', 'type': 'file', 'value': ['/home/asl/Pictures/annie-spratt-BAEyXAaBm_Q-unsplash.jpg']}]
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Ticket Failed To Create",
    "error": null,
    "errors": {
        "attachments": {
            "attachments": "File size exceeds 2 MB limit"
        }
    }
}
```

### create ticket

**Request:** `POST` `{{url}}/api/tickets/`

```json
[{'name': 'issue_type', 'type': 'text', 'value': '1'}, {'name': 'subject', 'type': 'text', 'value': 'example subject'}, {'name': 'description', 'type': 'text', 'value': 'example description'}, {'name': 'attachments[0]', 'type': 'file', 'value': ['postman-cloud:///1ef7eff2-7e20-49a0-aa44-c41b878eb3de']}, {'name': 'attachments[1]', 'type': 'file', 'value': ['/home/asl/Documents/projects/bane-invoice-backend/main/settings.py']}]
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Ticket Failed To Create",
    "error": null,
    "errors": {
        "attachments": {
            "attachments": "Unsupported file type. Supported types: pdf, jpeg, jpg, png."
        }
    }
}
```
