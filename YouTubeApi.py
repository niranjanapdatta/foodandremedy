""" This python code will fetch the video ID of every single video uploaded
to a particular YouTube channel using the YouTube Data API v3 """
# pylint: disable=E1101
from base64 import standard_b64decode
from json import load
from googleapiclient.discovery import build

MAX_RESULT = 50


class YouTubeApi:
    """ fetch and print the video ID of every single video uploaded to a
    particular YouTube channel """
    def __init__(self, api_service_name, api_version, api_key, channel_id):
        self.api_service_name = api_service_name
        self.api_version = api_version
        self.api_key = api_key
        self.channel_id = channel_id
        self.youtube = build(self.api_service_name, self.api_version,
                             developerKey=self.api_key)
        self.video_ids = []

    def get_video_ids(self):
        """ Get all the video IDs for the given channel """
        channel_details = self.youtube.channels().list(part="contentDetails",
                                                       id=self.channel_id). \
            execute()

        playlist_id = \
            channel_details['items'][0]['contentDetails']['relatedPlaylists'][
                'uploads']

        next_page = None

        while True:
            response = self.youtube.playlistItems().list(
                playlistId=playlist_id,
                part="snippet",
                maxResults=MAX_RESULT,
                pageToken=next_page). \
                execute()
            items_list = response.get('items', None)

            if items_list is None:
                break

            for item in items_list:
                item_id = standard_b64decode(item['id']).decode('utf-8')
                # To split playlist ID and Video ID
                _playlist_id, video_id = item_id.split('.')
                self.video_ids.append(video_id)

            next_page = response.get('nextPageToken')

            if next_page is None:
                break

    def print_video_ids(self):
        """ Print all the video IDs for the given channel """
        for video_id in self.video_ids:
            print(video_id)

    def map_to_video_urls(self):
        """ Print Video URLs of all the videos belonging to the given
        channel"""
        for video_id in self.video_ids:
            print("https://www.youtube.com/watch?v="+video_id)


if __name__ == "__main__":
    with open('config.json', 'r') as f:
        config_dict = load(f)

    _api_service_name = config_dict['api_service_name']
    _api_version = config_dict['api_version']
    _api_key = config_dict['api_key']
    _channel_id = config_dict['channel_id']

    youtube = YouTubeApi(_api_service_name, _api_version, _api_key,
                         _channel_id)
    youtube.get_video_ids()
    youtube.print_video_ids()
    youtube.map_to_video_urls()
