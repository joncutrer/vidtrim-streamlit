# Video Trimming Streamlit App

This project is a simple yet powerful web application for trimming videos, built with Streamlit. It utilizes `ffmpeg` for backend video processing, providing a user-friendly interface to select start and end times for trimming.

## Features

- **File Upload**: Users can upload video files in MP4 format.
- **Video Trimming**: Users can specify the start and end times for trimming using a simple input format.
- **Download**: Users can download the trimmed video directly from the app.

## Prerequisites

Before you can run this project, you need to have the following installed:
- Python 3.6 or higher
- `ffmpeg` (This needs to be installed on your system and accessible in your PATH)

## Installation

To set up this project locally, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/vidtrim-streamlit.git
   cd vidtrim-streamlit
   ```


2. Set Up a Virtual Environment (Optional but recommended)

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Running the Application

To run the application, use the following command:

```bash
streamlit run vidtrim_streamlit/streamlit_app.py
```

Open your web browser and go to http://localhost:8501 to see the app in action.

### Configuring Upload File Size

By default, Streamlit limits the size of uploaded files. If you need to upload larger video files, you can increase this limit by setting the --server.maxUploadSize flag. For example, to increase the upload limit to 200MB, you can start your application as follows:

```bash
streamlit run vidtrim_streamlit/streamlit_app.py --server.maxUploadSize=200
```

Adjust the 200 to the limit that you require, measured in megabytes (MB). This setting is crucial for ensuring that users can upload video files large enough for practical video trimming tasks.

## Deployment
This app is ready for deployment on Streamlit Sharing. Ensure you have added all necessary files and configurations to your GitHub repository before deploying.

## Contributing
Contributions to this project are welcome! Here's how you can contribute:

## Fork the repository
Create a new branch for your feature (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a pull request

## License
Distributed under the MIT License. See LICENSE for more information.