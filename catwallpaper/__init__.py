import os
import random
import re
import urllib
import requests
from platform import system

def main():
# Strings for wallpapers
	COLLECTION_STRING = [
		"cool-cat-wallpaper",
		"1920x1080-cat-wallpaper",
		"cat-wallpapers-and-screensavers",
		"baby-cat-wallpaper",
		"funny-cat-desktop-wallpaper",
	]


# Setting up python scrapping
	rnd = random.randint(0, len(COLLECTION_STRING) - 1)
	pack = COLLECTION_STRING[rnd]
	plist = requests.get("http://getwallpapers.com/collection/" + pack).text
	f = re.compile(r"/\w+/full.+.jpg")
	f = f.findall(plist)
	fy = "http://getwallpapers.com" + random.choice(f)

# Downloading the wallpaper
	r = requests.get(fy, allow_redirects=True)
	open('cybersecbyte.jpg', 'wb').write(r.content)

	uri = "cybersecbyte.jpg"

# If windows
	if system() == "Windows":
		import os
		import ctypes
		uri = "\cybersecbyte.jpg"
		cwd = os.getcwd()
		okk = cwd + uri
		try:
			ctypes.windll.user32.SystemParametersInfoW(20, 0, okk, 0)
		except:
			ctypes.windll.user32.SystemParametersInfoA(20, 0, okk, 0)
		

# If Mac
	elif system() == "Darwin":
		from os import system as s
		s('osascript -e \'tell application "Finder" to set desktop picture to POSIX file "{0}"\''.format(uri))

# If Linux
	elif system() == "Linux":
		import os
		desktop_session = os.environ.get('XDG_CURRENT_DESKTOP') or os.environ.get('DESKTOP_SESSION')

# For gnome
		if desktop_session.startswith('G'):
			cwd = os.getcwd()
			try:
				launchme = "gsettings set org.gnome.desktop.background picture-uri " + cwd + "/" + uri
				os.system(launchme)
			
			except:
				launchmedark = "gsettings set org.gnome.desktop.background picture-uri-dark " + cwd + "/" + uri
				os.system(launchmedark)

# For xfce
		elif desktop_session.startswith('X'):
			print("Support for xfce is coming soon in next updates")

# For mate
		elif desktop_session.startswith('M'):
			cwd = os.getcwd()
			launchmemate = "mateconftool-2 -t string --set " + cwd + "/" + uri
			os.system(launchmemate)

# For kde
		elif desktop_session.startswith('K'):
			print("Support for kde is coming soon in next updates")
