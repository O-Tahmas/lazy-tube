import os
from googleapiclient.discovery import build

# conventionally setting it to YT_API_KEY but can change that if you want
env_variable_name = "YT_API_KEY"
API_KEY = os.environ[env_variable_name]


def create_youtube_client():
    youtube = build("youtube", "v3", developerKey=API_KEY)
    return youtube


def get_video_details(youtube, video_id):
    video_response = (
        youtube.videos().list(part="id,snippet,contentDetails", id=video_id).execute()
    )

    if "items" in video_response and len(video_response["items"]) > 0:
        video = video_response["items"][0]
        return video
    else:
        return None

if __name__ == "__main__":
    'https://www.youtube.com/watch?v=pOaQ4IZ6y00&ab_channel=PatrickBoyle'
    youtube = create_youtube_client()
    video = get_video_details(youtube, 'LMsiWvUc9bI')
    print(video)
