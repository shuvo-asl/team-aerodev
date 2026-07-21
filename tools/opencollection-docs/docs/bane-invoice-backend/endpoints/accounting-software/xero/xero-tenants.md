# Xero Tenants

**GET** `{{url}}/api/xero/tenants/`

## Auth

Type: `inherit`

## Headers

| Name | Value |
|---|---|
| `Authorization` | `Bearer {{token}}` |

## Body

Type: `multipart-form`

## Examples

### Tenants

**Request:** `GET` `{{url}}/api/xero/tenants/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Fetched 'Xero' Tenants Successfully",
    "data": {
        "result": [
            {
                "id": "a8d5c66c-483d-4966-9f43-50a26635ffd3",
                "tenantId": "fc0e7a37-f74b-4c2a-9779-4ec0a1e7a2ff",
                "authEventId": "5f17bf0b-2aec-4c17-9f14-fed7088f9795",
                "tenantType": "ORGANISATION",
                "tenantName": "Bane",
                "createdDateUtc": "2024-09-04T10:33:58.634847+00:00",
                "updatedDateUtc": "2024-09-10T06:26:35.846466+00:00",
                "organisations": {
                    "Organisations": [
                        {
                            "OrganisationID": "fc0e7a37-f74b-4c2a-9779-4ec0a1e7a2ff",
                            "APIKey": "5SVRVENZMMZTOJXFHKQM3CDOSZETJJ",
                            "Name": "Bane",
                            "LegalName": "Bane",
                            "PaysTax": true,
                            "Version": "GLOBAL",
                            "OrganisationType": "COMPANY",
                            "BaseCurrency": "BDT",
                            "CountryCode": "BD",
                            "IsDemoCompany": false,
                            "OrganisationStatus": "ACTIVE",
                            "FinancialYearEndDay": 31,
                            "FinancialYearEndMonth": 12,
                            "DefaultSalesTax": "Tax Exclusive",
                            "DefaultPurchasesTax": "Tax Exclusive",
                            "CreatedDateUTC": "/Date(1725427076000+0000)/",
                            "Timezone": "BANGLADESHSTANDARDTIME",
                            "OrganisationEntityType": "COMPANY",
                            "ShortCode": "!Tm!!7",
                            "Class": "TRIAL",
                            "Edition": "BUSINESS",
                            "LineOfBusiness": "Software publishing",
                            "Addresses": [],
                            "Phones": [],
                            "ExternalLinks": [],
                            "PaymentTerms": {}
                        }
                    ]
                }
            }
        ]
    }
}
```
