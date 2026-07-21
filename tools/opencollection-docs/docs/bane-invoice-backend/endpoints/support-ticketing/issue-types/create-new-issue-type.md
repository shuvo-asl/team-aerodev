# create new issue type

**POST** `{{url}}/api/issue-types/`

**Description:**

Creates a new issue type with a **unique name**. You may optionally assign handler users.

**Request Body:**

``` json
{
  "name": "Slow UI901",
  "handlers": [1, 3]  // Optional
}

 ```

**Field Details:**

- `name` _(string, required)_ – Must be unique across all issue types.
    
- `handlers` _(list of user IDs, optional)_ – Users assigned to handle this issue type.
    

**Success Response:**

``` json
{
  "status": "success",
  "message": "Issue Type successfully created",
  "data": {
    "result": {
      "id": 10,
      "name": "Slow UI901",
      "handlers": [
        { "id": 3, "name": "Jeff Bezos" },
        { "id": 1, "name": "Admin Admin" }
      ]
    }
  }
}

 ```

``` json
Failure Response (Duplicate Name):
{
"status": "failed",
"message": "Issue Type Failed To Create",
"error": null,
"errors": {
"name": "issue type with this name already exists."
}
}
 ```

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "name": "Slow UI901",
    "handlers": [1, 3]
}
```

## Examples

### create new issue type, type alread exists

**Request:** `POST` `{{url}}/api/issue-types/`

```json
{
    "name": "Slow UI",
    "handlers": [1, 3]
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Issue Type Failed To Create",
    "error": null,
    "errors": {
        "name": "issue type with this name already exists."
    }
}
```

### create new issue type

**Request:** `POST` `{{url}}/api/issue-types/`

```json
{
    "name": "Slow UI901",
    "handlers": [1, 3]
}
```

**Response:** `201 Created`

```json
{
    "status": "success",
    "message": "Issue Type successfully created",
    "data": {
        "result": {
            "id": 10,
            "name": "Slow UI901",
            "handlers": [
                {
                    "id": 3,
                    "name": "Jeff Bezos"
                },
                {
                    "id": 1,
                    "name": "Admin Admin"
                }
            ]
        }
    }
}
```
