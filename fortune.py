#Author: Pablo Moles
#Read the README file for more info

import urllib2
import random
import re

##### Complete with your path #####
f = open("%PATH_TO_TAGS%/tags","r")
###################################
i = 0
######## Number of tags ###########
'''If you want to add tags, edit the text file called 'tags'. Make sure that are allowed in www.quotesdaddy.com or you are going to get an error. Remember to update the maximum value of the randint function.'''
limit = random.randint(0,35)
##################################
for line in f:
	if i == limit:
		web = urllib2.urlopen("http://www.quotesdaddy.com/widget/tag/"+line[:-1]+"#")
		content = web.read()
		print "\033[93m\'"+ re.findall('&ldquo;(.*?)&rdquo', content)[0]+ "\'\n-", (re.findall('<p>by: <a target="_top"(.*?)</a>', content)[0]).split('>')[-1]+"\033[0m\n"
		break
	else:
		i+=1
