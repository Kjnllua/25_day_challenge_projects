import asyncio
from asyncio import TimeoutError
import requests
from requests import Response
from dataclasses import dataclass


# 1. Model the data
@dataclass
class WebsiteResponse:
    url: str
    status: int | None
    reason: str


# 2. Check an individual website
async def check_website(url: str) -> WebsiteResponse:
    if not url.startswith(('http://', 'https://')):
        url = f'https://{url}'

    # Will raise a Timeout Error:
    # if url == 'https://www.fail-website.com':
    #     await asyncio.sleep(10)

    try:
        # This is a simple trick we can use to convert something blocking
        response: Response = await asyncio.to_thread(requests.get, url)
        return WebsiteResponse(url, response.status_code, response.reason)
    except Exception as e:
        return WebsiteResponse(url, None, str(e))


# 3. Check multiple websites
async def check_websites(urls: list[str], timeout: float = 5) -> None:
    tasks = [check_website(url) for url in urls]

    # Gives us back websites in real time
    # If it takes longer than 5 seconds an exception is raised
    try:
        for completed_task in asyncio.as_completed(tasks, timeout=timeout):
            response: WebsiteResponse = await completed_task

            if response.status is not None:
                print(
                    f'{response.url}: ✅ ONLINE ({response.status} {response.reason})'
                )
            else:
                print(f'Could not retrieve information for: "{response.url}"')
                # Include response.reason for more information
    except TimeoutError:
        print('Timeout reached — some websites took too long.')


async def main() -> None:
    urls: list[str] = [
        'www.indently.io',
        'www.apple.com',
        'www.facebook.com',
        'nonexistent-website-404.com',
        'www.instagram.com',
        'www.reddit.com',
        'www.wikipedia.org',
        'www.fail-website.com',
        'www.amazon.com',
        'www.linkedin.com',
        'www.microsoft.com',
        'www.github.com',
    ]

    print(f'Checking {len(urls)} websites...')
    await check_websites(urls)
    print('Done!')


if __name__ == '__main__':
    asyncio.run(main())

# Homework:
# 1. Add response time for each website.
# 2. When a website takes too long to respond, display which website
# too long as a part of the listed websites.
