# Object Tag XSS


## Location

```
http://ip/index.php?page=media&src=nsa
```
## Breach

In this page we noticed that the website is using the query src to show the image, so we tried exploit it by passing a HTML code in base64 format that contains an HTML script Tag.

```
/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnSGVsbG8nKTwvc2NyaXB0Pg==
```

it's an XSS breach, an attacker could use it to run malicious script when the user use's a link that contains the script and benifit from it by stealing his data (cookies, localStoreg) or even redirecting the user to a similar fake page (Phishing attack)

## Solution

To be safe from XSS, the input must be sanitized. The web application code should never output data received as input directly to the browser.
in this case the src query must be filtered and make sure that the query is the name of image that exists in the server.