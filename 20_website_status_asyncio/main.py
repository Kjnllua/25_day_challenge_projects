import asyncio
import requests

async def check_status(url):
    try:
        resp = await asyncio.to_thread(requests.get, url, timeout=3)
        return url, resp.status_code, resp.reason
    except Exception as e:
        return url, None, str(e)

async def main(urls):
    tasks = [check_status(url) for url in urls]
    for future in asyncio.as_completed(tasks):
        url, status, reason = await future
        if status:
            print(f"{url}: ONLINE ({status} {reason})")
        else:
            print(f"{url}: OFFLINE ({reason})")

if __name__ == "__main__":
    raw_urls = ['www.indently.io', 'www.apple.com', 'www.facebook.com']
    urls = [url if url.startswith("http") else "http://" + url for url in raw_urls]
    asyncio.run(main(urls))
