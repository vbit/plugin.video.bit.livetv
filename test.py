
import util, urllib2

def playVideo(params):
    response = urllib2.urlopen(params['video'])
    if response and response.getcode() == 200:
        content = response.read()
        videoLink = util.extract(content, 'src=\'" + "', '\"')
        print videoLink

    else:
        util.showError(ADDON_ID, 'Could not open URL %s to get video information' % (params['video']))

def buildMenu():
    url = WEB_PAGE_BASE + '/livetv'
    response = urllib2.urlopen(url)
    if response and response.getcode() == 200:
        content = response.read()
        video = util.extract(content, '<a class="channel_link"', '</a>')
        params = {'play':1}
        params['video'] = WEB_PAGE_BASE + util.extract(video,'href="','\"')
        params['image'] = util.extract(video,'img src="','\"')
        params['title'] = util.extract(video,'channel="','\"')
        link = util.makeLink(params)
        util.addMenuItem(params['title'], link, 'DefaultVideo.png', params['image'], False)

    else:
        util.showError(ADDON_ID, 'Could not open URL %s to create menu' %(url))

WEB_PAGE_BASE = 'http://play.fpt.vn'
ADDON_ID = 'plugin.video.fptplay'

parameters = util.parseParameters()
if 'play' in parameters:
    playVideo(parameters)
else:
    buildMenu()

