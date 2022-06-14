# Cookie Capturing

## Location

```
Cookies
```
## Breach

After checking the Cookies we found an interesting one I_am_admin with what it looks like a md5 hash as a value
after looking for a decryption for it's value => "false"
we changed with and md5 "true" value, and we got the flag.

an attacker could get an admin access to the website and this is very dangerous.

## Solution

we should never store such sensitive data in the Cookies
we could use secure session or other solution like jwt and always check that in the server our one and only source of truth.