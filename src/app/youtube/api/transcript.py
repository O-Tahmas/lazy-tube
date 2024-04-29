import requests
import validators
from urllib.parse import urlparse, parse_qs
from youtube_api import create_youtube_client, get_video_details
from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id_from_link(link):
    # Validate if it is a proper URL
    if not validators.url(link):
        raise ValueError("The input is not a valid URL.")

    # Escape if the YT link isn't actually a YT link
    if 'youtube' not in link:
        raise ValueError('Please input a valid YouTube link.')

    # Parse the URL and query parameters
    parsed_url = urlparse(link)
    query_params = parse_qs(parsed_url.query)

    # Extract the video ID using the 'v' query parameter
    video_id = query_params.get('v')
    if video_id:
        return video_id[0]
    return None


def get_captions(youtube, video_id):
    # First, check for available captions
    captions_list = youtube.captions().list(part='id', videoId=video_id).execute()
    if captions_list['items']:
        # Assuming you want the first available caption
        caption_id = captions_list['items'][0]['id']
        # Downloading the caption
        caption_download = youtube.captions().download(id=caption_id).execute()
        return caption_download
    else:
        print("No captions found.")
        return None




if __name__ == '__main__':
    test_link = 'https://www.youtube.com/watch?v=Xg9ihH15Uto&ab_channel=Fireship'
    test_id = 'Xg9ihH15Uto'
    print(YouTubeTranscriptApi.get_transcript(test_id))