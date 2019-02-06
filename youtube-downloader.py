from __future__ import unicode_literals
import youtube_dl


'''
Each line should consist of a title and url starting with http...
ie songname http://www.youtube.com/?watch=whatever
   songname2 http....
or just urls without titles.  It'll grab the titles from their respective videos of origin

Currently, it just ignores your title and takes the youtube video title.
'''
fname = 'path-to-your-txt-file'

#youtube_dl settings

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def separate(line):
	#this separates the url and the identifying information, which will be used as the file title
	#returns title, url
	#if there is no title, it will still return the url along with a blank string as the title

	title, url = line.split('http')
	try:
		return title, 'http' + url
	except:
		try:
			return '', 'http' + url
		except:
			print('file line is not formatted correctly:' + line)

def download_this_list(list):
	#takes a list of titles and urls or just urls
	#downloads all videos and extracts mp3's

	for x in content:
		title, url = separate(x)
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		    ydl.download([url]) 

#grabbing the file... (which should consist of titles + the video url or just the urls of each video, one url per line
with open(fname) as f:
	content = f.readlines()

content = [x.strip() for x in content] 

download_this_list(content)
