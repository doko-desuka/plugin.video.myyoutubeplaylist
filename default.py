# -*- coding: utf-8 -*-
import sys

import xbmcgui
import xbmcaddon
import xbmcplugin


# 1) The most important part. Within the single quotes below, paste only the ID of the YouTube playlist:
# ----------------------------------------------------------------------
myPlaylistID = 'PLIGsMJ42bg3wKypP4M8YWNMi5Hyr4r3Gq'
# ----------------------------------------------------------------------
# The ID is obtained from the full address while watching it. Example:
# https://www.youtube.com/watch?v=ZmKy4WbFasM&list=PLIGsMJ42bg3wKypP4M8YWNMi5Hyr4r3Gq
# See the "&list=blablabla"? The 'blablabla' part is the playlist ID.

# 2) (Optional) Change the name inside the single quotes below if you want, it's the item's label:
listItem = xbmcgui.ListItem('My YouTube Playlist')

# 3) (Optional) The item's thumbnail image. The default is to use the same as the add-on's icon:
myThumbnail = xbmcaddon.Addon().getAddonInfo('icon')
# You can replace the icon.png image (found in the add-on folder) with any other image, just make
# sure it has the exact same name and it's also in PNG format, so you can overwrite the default one.

# All done! No more changes needed from here. Pack the add-on folder into a zip and install in Kodi.
# --------------------------------------------------
listItem.setArt({'thumb': myThumbnail, 'poster': myThumbnail, 'fanart': myThumbnail})
url = r'plugin://plugin.video.youtube/playlist/%s/' % myPlaylistID
xbmcplugin.addDirectoryItem(int(sys.argv[1]), url, listItem, isFolder=True)
xbmcplugin.endOfDirectory(int(sys.argv[1]))