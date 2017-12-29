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
https://domain.net
```

# Todo

- Check CORS E.G.

``` 
Access-Control-Allow-Origin: *Access-Control-Allow-Origin: *
```
Ref: https://en.wikipedia.org/wiki/Same-origin_policy
Note: Just because the request isn't read by the browser doesn't mean the request has not been made.

Even though the browser gives the 'Access-Control-Allow-Origin' error, the request has still been made by the browser. If withCredentials is specified by the attacking page. (Which is why our regex matches that)

then this request will be sent to your domain with the victim's authentication cookies, meaning that the request will succeed.

- Generate PoC


# License

I don't give a fuck man, copy, paste, edit as much as you want ;)
