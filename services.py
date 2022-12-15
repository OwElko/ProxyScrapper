import requests
from lxml import html
from base64 import b64decode
from re import match as re_match
from re import search as re_search
from json import loads as json_loads


def is_ip_address(ip_string):
    return bool(re_match(r"\d{2,3}.\d{2,3}.\d{2,3}.\d{2,3}", ip_string))


def get_html(url, return_type='tree'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Apple \
        WebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    if return_type == 'tree':
        tree = html.fromstring(response.content)
        return tree
    else:
        return json_loads(response.text)


def advanced_name(url):
    entries = get_html(url).xpath('//tr')
    for entry in entries:
        ip_address = entry.getchildren()[1].text_content()
        print(ip_address)


def didsoft(url, output_file):
    entries = get_html(url).xpath('//tr')
    with open(output_file, "a+") as file:
        for entry in entries:
            ip_address = entry.getchildren()[0].text_content()
            port = entry.getchildren()[1].text_content()
            if is_ip_address(ip_address):
                file.write(f'{ip_address}:{port}\n')


def geonode(url, output_file):
    entries = get_html(url, 'json')
    with open(output_file, "a+") as file:
        for entry in entries['data']:
            ip_address = entry['ip']
            port = entry['port']
            file.write(f'{ip_address}:{port}\n')


def free_proxy_cz(url, output_file):
    entries = get_html(url).xpath('//tr')
    with open(output_file, "a+") as file:
        for entry in entries:
            encoded_string = entry.text_content()
            if 'document.write(Base64.decode' in encoded_string:
                ip_data = re_search(
                    r'decode\(\"([a-zA-Z0-9\=]+)\"\)\)(\d+)', encoded_string)
                ip_address = b64decode(ip_data.group(1)).decode('utf-8')
                port = ip_data.group(2)
                file.write(f'{ip_address}:{port}\n')


def main():
    pass


if __name__ == '__main__':
    main()
