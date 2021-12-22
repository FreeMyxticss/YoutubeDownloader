from pytube import YouTube, Playlist, Channel, Search

mode = int(input("Please select a mode:\n1. Download a URL\n2. Download a playlist\n3. Download a channels videos\n4. Execute search\n> "))

def save(video):
	vid = video.streams.filter(file_extension="mp4").get_by_itag(22)
	with open(f"downloads/{vid.title}_info.txt", 'w') as i:
		i.write(f"Title: {vid.title}\n"
		f"Author: {video.author}\n"
		f"Channel URL: {video.channel_url}\n"
		f"Views: {video.views}\n"
		f"Publish Date: {video.publish_date}\n"
		f"Video Rating: {video.rating}\n"
		f"Description: {video.description}\n"
		f"Length: {video.length}\n"
		f"Thumbnail URL: {video.thumbnail_url}")
		i.close()
	vid.download(filename=vid.title + ".mp4", output_path="downloads")
def mp3(video):
	vid = video.streams.filter(file_extension="mp4").get_audio_only()
	with open(f"downloads/{vid.title}_info.txt", 'w') as i:
		i.write(f"Title: {vid.title}\n"
		f"Author: {video.author}\n"
		f"Channel URL: {video.channel_url}\n"
		f"Views: {video.views}\n"
		f"Publish Date: {video.publish_date}\n"
		f"Video Rating: {video.rating}\n"
		f"Description: {video.description}\n"
		f"Length: {video.length}\n"
		f"Thumbnail URL: {video.thumbnail_url}")
		i.close()
	vid.download(filename=vid.title + ".mp3", output_path="downloads")

if mode == 1:
	URL = input("Please enter a URL\n> ")
	video = YouTube(URL)
	sm = int(input("Please choose one of the following\n1. MP4\n2. MP3\n> "))
	if sm == 1:
		save(video)
	elif sm == 2:
		mp3(video)
	else:
		print("That isn't an option")
elif mode == 2:
	URL = input("Please enter a URL\n> ")
	playlist = Playlist(URL)
	sm = int(input("Please choose one of the following\n1. MP4\n2. MP3\n> "))
	for video in playlist.videos:
		if sm == 1:
			save(video)
		elif sm == 2:
			mp3(video)
		else:
			print("That isn't an option")
elif mode == 3:
	URL = input("Please enter a URL\n> ")
	channel = Channel(URL)
	sm = int(input("Please choose one of the following\n1. MP4\n2. MP3\n> "))
	for video in channel.videos:
		if sm == 1:
			save(video)
		elif sm == 2:
			mp3(video)
		else:
			print("That isn't an option")
elif mode == 4:
	query = input("Please enter a search query\n> ")
	search = Search(query)
	for i in range(0, len(search.results)):
		print(str(i) + ". " + search.results[i].title + "\n")
	pos = int(input("Select a video\n> "))
	sm = int(input("Please choose one of the following\n1. MP4\n2. MP3\n> "))
	video = search.results[pos]
	if sm == 1:
		save(video)
	elif sm == 2:
		mp3(video)
	else:
		print("That isn't an option")
else:
	print("That isn't an option")
