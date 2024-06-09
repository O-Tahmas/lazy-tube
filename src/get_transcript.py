import validators
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi, CouldNotRetrieveTranscript

def get_video_id_from_link(link):
    """
    Extracts the video ID from a YouTube URL.

    Args:
        link (str): The full URL of the YouTube video.

    Returns:
        str: The extracted video ID, or None if no valid ID is found.

    Raises:
        ValueError: If the URL is not valid or it's not a YouTube URL.
    """
    if not validators.url(link):
        raise ValueError("The input is not a valid URL.")

    if 'youtube' not in link and 'youtu.be' not in link:
        raise ValueError('Please input a valid YouTube link.')

    parsed_url = urlparse(link)
    query_params = parse_qs(parsed_url.query)

    video_id = query_params.get('v')
    if video_id:
        return video_id[0]
    elif 'youtu.be' in parsed_url.hostname:
        return parsed_url.path.lstrip('/')
    return None

def get_captions(link):
    """
    Retrieves the captions for a YouTube video using its URL.

    Args:
        link (str): The full URL of the YouTube video.

    Returns:
        list of dicts: A list containing the captions of the video. Each entry in the list is a dictionary representing a single caption.

    Raises:
        ValueError: If the video URL is not valid or does not point to a YouTube video.
        YouTubeTranscriptApi.CouldNotRetrieveTranscript: If no transcript is available for the video or an error occurs in the API.
    """
    video_id = get_video_id_from_link(link)
    if not video_id:
        raise ValueError("Unable to extract video ID from the provided link.")
    
    try:
        return YouTubeTranscriptApi.get_transcript(video_id)
    except CouldNotRetrieveTranscript as e:
        raise CouldNotRetrieveTranscript(f"No transcript available for video ID {video_id}: {str(e)}")

# Temporary - test in main block
if __name__ == "__main__":
    try:
        link = 'https://www.youtube.com/watch?v=synJZAtH58E&ab_channel=JomaTech'
        txt = get_captions(link)
        print(txt)
    except Exception as e:
        print(f"Error: {e}")
