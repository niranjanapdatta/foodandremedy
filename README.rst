What does this script do?

This python script will fetch the video ID of every single video uploaded to a particular YouTube channel using the YouTube Data API v3.


How does it Work?

1. Create a config.json file(refer the config.json file)

2. Run:
	pip install google-api-python-client

3. Run the script:
	python3 YouTubeApi.py


How do I get my API key?

Visit- https://developers.google.com/youtube/v3/getting-started#before-you-start


How do I get the channel ID?

1. Play any video that belongs to the desired YouTube channel.

2. Click on the channel icon or channel name.

3. You will be redirected to the channel's home page. The URL of that page should look something like this:
	Example-
		URL: https://www.youtube.com/channel/UCR_9gNKW_ucKrHe6gZEv_iw
		
		Copy the part that lies after https://www.youtube.com/channel/
		
		channel ID: UCR_9gNKW_ucKrHe6gZEv_iw


Where can I use the video IDs that are obtained using the script?

The video IDs can be concatenated with "https://www.youtube.com/watch?v=" in order to obtain the video URL. In a similar sense, you can use the video IDs to obtain the thumbnails of a particular video or the details(title, description, viewcount, likes etc.) of the video.


*This code has been flake8 and pylint checked*

This was done as part of App Development for https://swayampaaka.com 
