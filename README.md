YouTube Batch Downloader

A Python desktop application that provides a graphical interface for batch-processing video URLs.

Built with Python, Tkinter, and yt-dlp, the application lets users load a text file containing video URLs, choose a destination folder, and process the URLs sequentially.

The application includes a progress bar and an activity log to help users monitor the download process.

Features

* Graphical interface: A simple desktop GUI built with Tkinter.
* Batch processing: Read multiple video URLs from a text file.
* Selectable input: Choose the source .txt file through a file dialog.
* Custom output directory: Choose where downloaded videos are saved.
* Video and audio selection: Request the best available video and audio streams.
* MP4 output: Request MP4 merging when separate video and audio streams are downloaded.
* Progress tracking: Display progress through the URL list.
* Activity logging: Show the URLs being processed and report status messages.
* Background processing: Run downloads in a separate thread.
* Completion notification: Display a message when processing finishes.

Requirements

* Python 3
* yt-dlp
* FFmpeg, when required for merging separate video and audio streams
* Tkinter, which is included with many Python installations but may need to be installed separately on some Linux systems

Installation

1. Clone the repository

Open a terminal and run:

git clone https://github.com/vsroshan/youtube-batch-downloader.git
cd youtube-batch-downloader

Replace YOUR-USERNAME with the GitHub username that owns this repository.

Alternatively, download the repository as a ZIP file from GitHub and extract it.

2. Create a virtual environment

On macOS or Linux:

python3 -m venv .venv
source .venv/bin/activate

On Windows:

py -m venv .venv
.venv\Scripts\activate

3. Install Python dependencies

If the repository includes requirements.txt, run:

python -m pip install -r requirements.txt

The main third-party Python dependency is yt-dlp.

4. Install FFmpeg

FFmpeg may be required when yt-dlp downloads separate video and audio streams that need to be merged.

On macOS, if Homebrew is installed:

brew install ffmpeg

On Windows or Linux, install a compatible FFmpeg build using the instructions for your operating system.

Verify the installation:

ffmpeg -version

Usage

1. Prepare a text file

Create a text file containing one video URL per line.

For example:

https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/watch?v=VIDEO_ID_3

Replace these placeholders with valid URLs for content you are authorized to download.

Blank lines are ignored.

2. Launch the application

Run the main Python file:

python youtube_batch_downloader.py

Replace the filename with the actual name of the Python file you upload.

3. Select the source file

Click Select TXT File and choose your list of video URLs.

4. Select the destination folder

Click Select Destination Folder and choose the directory where you want the downloaded files saved.

5. Start downloading

Click START DOWNLOAD.

The application processes the URLs sequentially and displays progress and status messages.

6. Check the output

When processing finishes, check the selected destination folder for the downloaded videos.

How It Works

The application uses yt-dlp to process each URL.

It requests the best available video and audio streams, falling back to the best available format when necessary. When separate streams are downloaded, yt-dlp may use FFmpeg to merge them into an MP4 container.

The application sets noplaylist=True, so it is configured to process individual video URLs rather than download entire playlists from a playlist URL.

Troubleshooting

The application does not start

* Verify that Python is installed.
* Confirm that Tkinter is available in your Python installation.
* Install the required Python dependencies.
* Check the terminal for error messages.

Video and audio merging fails

* Check whether FFmpeg is installed.
* Verify that FFmpeg is available on your system.
* Review the error messages returned by yt-dlp.

Some downloads fail

* Check your internet connection.
* Verify that the URL is valid and the video is accessible.
* Review the activity log and any diagnostic messages.

The progress bar reaches the end, but some videos are missing

The application enables yt-dlp’s ignoreerrors option. As a result, some download errors may not raise exceptions that the application can report as failures. The displayed success message does not guarantee that every video was downloaded successfully.

Responsible Use

Use this application only for content you own, content you have permission to download, or content that is otherwise lawfully available for downloading.

Respect copyright, applicable laws, and YouTube’s terms and policies. Do not use this application to download copyrighted material without the necessary rights or authorization.

Project Status

This repository contains the initial published version of the project.

Author

Created as a personal Python programming project.
