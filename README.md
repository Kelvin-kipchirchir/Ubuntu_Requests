Custom Image Fetcher
This project is a Python-based image downloader that fetches images from user-provided URLs and saves them locally.
It demonstrates web requests, file handling, and error handling in Python.
The script includes:
            Support for downloading multiple URLs at once.
            File size restrictions (max 5MB).
            Duplicate image detection using MD5 hashing.
            URL validation and error handling.
            Automatic folder creation for storing images.

📂 Project Structure
Ubuntu_Requests/
│── ubuntu_images/     # Folder where images are saved (auto-created)
│── fetcher.py         # Main Python script
│── README.md          # Documentation

🚀 Features
✅ Download multiple images in one go (comma/space-separated URLs).
✅ Skip duplicates using file content hash comparison.
✅ Restrict downloads to images only (Content-Type check).
✅ Prevent downloads larger than 5MB.
✅ Handle common issues: invalid URLs, timeouts, and connection errors.

🔧 Requirements
Python 3.7+
Requests library

📸 Example Run
Welcome to the Ubuntu Image Fetcher program
Enter image URLs below to save them locally.
Paste image URLs (comma or space separated): 
https://example.com/cat.jpg, https://example.com/dog.png
Starting download for 2 image(s)...
Successfully fetched: cat.jpg
Image saved to ubuntu_images/cat.jpg
Successfully fetched: dog.png
Image saved to ubuntu_images/dog.png
All done! Images are saved in the 'ubuntu_images' folder
