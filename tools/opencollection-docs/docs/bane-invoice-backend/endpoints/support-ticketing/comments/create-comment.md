# create comment

**POST** `{{url}}/api/comments/`

## 📝 POST `/api/comments/`

### 📄 Description

Create a new comment for a ticket, optionally including attachments.

### 🔐 Permissions

- Must not require a password change (`requires_password_change = False`)
    
- Must be the ticket `client` or `assigned person`
    
- Ticket must **not** be `CLOSED` or `DISCARDED`
    

### 📤 Request Type

- Content-Type: `multipart/form-data`
    

### 🧾 Form Fields

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `ticket` | int | ✅ Yes | ID of the ticket you're commenting on |
| `text` | string | ✅ Yes | Comment content |
| `attachments[]` | file (array) | ❌ No | Files attached to the comment (e.g. `attachments[0]`, `attachments[1]`) |

📦 Example (Form-Data Keys)

``` bash
ticket = 14  
text = "Please review the attached files"  
attachments[0] = (binary file: "file1.jpg")  
attachments[1] = (binary file: "file2.pdf")

 ```

✅ Success Response  

``` json
{
  "status": "success",
  "message": "Comment Created Successfully",
  "data": {
    "ticket": 14,
    "text": "Please review the attached files",
    "id": 13,
    "created_at": "2025-05-13T12:00:00Z",
    "attachments": [
      {
        "id": 24,
        "file": "http://localhost:5011/api/media/ticket_attachments/file1.jpg"
      },
      {
        "id": 25,
        "file": "http://localhost:5011/api/media/ticket_attachments/file2.pdf"
      }
    ]
  }
}


 ```

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `` | `` | query |

## Body

Type: `multipart-form`

```
[{'name': 'ticket', 'type': 'text', 'value': 'TCK-00014'}, {'name': 'text', 'type': 'text', 'value': 'example text'}, {'name': 'attachments[0]', 'type': 'file', 'value': ['postman-cloud:///1ef7eff2-7e20-49a0-aa44-c41b878eb3de']}]
```

## Examples

### create comment

**Request:** `POST` `{{url}}/api/comments/`

```json
[{'name': 'ticket', 'type': 'text', 'value': 'TCK-00014'}, {'name': 'text', 'type': 'text', 'value': 'example text'}, {'name': 'attachments[0]', 'type': 'file', 'value': ['postman-cloud:///1ef7eff2-7e20-49a0-aa44-c41b878eb3de']}]
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Message successfully created",
    "data": {
        "result": {
            "ticket": "TCK-00014",
            "text": "example text",
            "id": 25,
            "created_at": "2025-05-15T11:49:27.315087+06:00",
            "user": {
                "id": 4,
                "name": "admin1 admin1",
                "profile_image": null
            },
            "attachments": [
                {
                    "id": 9,
                    "file": "http://localhost:5011/api/media/comment_attachments/bdflag_Woee0d1.jpg"
                }
            ]
        }
    }
}
```
