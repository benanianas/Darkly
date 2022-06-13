# Request Header


## Location

```
http://ip/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c
```
## Breach

we found a commented html sections that conatians instructions to get our flag
we used theme and we changed the request "Referer" & "User-Agent"

any attacker could change the headers if a webpage depends on it for some functionalities

## Solution

- Never trust HTTP request headers since we it can be manipulated easily