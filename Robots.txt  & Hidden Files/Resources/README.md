# Hidden Files

## Location

```
http://ip/robots.txt 
http://ip/hidden 
```
## Breach

After finding the robots.txt file wich is used to hide content from search engines crawlers so that content got not indexed in users searches in serch engines.
one of the pages we found in the robots.txt is http://ip/hidden, the page contains a lot of folders with readme files that contains same phrases,
we made a script to crawl on all the readme files and get something in a ton of unuseful files.

## Solution

robots.txt file does not hide files from a potencial attacker, we should not serve sensitive and secret files.
we can use .htaccess? or at least protect files with a password.