# duplicate invoices

**POST** `{{url}}/api/duplicate-invoice`

## 📄 Instructions for Using the Duplicate Invoice API

### ✅ Purpose

This API allows duplicating an invoice from the **current active company** to **one or more other companies** (where the user has access). The same invoice number and items will be duplicated.

**Only GENERAL type invoices can be duplicated.**

📥 Required Request Fields

{  
"invoice": , // Invoice ID (must belong to current company)  
"companies": \[, \] // List of company IDs where to duplicate  
}

#### Field Details:

- `invoice`: ID of the invoice that needs to be duplicated.
    
- `companies`: List of company IDs. User must have access to all these companies.
    

🛑 Validation & Errors

**Invoice Not Found**

- If the given invoice ID doesn't exist or doesn't belong to current company.
    

{  
"status": "failed",  
"message": "Failed to duplicate invoices",  
"error": "Invoice not found"  
}

**User Has No Access to One or More Companies**

- If user doesn’t belong to one or more of the `companies` list.
    

{  
"status": "failed",  
"message": "Failed to duplicate invoices",  
"errors": {  
"companies": {  
"error": "Companies Not found",  
"company_ids": \[202, 203\]  
}  
}  
}

**Invoice Already Exists in One or More Companies**

- If the target companies already have an invoice with the same invoice number.
    

{  
"status": "failed",  
"message": "Failed to duplicate invoices",  
"errors": {  
"companies": {  
"error": "Invoice already exists",  
"company_ids": \[201\]  
}  
}  
}

- ⚠️ Other Notes
    
    - Invoices will be duplicated as `DRAFT` status.
        
    - Client will only be assigned to duplicated invoice if it already exists in that target company.

## Auth

Type: `bearer`

## Body

Type: `json`

```json
{
    "invoice": 316,
    "companies": [12, 28]
}
```

## Examples

### duplicate invoices

**Request:** `POST` `{{url}}/api/duplicate-invoice`

```json
{
    "invoice": 292,
    "companies": [12, 28]
}
```

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Invoice duplicated successfully",
    "data": {
        "result": {}
    }
}
```

### exception given companies already have invoice with given invoices's number

**Request:** `POST` `{{url}}/api/duplicate-invoice`

```json
{
    "invoice": 316,
    "companies": [12, 28]
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to duplicate invoices",
    "error": null,
    "errors": {
        "companies": {
            "error": "Invoice already exists",
            "company_ids": [
                12,
                28
            ]
        }
    }
}
```

### exception when user is not member of target companies

**Request:** `POST` `{{url}}/api/duplicate-invoice`

```json
{
    "invoice": 316,
    "companies": [3]
}
```

**Response:** `400 Bad Request`

```json
{
    "status": "failed",
    "message": "Failed to duplicate invoices",
    "error": null,
    "errors": {
        "companies": {
            "error": "Companies Not found",
            "company_ids": [
                3
            ]
        }
    }
}
```
