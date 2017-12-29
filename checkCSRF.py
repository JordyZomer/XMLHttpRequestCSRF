# Import dependencies
import requests
import argparse
import re

# Parse user iput
parser = argparse.ArgumentParser(description='XHR CSRF checking tool by Jordy Zomer')
parser.add_argument('--targets', type=str, help='A file that contains the targets')
args = parser.parse_args()

# Open target file
targets = open(args.targets, 'r').readlines()

# If there's a XHR POST request and the cookies are sent too it might be a CSRF 
def checkCSRF(script, resp, targ):
    if re.match(r'xhr.open\(\"POST\"\, \"(http|https):\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)\"\, false\)\;', resp) and re.match(r'xhr\.withCredentials=true;'):
        print "Found possible CSRF vulnerability in [%s] at [%s]" % (targ, script)

# For every target in your file do        
for target in targets:
    target = target.rstrip()

    # Make a request to the target 
    response = requests.get(target).text

    # Is it a javascript file?
    javascript = re.findall(r'src="([^"]+\.js)?"',response) 

    # For every javascript file do
    for script in javascript:

        newTarget = target + script

        if re.match(r'(http|https)\:\/\/',script):
            newTarget = script
        # Make a request to the script
        newResponse = requests.get(newTarget).text
        
        # Check script for regex
        checkCSRF(newTarget, newResponse, target)
