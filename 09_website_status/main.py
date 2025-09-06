import time
import requests
from dataclasses import dataclass, field
from typing import Dict, Optional



@dataclass
class WebsiteStatus:
    url: str
    status_code: Optional[int] = None
    reason: Optional[str] = None
    load_time_seconds: Optional[float] = None
    content_type: Optional[str] = None
    encoding: Optional[str] = None
    headers: Dict[str, str] = field(default_factory=dict)
    error: Optional[str] = None


def normalise_url(url: str) -> str:
    return url if url.startswith(('http://', 'https://')) else f'https://{url}'


def check_website(url: str, timeout: int = 10) -> WebsiteStatus:
    url = normalise_url(url)
    start = time.perf_counter()
    status = WebsiteStatus(url=url)  # default values already set

    try:
        response = requests.get(url, timeout=timeout)
        status.load_time_seconds = time.perf_counter() - start
        status.status_code = response.status_code
        status.reason = response.reason
        status.content_type = response.headers.get('Content-Type', '')
        status.encoding = response.encoding
        status.headers = dict(response.headers)

    except requests.RequestException as exc:
        status.load_time_seconds = time.perf_counter() - start
        status.error = str(exc)

    return status


def display_status(ws: WebsiteStatus) -> None:
    print(f'\n=== Website diagnostics for {ws.url} ===')

    # Failure path
    if ws.error:
        print(f'ERROR        : {ws.error}')
        if ws.load_time_seconds is not None:
            print(f'Elapsed       : {ws.load_time_seconds:.3f}s')
        return

    # Success path
    print(f'Status code  : {ws.status_code} ({ws.reason})')
    print(f'Load time    : {ws.load_time_seconds:.3f}s')
    print(f'Content-Type : {ws.content_type}')
    print(f'Encoding     : {ws.encoding or "n/a"}')
    print('Headers      :')
    for key, value in ws.headers.items():
        print(f'  • {key}: {value}')


if __name__ == '__main__':
    website: WebsiteStatus = check_website('indently.io')
    display_status(website)
