# Input Value

## Location

```
http://ip/?page=upload
```
## Breach
we tried to apload different files and scriot but the websites accept only jpeg files
so we used a curl command to apload a php script as a jpeg image and it worked
```
curl -X POST -F "uploaded=@./file.php;type=image/jpeg" http://ip/\?page\=upload -F "Upload=Upload" | grep flag

an attacker could easily upload a malicious script to the server and do whatever he want an your server.
```
## Solution

always check uploaded files (type, size) in both front-end and backend