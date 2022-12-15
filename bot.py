import typer
from services import free_proxy_cz, geonode, didsoft


def main(output_file: str):
    iterations = []

    # free_proxy_cz
    for page in [1, 2, 3, 4, 5]:
        iterations.append({
            'site': 'free_proxy_cz',
            'url': f'http://free-proxy.cz/en/proxylist/main/{page}'
        })

    # geonode
    iterations.append({
        'site': 'geonode',
        'url': 'https://proxylist.geonode.com/api/proxy-list?limit= \
        200&page=1&sort_by=lastChecked&sort_type=desc'
    })

    # didsoft
    softdid_items = [{
        'site': 'didsoft',
        'url': 'https://www.socks-proxy.net/'
    }, {
        'site': 'didsoft',
        'url': 'https://free-proxy-list.net/'
    }, {
        'site': 'didsoft',
        'url': 'https://www.us-proxy.org/'
    }, {
        'site': 'didsoft',
        'url': 'https://free-proxy-list.net/uk-proxy.html'
    }, {
        'site': 'didsoft',
        'url': 'https://www.sslproxies.org/'
    }, {
        'site': 'didsoft',
        'url': 'https://free-proxy-list.net/anonymous-proxy.html'
    }]
    for softdid in softdid_items:
        iterations.append(softdid)

    typer.echo('Saving proxies...')
    with typer.progressbar(iterations) as progress:
        for item in progress:
            if item['site'] == 'free_proxy_cz':
                free_proxy_cz(item['url'], output_file)
            if item['site'] == 'geonode':
                geonode(item['url'], output_file)
            if item['site'] == 'didsoft':
                didsoft(item['url'], output_file)
    typer.echo("Done!")


if __name__ == "__main__":
    typer.run(main)
