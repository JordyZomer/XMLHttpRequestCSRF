# XMLHttpRequestCSRF
A script to check if there may be a CSRF vulnerability in XMLHttpRequests on the target site.


#  Requirements

- argparse
- re
- requests


# Usage

Add the desired hosts to a file, for example targets.txt and run the script:

```> python2.7 checkCSRF.py --targets targets.txt```

The target file may look like the following:

```> cat targets.txt
http://example.com
https://domain.net```

# License

I don't give a fuck man, copy, paste, edit as much as you want ;)
