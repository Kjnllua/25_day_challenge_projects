import asyncio
import requests
from dataclasses import dataclass


# 1. Model the data
@dataclass
class Response:
    url: str
    status: int | None
    reason: str


# 2. Check an individual website
async def check_website(url: str) -> Response:
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'

    try:
        response = await asyncio.to_thread(requests.get, url)
        return Response(url, response.status_code, response.reason)
    except Exception as e:
        return Response(url, None, str(e))


# 3. Check multiple websites
async def check_websites(urls: list[str], timeout: float = 5) -> None:
    tasks = [check_website(url) for url in urls]

    # Gives us back websites in real time
    # If it takes longer than 5 seconds an exception is raised
    for completed_task in asyncio.as_completed(tasks, timeout=timeout):
        response: Response = await completed_task

        if response.status is not None:
            print(f'{response.url}: ✅ ONLINE ({response.status} {response.reason})')
        else:
            print(f'{response.url}: ❌ OFFLINE ({response.reason})')


async def main() -> None:
    urls: list[str] = [
        'www.indently.io',
        'www.apple.com',
        'www.facebook.com',
        'nonexistent-website-404.com',
        'www.instagram.com',
        'www.reddit.com',
        'www.wikipedia.org',
        'www.amazon.com',
        'www.linkedin.com',
        'www.microsoft.com',
        'www.github.com'
    ]

    print(f'Checking {len(urls)} websites...')
    await check_websites(urls)


if __name__ == '__main__':
    asyncio.run(main())

# Homework:
# 1. Add response time for each website.
# 2. Handle the exception that is raised when the timeout is reached.
