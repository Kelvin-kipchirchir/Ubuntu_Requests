
# Week 6 Python Assignment: Custom Image Fetcher
# This script fetches images from provided URLs and saves them locally web requests and file handling in Python.

import requests
import os
from urllib.parse import urlparse
import uuid
import hashlib


# Directory for images storage
MY_IMAGE_DIR = "ubuntu_images"
os.makedirs(MY_IMAGE_DIR, exist_ok=True)

# Store downloaded file hashes to compare and prevent duplicates
my_downloaded_hashes = set()


# My custom function to fetch and save images
def fetch_image(url):
    try:
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # filter image content
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"sorry this is not a valid image: {url}")
            return

        # filter file size to 5MB
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > 5_000_000:
            print(f"sorry this image is too large, required less than 5MB: {url}")
            return

        # Create a filename
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or "." not in filename:
            ext = content_type.split("/")[-1] or "jpg"
            filename = f"ubuntu_{uuid.uuid4().hex[:8]}.{ext}"

        filepath = os.path.join(MY_IMAGE_DIR, filename)

        # Checking for duplicates
        content = response.content
        file_hash = hashlib.md5(content).hexdigest()
        if file_hash in my_downloaded_hashes:
            print(f" Duplicates skipped: {filename}")
            return
        my_downloaded_hashes.add(file_hash)

        # Save the image
        with open(filepath, 'wb') as f:
            f.write(content)

        print(f"Successfully fetched: {filename}")
        print(f"Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.") 

    except requests.exceptions.MissingSchema:
        print(f"Invalid URL format: {url}")
    except requests.exceptions.Timeout:
        print(f"Timeout: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Connection error for {url}: {e}")
    except Exception as e:
        print(f"Unexpected error for {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher program")
    print("Enter image URLs below to save them locally.\n")

    # Accept multiple URLs from user
    urls = input("Paste image URLs (comma or space separated): ")
    urls = [u.strip() for u in urls.replace(",", " ").split() if u.strip()]

    print(f"\nStarting download for {len(urls)} image(s)...\n")

    for url in urls:
        fetch_image(url)

    print("\nAll done! Images are saved in the 'ubuntu_images' folder.")


if __name__ == "__main__":
    main()
