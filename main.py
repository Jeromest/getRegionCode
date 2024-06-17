import requests
import time
from bs4 import BeautifulSoup

jdCodeList = []


def getJiedao():
    # URL of the target webpage
    url = 'https://xingzhengquhua.bmcx.com/610502__xingzhengquhua/'

    # Send a GET request to fetch the raw HTML content
    response = requests.get(url)

    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table that contains the data
    table = soup.find('table')
    # table = soup.find('table', {'class': 'admin_list_btm'})

    # Extract the headers to find the relevant columns
    headers = table.find_all('tr')
    # headers = table.find_all('th')
    header_names = [header.get_text().strip() for header in headers]

    # 去除所有的镇
    # filtered_header_names = [name for name in header_names if "镇" not in name]
    # 只要街道
    filtered_header_names = [name for name in header_names[3:17] if "街道" in name]

    # Identify the index of the required columns
    # district_index = filtered_header_names.index('所辖行政区')
    # code_index = filtered_header_names.index('行政区划代码')

    # Extract the rows of the table
    rows = table.find_all('tr')[1:]  # Skip the header row

    # Extract the data
    data = []
    for row in rows:
        cells = row.find_all('td')
        district = cells[0].get_text().strip()
        code = 0
        if len(cells) > 1:  # 检查cells长度是否大于1
            if cells[1]:  # 检查cells[1]是否存在
                code = cells[1].get_text().strip()
        data.append((district, code))

    # Print the extracted data
    for district, code in data:
        print(f'{district}: {code}')

    # 街道代码

    for district, code in data:
        if "街道" in district:
            jdCodeList.append(code)
    print(jdCodeList)


# 下面开始获取每一个街道下的社区名称和社区代码


def getShequ(code):
    url2 = 'https://xingzhengquhua.bmcx.com/' + code + '__xingzhengquhua/'

    # Send a GET request to fetch the raw HTML content
    response2 = requests.get(url2)

    # Parse the content of the request with BeautifulSoup
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Find the table that contains the data
    table2 = soup2.find('table')
    # table = soup.find('table', {'class': 'admin_list_btm'})

    # Extract the headers to find the relevant columns
    headers2 = table2.find_all('tr')
    # headers = table.find_all('th')
    header_names2 = [header.get_text().strip() for header in headers2[4:]]

    endFlag = len(header_names2) - 1
    for index, item in enumerate(header_names2):
        if "会员" in item:
            endFlag = index
            break

    filtered_header_names2 = [name for name in header_names2[:endFlag]]
    print(filtered_header_names2)

    # Extract the rows of the table
    rows2 = table2.find_all('tr')[1:]  # Skip the header row

    # Extract the data
    data2 = []
    for row2 in rows2:
        cells2 = row2.find_all('td')
        district2 = cells2[0].get_text().strip()
        code2 = 0
        if len(cells2) > 1:  # 检查cells长度是否大于1
            if cells2[1]:  # 检查cells[1]是否存在
                code2 = cells2[1].get_text().strip()
        data2.append((district2, code2))

    # Print the extracted data
    for district2, code2 in data2:
        print(f'{district2}: {code2}')


if __name__ == '__main__':
    # 街道
    getJiedao()
    for jdCode in jdCodeList:
        # 社区
        getShequ(jdCode)
        time.sleep(1)
