# Example 1: Download and Save a File Asynchronously

import aiohttp
import aiofiles
import asyncio

async def download_and_save(url, filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"Downloading: {url}")
            if response.status == 200:
                content = await response.read()
                async with aiofiles.open(filename, 'wb') as f:
                    await f.write(content)
                    print(f"Saved to: {filename}")
            else:
                print(f"Failed to download: {url}, Status: {response.status}")

async def main():
    urls = [
        ("https://www.example.com", "example.html"),
        ("https://httpbin.org/image/png", "image.png")
    ]
    tasks = [download_and_save(url, fname) for url, fname in urls]
    await asyncio.gather(*tasks)

asyncio.run(main())

# ✅ Example 2: Read File and Post Content to API

import aiohttp
import aiofiles
import asyncio

async def read_and_post(file_path, post_url):
    async with aiofiles.open(file_path, mode='r') as f:
        content = await f.read()

    async with aiohttp.ClientSession() as session:
        async with session.post(post_url, data={"file_content": content}) as response:
            resp = await response.text()
            print(f"Posted file content. Server responded with: {resp}")

async def main():
    await read_and_post("example.txt", "https://httpbin.org/post")

asyncio.run(main())

# ✅ Example 3: Scrape Multiple URLs and Write Their Titles to a File

from bs4 import BeautifulSoup
import aiohttp
import aiofiles
import asyncio

async def fetch_title(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        return url, soup.title.string if soup.title else "No Title"

async def scrape_and_log(urls, output_file):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_title(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

        async with aiofiles.open(output_file, 'w') as f:
            for url, title in results:
                await f.write(f"{url} => {title}\n")

async def main():
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://httpbin.org"
    ]
    await scrape_and_log(urls, "titles.txt")

asyncio.run(main())