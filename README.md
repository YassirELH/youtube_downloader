# YouTube Downloader

YouTube Downloader is a Django-based web application that allows users to download YouTube videos by simply providing a video URL. The application fetches the video and provides a download link for the video in MP4 format.

## Features

- **Easy to Use**: Input a YouTube video URL and download the video with a single click.
- **MP4 Format**: Downloads videos in MP4 format for compatibility with most devices.
- **User-Friendly Interface**: Simple and intuitive web interface.

## Installation

### Prerequisites

- Python 3.11
- Django
- Git

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YassirELH/youtube_downloader.git
   cd youtube_downloader
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv youtube_env
   youtube_env\Scripts\activate
   ```

3. **Install the Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Django Development Server**
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:8000` to start using the application.

## Usage

1. **Enter URL**: On the home page, enter the URL of the YouTube video you want to download.
2. **Download Video**: Click the download button to fetch and download the video. The video will be downloaded in MP4 format.

## Project Structure

```
youtube_downloader/
│
└── youtube_downloader/
    ├── downloaded_videos/       # Directory for storing downloaded videos
    ├── videos/                  # Django application directory
    │   ├── __pycache__/
    │   ├── migrations/          # Database migrations
    │   ├── templates/           # HTML templates
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── youtube_downloader/      # Main Django project directory
    │   ├── __pycache__/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3               # SQLite database file
    └── manage.py                # Django management script
├── youtube_env/            # Virtual environment
├── requirements.txt        # Python dependencies
└── README.md               # Project README



```

## Dependencies

- **Django**: The web framework used for the project.
- **pytube**: A lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.


## Known Issues

### Cipher Issue in `pytube`

There is a known issue with the cipher file in the `pytube` library. This can cause errors when attempting to download videos. The `pytube` maintainers are aware of this and are working on a fix. In the meantime, a workaround is to manually patch the cipher file.

To manually patch the cipher file, locate the `cipher.py` file in your `pytube` installation and apply the necessary changes as described in the `pytube` GitHub issues section [https://github.com/pytube/pytube/issues/1954](regex issue) .

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
