import validators
from urllib.parse import urlparse, parse_qs
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


def get_captions(link):
    video_id = get_video_id_from_link(link)
    # Utilizing the `youtube_transcript_api` package
    return YouTubeTranscriptApi.get_transcript(video_id)



if __name__ == '__main__':
    test_link = 'https://www.youtube.com/watch?v=Xg9ihH15Uto&ab_channel=Fireship'
    test_id = 'Xg9ihH15Uto'
    print(get_captions(test_link))