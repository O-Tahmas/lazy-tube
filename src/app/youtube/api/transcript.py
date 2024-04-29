import validators
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

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
    # Validate if it is a proper URL
    if not validators.url(link):
        raise ValueError("The input is not a valid URL.")

    # Ensure the URL is a YouTube link
    if 'youtube' not in link:
        raise ValueError('Please input a valid YouTube link.')

    # Parse the URL and extract query parameters
    parsed_url = urlparse(link)
    query_params = parse_qs(parsed_url.query)

    # Extract and return the video ID using the 'v' query parameter
    video_id = query_params.get('v')
    if video_id:
        return video_id[0]
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
    # Utilize the youtube_transcript_api package to fetch the transcript
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except YouTubeTranscriptApi.CouldNotRetrieveTranscript as e:
        raise YouTubeTranscriptApi.CouldNotRetrieveTranscript(f"No transcript available for video ID {video_id}: {str(e)}")

