# Brute-force Attack

## Location

```
http://ip/?page=signin
```
## Breach

in the sign in page we used a simple python script that try a list of most common password
and it didn't take a lot of time to get our hands on the sign in credentials with the first username we think of "admin"
and the password "shadow"

## Solution
- use more complicated password and unpredictable usernames lika admin, administrator, administrateur ...
- limit server requests for the same ip.
