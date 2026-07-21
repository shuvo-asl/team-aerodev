# dashbaord

**GET** `{{url}}/api/dashboard/`

## Auth

Type: `bearer`

## Examples

### dashbaord

**Request:** `GET` `{{url}}/api/dashboard/`

**Response:** `200 OK`

```json
{
    "status": "success",
    "message": "Dashboard successfully fetched",
    "data": {
        "result": {
            "overdue_invoices": [
                {
                    "invoice_no": "INV-000222",
                    "client": "Baidu",
                    "due_date": "2024-11-10",
                    "due": 6
                },
                {
                    "invoice_no": "INV-000221",
                    "client": "Baidu",
                    "due_date": "2024-11-10",
                    "due": 10
                },
                {
                    "invoice_no": "INV-000220",
                    "client": "Baidu",
                    "due_date": "2024-11-10",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000219",
                    "client": "Baidu",
                    "due_date": "2024-11-10",
                    "due": 3
                },
                {
                    "invoice_no": "INV-000218",
                    "client": "Baidu",
                    "due_date": "2024-11-10",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000217",
                    "client": "Baidu",
                    "due_date": "2024-11-09",
                    "due": 6
                },
                {
                    "invoice_no": "INV-000216",
                    "client": "Baidu",
                    "due_date": "2024-11-09",
                    "due": 6
                },
                {
                    "invoice_no": "INV-000215",
                    "client": "Baidu",
                    "due_date": "2024-11-09",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000211",
                    "client": "test123",
                    "due_date": "2024-11-06",
                    "due": 136
                },
                {
                    "invoice_no": "INV-000210",
                    "client": "Baidu",
                    "due_date": "2024-11-04",
                    "due": 6
                },
                {
                    "invoice_no": "INV-000206",
                    "client": "Baidu",
                    "due_date": "2024-11-04",
                    "due": 3
                },
                {
                    "invoice_no": "INV-000205",
                    "client": "Baidu",
                    "due_date": "2024-11-04",
                    "due": 18
                },
                {
                    "invoice_no": "INV-000204",
                    "client": "Baidu",
                    "due_date": "2024-11-04",
                    "due": 12
                },
                {
                    "invoice_no": "INV-000203",
                    "client": "Baidu",
                    "due_date": "2024-11-04",
                    "due": 4
                },
                {
                    "invoice_no": "INV-000202",
                    "client": "Baidu",
                    "due_date": "2024-11-04",
                    "due": 3
                },
                {
                    "invoice_no": "INV-000201",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000200",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000199",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000198",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 4
                },
                {
                    "invoice_no": "INV-000197",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 6
                },
                {
                    "invoice_no": "INV-000196",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000195",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000194",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000193",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000192",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 4
                },
                {
                    "invoice_no": "INV-000191",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000190",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 4
                },
                {
                    "invoice_no": "INV-000189",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 3
                },
                {
                    "invoice_no": "INV-000188",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 6
                },
                {
                    "invoice_no": "INV-000187",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 8
                },
                {
                    "invoice_no": "INV-000186",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 4
                },
                {
                    "invoice_no": "INV-000185",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 8
                },
                {
                    "invoice_no": "INV-000183",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 3
                },
                {
                    "invoice_no": "INV-000180",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 3
                },
                {
                    "invoice_no": "INV-000179",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000178",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000177",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 4
                },
                {
                    "invoice_no": "INV-000176",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 4
                },
                {
                    "invoice_no": "INV-000175",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000174",
                    "client": "Baidu",
                    "due_date": "2024-11-03",
                    "due": 60
                },
                {
                    "invoice_no": "INV-000172",
                    "client": "test123",
                    "due_date": "2024-11-03",
                    "due": 8.16
                },
                {
                    "invoice_no": "INV-000170",
                    "client": "test123",
                    "due_date": "2024-11-03",
                    "due": 129.6
                },
                {
                    "invoice_no": "INV-000165",
                    "client": "test123",
                    "due_date": "2024-10-29",
                    "due": 84
                },
                {
                    "invoice_no": "INV-000164",
                    "client": "amit",
                    "due_date": "2024-10-29",
                    "due": 2
                },
                {
                    "invoice_no": "INV-000163",
                    "client": "Arifuzzaman Shoab",
                    "due_date": "2024-10-26",
                    "due": 150
                },
                {
                    "invoice_no": "INV-000162",
                    "client": "amit",
                    "due_date": "2024-10-29",
                    "due": 150
                },
                {
                    "invoice_no": "INV-000159",
                    "client": "Arifuzzaman Shoab",
                    "due_date": "2024-10-23",
                    "due": 19.6
                },
                {
                    "invoice_no": "INV-000158",
                    "client": "Arifuzzaman Shoab",
                    "due_date": "2024-10-23",
                    "due": 40
                },
                {
                    "invoice_no": "INV-000156",
                    "client": "sdfd",
                    "due_date": "2024-11-01",
                    "due": 85.5
                },
                {
                    "invoice_no": "INV-000155",
                    "client": "dfgd",
                    "due_date": "2024-10-25",
                    "due": 610.4
                },
                {
                    "invoice_no": "INV-000154",
                    "client": "spaceY",
                    "due_date": "2024-11-01",
                    "due": 12.88
                },
                {
                    "invoice_no": "INV-000153",
                    "client": "dfgd",
                    "due_date": "2024-10-25",
                    "due": 294
                },
                {
                    "invoice_no": "INV-000152",
                    "client": "dfgd",
                    "due_date": "2024-10-20",
                    "due": 10
                },
                {
                    "invoice_no": "INV-000151",
                    "client": "spaceY",
                    "due_date": "2024-10-29",
                    "due": 3
                },
                {
                    "invoice_no": "INV-000150",
                    "client": "Arifuzzaman Shoab",
                    "due_date": "2024-10-19",
                    "due": 192
                },
                {
                    "invoice_no": "INV-000149",
                    "client": "Ziliun",
                    "due_date": "2024-11-03",
                    "due": 82.5
                },
                {
                    "invoice_no": "INV-000148",
                    "client": "Ziliun",
                    "due_date": "2024-11-04",
                    "due": 474
                },
                {
                    "invoice_no": "INV-000147",
                    "client": "US Bangla",
                    "due_date": "2024-10-10",
                    "due": 353
                },
                {
                    "invoice_no": "INV-000146",
                    "client": "US Bangla",
                    "due_date": "2024-10-10",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000145",
                    "client": "US Bangla",
                    "due_date": "2024-10-18",
                    "due": 295.6
                },
                {
                    "invoice_no": "INV-000144",
                    "client": "spaceY",
                    "due_date": "2024-10-23",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000143",
                    "client": "US Bangla",
                    "due_date": "2024-10-10",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000140",
                    "client": "spaceY",
                    "due_date": "2024-10-23",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000139",
                    "client": "spaceY",
                    "due_date": "2024-10-22",
                    "due": 63
                },
                {
                    "invoice_no": "INV-000138",
                    "client": "Ziliun",
                    "due_date": "2024-10-27",
                    "due": 20
                },
                {
                    "invoice_no": "INV-000137",
                    "client": "spaceY",
                    "due_date": "2024-10-22",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000136",
                    "client": "spaceY",
                    "due_date": "2024-10-22",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000135",
                    "client": "spaceY",
                    "due_date": "2024-11-08",
                    "due": 15
                },
                {
                    "invoice_no": "INV-000134",
                    "client": "spaceY",
                    "due_date": "2024-10-22",
                    "due": 2.37
                },
                {
                    "invoice_no": "INV-000133",
                    "client": "spaceY",
                    "due_date": "2024-10-22",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000132",
                    "client": "spaceY",
                    "due_date": "2024-10-22",
                    "due": 20.22
                },
                {
                    "invoice_no": "INV-000131",
                    "client": "spaceY",
                    "due_date": "2024-10-22",
                    "due": 11
                },
                {
                    "invoice_no": "INV-000130",
                    "client": "spaceY",
                    "due_date": "2024-10-22",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000129",
                    "client": "spaceY",
                    "due_date": "2024-10-22",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000128",
                    "client": "epic client",
                    "due_date": "2024-10-14",
                    "due": 1514
                },
                {
                    "invoice_no": "INV-000127",
                    "client": "bvcd",
                    "due_date": "2024-11-07",
                    "due": 4
                },
                {
                    "invoice_no": "INV-000126",
                    "client": "US Bangla",
                    "due_date": "2024-10-30",
                    "due": 200
                },
                {
                    "invoice_no": "INV-000125",
                    "client": "test",
                    "due_date": "2024-10-22",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000124",
                    "client": "shoab",
                    "due_date": "2024-10-12",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000121",
                    "client": "bvcd",
                    "due_date": "2024-10-21",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000120",
                    "client": "US Bangla",
                    "due_date": "2024-10-08",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000119",
                    "client": "test",
                    "due_date": "2024-10-21",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000118",
                    "client": "US Bangla Testdce4",
                    "due_date": "2024-10-20",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000117",
                    "client": "Ziliun",
                    "due_date": "2024-10-27",
                    "due": 27.5
                },
                {
                    "invoice_no": "INV-000115",
                    "client": "US Bangla Testdce4",
                    "due_date": "2024-11-11",
                    "due": 72.6
                },
                {
                    "invoice_no": "INV-000114",
                    "client": "cvc",
                    "due_date": "2024-10-27",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000113",
                    "client": "ytu",
                    "due_date": "2024-10-12",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000112",
                    "client": "test",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000111",
                    "client": "spaceY",
                    "due_date": "2024-10-18",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000108",
                    "client": "spaceY",
                    "due_date": "2024-10-18",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000107",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000106",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000105",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000104",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000103",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000102",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000101",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000100",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000099",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000098",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000097",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000096",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000095",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000094",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000093",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000092",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000091",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000090",
                    "client": "spaceY",
                    "due_date": "2024-10-17",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000089",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000088",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000087",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000086",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000085",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000084",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000083",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000082",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000081",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000080",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000079",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000078",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000077",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000076",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000075",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000074",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000073",
                    "client": "spaceY",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000072",
                    "client": "test",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000071",
                    "client": "test",
                    "due_date": "2024-10-23",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000070",
                    "client": "test",
                    "due_date": "2024-10-16",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000068",
                    "client": "epic client",
                    "due_date": "2024-10-05",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000067",
                    "client": "bvcd",
                    "due_date": "2024-11-07",
                    "due": 37.8
                },
                {
                    "invoice_no": "INV-000066",
                    "client": "epic client",
                    "due_date": "2024-10-05",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000065",
                    "client": "epic client",
                    "due_date": "2024-10-05",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000064",
                    "client": "epic client",
                    "due_date": "2024-10-05",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000063",
                    "client": "epic client",
                    "due_date": "2024-10-05",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000059",
                    "client": "test",
                    "due_date": "2024-10-15",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000032",
                    "client": "epic client",
                    "due_date": "2024-10-05",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000029",
                    "client": "bvcd",
                    "due_date": "2024-10-14",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000025",
                    "client": "test",
                    "due_date": "2024-11-06",
                    "due": 1600
                },
                {
                    "invoice_no": "INV-000023",
                    "client": "spaceY",
                    "due_date": "2024-10-09",
                    "due": 0
                },
                {
                    "invoice_no": "INV-000021",
                    "client": "US Bangla Test3",
                    "due_date": "2024-10-23",
                    "due": 0
                },
                {
                    "invoice_no": "INV-00005",
                    "client": "Harry",
                    "due_date": "2024-03-24",
                    "due": 0
                },
                {
                    "invoice_no": "INV-00003",
                    "client": "marry",
                    "due_date": "2024-03-24",
                    "due": 0
                },
                {
                    "invoice_no": "INV-00001",
                    "client": "test",
                    "due_date": "2024-03-21",
                    "due": 0
                }
            ],
            "invoice_by_status": {
                "draft": 30,
                "sent": 184,
                "paid": 0,
                "overdue": 0
            },
            "weekly_revenue_trend": {
                "weekly_revenue": [
                    {
                        "date": "2024-10-16",
                        "amount": 294
                    },
                    {
                        "date": "2024-10-17",
                        "amount": 623.28
                    },
                    {
                        "date": "2024-10-20",
                        "amount": 337.5
                    },
                    {
                        "date": "2024-10-21",
                        "amount": 59.6
                    },
                    {
                        "date": "2024-10-22",
                        "amount": 528
                    },
                    {
                        "date": "2024-10-23",
                        "amount": 199
                    },
                    {
                        "date": "2024-10-28",
                        "amount": 799.56
                    },
                    {
                        "date": "2024-10-29",
                        "amount": 86
                    },
                    {
                        "date": "2024-10-31",
                        "amount": 301
                    },
                    {
                        "date": "2024-11-03",
                        "amount": 14
                    },
                    {
                        "date": "2024-11-04",
                        "amount": 49
                    },
                    {
                        "date": "2024-11-12",
                        "amount": 259.8
                    }
                ]
            }
        }
    }
}
```
