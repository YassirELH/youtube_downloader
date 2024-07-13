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
├── youtube_env/            # Virtual environment
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── README.md               # Project README
└── my_app/                 # Django application directory
    ├── migrations/         # Database migrations
    ├── static/             # Static files (CSS, JS, images)
    ├── templates/          # HTML templates
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

## Dependencies

- **Django**: The web framework used for the project.
- **pytube**: A lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
