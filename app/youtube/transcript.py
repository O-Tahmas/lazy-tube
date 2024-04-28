import requests
from app.youtube.youtube_api import create_youtube_client, get_video_details

def get_video_id_from_link(link):
    # Extract the video ID from the YouTube video link
    video_id = link.split('v=')[1]
    return video_id

def get_video_transcript(video_id):
    youtube = create_youtube_client()
    video = get_video_details(youtube, video_id)

    if video:
        if 'contentDetails' in video and 'caption' in video['contentDetails']:
            caption_url = video['contentDetails']['caption']['url']
            response = requests.get(caption_url)
            
            if response.status_code == 200:
                transcript_data = response.text
                return transcript_data
            else:
                print(f'Failed to retrieve transcript. Status code: {response.status_code}')
        else:
            print('No captions available for this video.')
    else:
        print('Video not found.')

    return None

def get_transcript_from_link(link):
    video_id = get_video_id_from_link(link)
    transcript = get_video_transcript(video_id)
    return transcript