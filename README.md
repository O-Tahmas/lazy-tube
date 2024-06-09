# YouTube Video Summarizer and Q&A Assistant

This project is a Python-based tool that fetches the transcript from a YouTube video, summarizes it using the Gemini API, and allows users to ask follow-up questions about the video transcript.


## Features
- Transcribes a video from a given YouTube video URL.
- Summarizes the transcript using the Gemini API.
- Allows users to ask follow-up questions about the video transcript.


## Prerequisites

- Python >=3.11

Before running this script, ensure you have completed the following setup steps:
1. **Create a Google Cloud project**
2. **Enable the Vertex AI API** in your Google Cloud project.
    You can find detailed instructions on how to set up Vertex AI [here:](https://cloud.google.com/vertex-ai/docs/featurestore/setup)


## Installation

1. Clone the repository: 

    ```bash
    git clone https://github.com/yourusername/youtube-video-summarizer.git
    cd youtube-video-summarizer
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```


## Usage

This is designed to run entirely from the terminal:
```bash
python main.py <YouTube URL> <Project Name> <Location> <Model Choice>
```

### Arguments
- `<YouTube URL>`: The full URL of the YouTube video.
- `<Project Name>`: The name of your Google Cloud project.
- `<Location>`: The location of your Vertex AI resources.
- `<Model Choice>`: The model to use for generating content.

After summarizing the transcript, you can ask follow-up questions about the video by typing them in the prompt. To exit the question loop, type `exit`.


## Project Structure
- `main.py`: The main script that integrates all functionalities.
- `get_transcript.py`: Contains functions to extract the transcript from a YouTube video.
- `gemini_api.py`: Contains functions to interact with the Gemini API for summarization and Q&A.


## Contributing

This is of course extremely scalable, contributions are welcome! Please feel free to submit a Pull Request.


## License

This project is licensed under the MIT License.