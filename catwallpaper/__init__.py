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
		"cat-background-wallpaper",
		"baby-kitten-wallpapers",
		"hd-cat-wallpapers",
		"hd-cat-wallpapers-1920x1080",
		"wallpaper-cats-and-kittens",
		
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
			cwd = os.getcwd()
			launchmexfce = "xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/imagepath -s " + uri
			os.system(launchmexfce)

# For mate
		elif desktop_session.startswith('M'):
			cwd = os.getcwd()
			launchmemate = "mateconftool-2 -t string --set " + cwd + "/" + uri
			os.system(launchmemate)

# For kde
		elif desktop_session.startswith('K'):
			cwd = os.getcwd()
			image_path = cwd + "/" + uri
			command = (
				f'dbus-send --session --dest=org.kde.plasmashell ' \
				f'--type=method_call /PlasmaShell org.kde.PlasmaShell.evaluateScript ' \
				f'string:"var allDesktops = desktops();' \
				f'print (allDesktops);for (i=0;i<allDesktops.length;i++)' \
				f'{{d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";' \
				f'd.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");' \
				f'd.writeConfig(\"Image\", \"file://{image_path}\")}}"'
			)
# The end xD
