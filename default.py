
import util, urllib2
import xbmc

def playVideo(params):
    response = urllib2.urlopen(params['video'])
    if response and response.getcode() == 200:
        content = response.read()
        videoLink = util.extract(content, 'src=\'" + "', '\"')
        link=videoLink.replace('1000','2500')
        util.playMedia(params['title'], params['image'], link, 'Video')
    else:
        util.showError(ADDON_ID, 'Could not open URL %s to get video information' % (params['video']))

def buildMenu():
    url = WEB_PAGE_BASE + '/livetv'
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        videos = util.extractAll(content, '<a class="channel_link"', '</a>')
        for video in videos:
            params = {'play':1}
            params['video'] = WEB_PAGE_BASE + util.extract(video,'href="','\"')
            params['image'] = util.extract(video,'img src="','\"')
            params['title'] = util.extract(video,'channel="','\"')
            link = util.makeLink(params)
            util.addMenuItem(params['title'], link, 'DefaultVideo.png', params['image'], False)
        xbmc.executebuiltin("Container.SetViewMode(52)")
        util.endListing()
    else:
        util.showError(ADDON_ID, 'Could not open URL %s to create menu' %(url))
'''
def firstRun():
    url = WEB_PAGE_BASE + '/livetv'
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        video = util.extract(content, '<a class="channel_link"', '</a>')
        params = {'play':1}
        params['video'] = WEB_PAGE_BASE + util.extract(video,'href="','\"')
        params['image'] = util.extract(video,'img src="','\"')
        params['title'] = util.extract(video,'channel="','\"')

        util.logAddon(params)
        util.endListing()
        return params

    else:
        util.showError(ADDON_ID, 'Could not open URL %s to create menu' %(url))
'''


WEB_PAGE_BASE = 'http://play.fpt.vn'
ADDON_ID = 'plugin.video.bit.livetv'

parameters = util.parseParameters()
if 'play' in parameters:
    playVideo(parameters)
else:
    buildMenu()
    util.logAddon('BUILDMENU')
    



