# Path Traversal


## Location

```
location: http://ip/?page=../../../../../../../etc/passwd
```
## Breach

By manipulating variables that reference files with ../ sequences using the page query, we tried to get to the server root directory
and trying to get to files in the root directory
we succeeded to find an passwd file and wd got our flag

## Solution

- always sanitize the page query and filter out the potential risks
- using an .htaccess to give access to only the website code and not every directory in the server.