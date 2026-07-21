# export coa/client

**GET** `{{url}}/api/export-import/?file_type=csv&model=coa`

## Auth

Type: `bearer`

## Query Params

| Name | Value | Type |
|---|---|---|
| `file_type` | `csv` | query |
| `model` | `coa` | query |

## Headers

| Name | Value |
|---|---|
| `file_type` | `csv` |
| `model` | `coa` |

## Examples

### New Request

**Request:** `GET` `{{url}}/api/export-import/?file_type=csv&model=coa`

**Response:** `200 OK`

```json
account_name,code,account_type,details,transaction_type,source
22,22,FIXED,,non_expense,xero
11,11,NONCURRENT,,non_expense,xero
a testing,0001,FIXED,,non_expense,xero
city afg,,BANK,,non_expense,xero
CITY BDT,1234,BANK,,non_expense,xero
CITY USD,,BANK,,non_expense,xero
Owner A Share Capital,970,EQUITY,The value of shares purchased by the shareholders,non_expense,xero
Retained Earnings,960,EQUITY,Do not Use,non_expense,xero
Loan,900,TERMLIAB,Money that has been borrowed from a creditor,non_expense,xero
Owner A Funds Introduced,881,CURRLIAB,Funds contributed by the owner,non_expense,xero
Owner A Drawings,880,CURRLIAB,Withdrawals by the owners,non_expense,xero
Tracking Transfers,877,CURRLIAB,Transfers between tracking categories,non_expense,xero
Rounding,860,CURRLIAB,An adjustment entry to allow for rounding,non_expense,xero
Suspense,850,CURRLIAB,"An entry that allows an unknown transaction to be entered, so the accounts can still be worked on in balance and the entry can be dealt with later.",non_expense,xero
Historical Adjustment,840,CURRLIAB,For accountant adjustments,non_expense,xero
Income Tax Payable,830,CURRLIAB,"The amount of income tax that is due to be paid, also resident withholding tax paid on interest received.",non_expense,xero
Superannuation Payable,826,CURRLIAB,The amount of superannuation that is due to be paid,non_expense,xero
Employee Tax Payable,825,CURRLIAB,The amount of tax that has been deducted from wages or salaries paid to employes and is due to be paid,non_expense,xero
Sales Tax,820,CURRLIAB,"The balance in this account represents Sales Tax owing to or from your tax authority. At the end of the tax period, it is this account that should be used to code against either the 'refunds from' or 'payments to' your tax authority that will appear on the bank statement. Xero has been designed to use only one sales tax account to track sales taxes on income and expenses, so there is no need to add any new sales tax accounts to Xero.",non_expense,xero
Wages Payable,803,CURRLIAB,Xero automatically updates this account for payroll entries created using Payroll and will store the payroll amount to be paid to the employee for the pay run. This account enables you to maintain separate accounts for employee Wages Payable amounts and Accounts Payable amounts,non_expense,xero
Unpaid Expense Claims,801,CURRLIAB,Expense claims typically made by employees/shareholder employees still outstanding.,non_expense,xero
Accounts Payable,800,CURRLIAB,Outstanding invoices the company has received from suppliers but has not yet paid at balance date,non_expense,xero
Less Accumulated Depreciation on Computer Equipment,721,FIXED,The total amount of computer equipment cost that has been consumed by the business (based on the useful life),non_expense,xero
Computer Equipment,720,FIXED,Computer equipment that is owned and controlled by the business,non_expense,xero
Less Accumulated Depreciation on Office Equipment,711,FIXED,The total amount of office equipment cost that has been consumed by the entity (based on the useful life),non_expense,xero
Office Equipment,710,FIXED,Office equipment that is owned and controlled by the business,non_expense,xero
Inventory,630,INVENTORY,Value of tracked items for resale.,non_expense,xero
Prepayments,620,CURRENT,An expenditure that has been paid for in advance.,non_expense,xero
Accounts Receivable,610,CURRENT,Outstanding invoices the company has issued out to the client but has not yet received in cash at balance date.,non_expense,xero
Income Tax Expense,505,EXPENSE,A percentage of total earnings paid to the government.,expense,xero
Realised Currency Gains,499,EXPENSE,Gains or losses made due to currency exchange rate changes,expense,xero
Unrealised Currency Gains,498,EXPENSE,Unrealised currency gains on outstanding items,expense,xero
Bank Revaluations,497,EXPENSE,Bank account revaluations due for foreign exchange rate changes,expense,xero
Travel - International,494,EXPENSE,Expenses incurred from international travel which has a business purpose,expense,xero
Travel - National,493,EXPENSE,Expenses incurred from domestic travel which has a business purpose,expense,xero
Telephone & Internet,489,EXPENSE,"Expenditure incurred from any business-related phone calls, phone lines, or internet connections",expense,xero
Subscriptions,485,EXPENSE,"E.g. Magazines, professional bodies",expense,xero
Superannuation,478,EXPENSE,Superannuation contributions,expense,xero
Wages and Salaries,477,EXPENSE,Payment to employees in exchange for their resources,expense,xero
Repairs and Maintenance,473,EXPENSE,Expenses incurred on a damaged or run down asset that will bring the asset back to its original condition.,expense,xero
Rent,469,EXPENSE,The payment to lease a building or area.,expense,xero
Printing & Stationery,461,EXPENSE,Expenses incurred by the entity as a result of printing and stationery,expense,xero
Office Expenses,453,EXPENSE,General expenses related to the running of the business office.,expense,xero
Motor Vehicle Expenses,449,EXPENSE,Expenses incurred on the running of company motor vehicles,expense,xero
"Light, Power, Heating",445,EXPENSE,"Expenses incurred for lighting, powering or heating the premises",expense,xero
Legal expenses,441,EXPENSE,Expenses incurred on any legal matters,expense,xero
Interest Expense,437,EXPENSE,"Any interest expenses paid to your tax authority, business bank accounts or credit card accounts.",expense,xero
Insurance,433,EXPENSE,Expenses incurred for insuring the business' assets,expense,xero
General Expenses,429,EXPENSE,General expenses related to the running of the business.,expense,xero
Freight & Courier,425,EXPENSE,Expenses incurred on courier & freight costs,expense,xero
Entertainment,420,EXPENSE,Expenses paid by company for the business but are not deductable for income tax purposes.,expense,xero
Depreciation,416,EXPENSE,The amount of the asset's cost (based on the useful life) that was consumed during the period,expense,xero
Consulting & Accounting,412,EXPENSE,Expenses related to paying consultants,expense,xero
Cleaning,408,EXPENSE,Expenses incurred for cleaning  business property.,expense,xero
Bank Fees,404,EXPENSE,Fees charged by your bank for transactions regarding your bank account(s).,expense,xero
Advertising,400,EXPENSE,Expenses incurred for advertising while trying to increase sales,expense,xero
Cost of Goods Sold,310,DIRECTCOSTS,Cost of goods sold by the business,expense,xero
Interest Income,270,REVENUE,Interest income,non_expense,xero
Other Revenue,260,REVENUE,Any other income that does not relate to normal business activities and is not recurring,non_expense,xero
Sales,200,REVENUE,Income from any normal business activity,non_expense,xero
```
