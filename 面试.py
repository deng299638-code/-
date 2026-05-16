from lxml import etree
import requests
import csv

headers = {
}
url = "https://www.chinamoney.com.cn/english/bdInfo/"

res = requests.get(url, headers=headers)
res.encoding = "utf-8"
tree = etree.HTML(res.text)

rows = tree.xpath('//div[@class="result-table"]//tr[td[4]/text()="Treasury Bond" and td[7]/text()="2023"]')

data_list = []
for row in rows:
    typ_list = row.xpath('./td[4]/text()')
    year_list = row.xpath('./td[7]/text()')

    if typ_list and year_list:
        typ = typ_list[0].strip()
        year = year_list[0].strip()
        data_list.append({
            "Bond Type": typ,
            "Issue Year": year
        })

print(data_list)
with open("bond_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Bond Type", "Issue Year"])
    writer.writeheader()
    writer.writerows(data_list)