Q. What does this script do?

A. This python script will fetch the video ID of every single video uploaded to a particular YouTube channel using the YouTube Data API v3.


Q. How does it Work?

A. > Create a config.json file(refer the config.json file)

   > Run the script:
     python3 YouTubeApi.py
   
   
Q. How do I get my API key?

A. Visit- https://developers.google.com/youtube/v3/getting-started#before-you-start


Q. How do I get the channel ID?

A. > Play any video that belongs to the desired YouTube channel.
   > Click on the channel icon or channel name.
   > You will be redirected to the channel's home page. The URL of that page should look something like this:
	Example-
		URL: https://www.youtube.com/channel/UCR_9gNKW_ucKrHe6gZEv_iw
		Copy the part that lies after https://www.youtube.com/channel/
		channel ID: UCR_9gNKW_ucKrHe6gZEv_iw


Q. Where can I use the video IDs that are obtained using the script?

A. The video IDs can be concatenated with "https://www.youtube.com/watch?v=" in order to obtain the video URL. In a similar sense, you can use the video IDs to obtain the thumbnails of a particular video or the details(title, description, viewcount, likes etc.) of the video.


*This code has been flake8 and pylint checked*

*** This was done as part of App Development for https://swayampaaka.com **
