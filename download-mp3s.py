import re, urllib

#print 'Enter URL:'
#print 'Usage: "http://www.awebsite.net/some/thing/" (remember double quotes!)'
#myurl = input("@>")
myurl = "http://www.planecrashinfo.com/lastwords.htm"
mydomainz = re.findall('(.+\..+/)', myurl)
mydomain = mydomainz[0]
print "Domain:\n" + mydomain

#for i in re.findall('''href=["'](.[^"']+)(\.mp3)["']''', urllib.urlopen(myurl).read()):
print "Paths:"
for i in re.findall('''href=["'](.[^"']+\.mp3)["']''', urllib.urlopen(myurl).read()):
    filepath = mydomain + i
    print filepath
    filenamez = re.search('([^/]+.mp3)', i)
    filename = filenamez.group(0)
    urllib.urlretrieve(filepath, filename)
