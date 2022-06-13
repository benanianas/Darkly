# ADMIN page

## Location

```
http://ip/robots.txt 
http://ip/whatever
http://ip/admin 
```
## Breach

After finding the robots.txt file wich is used to hide content from search engines crawlers so that content got not indexed in users searches in serch engines.
one of the pages we found in the robots.txt is http://ip/whatever contains a file with a  waht it looks like a user login and a password
root:8621ffdbc5698829397d97767ac13db3
a little search in md5 databses and we got our password "dragon"

we used the credentiels to ge access in the /admin page and boom we got the flag.

## Solution

robots.txt file does not hide files from a potencial attacker, we should not serve sensitive and secret files.
we can use .htaccess? or at least protect files with a password.
for the password we should always use a complicated password and make sure it's not and available in hashs database + use a more complicated hashing algorithm