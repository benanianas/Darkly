# Feedback form XSS

## Location

```
http://ip/?page=feedback
```
## Breach

In this page everyone could leave a feedback, and it's saved and everyone could see it, so if we could use an xss breach it will affect every user visiting this page.
even though the html tag sanitized and filtered out we managed to get the flag using the word script

it's an XSS breach, an attacker could use it to run malicious script when the user visit the page and benifit from it by stealing his data (cookies, localStoreg) or even redirecting the user to a similar fake page (Phishing attack)

## Solution

To be safe from XSS, the input must be sanitized. The web application code should never output data received as input directly to the browser.
in this case the src query must be filtered and make sure that the query is the name of image that exists in the server.