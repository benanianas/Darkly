
# Input Value

## Location

```
http://ip/?page=survey
```
## Breach
In this page by changing the the survey input value we got the flag.
an attacker could use this breach to uplaod a wrong values to the databse and the survey would lose the integrity

## Solution

we should always check users inputs in the backend and filter out the values we don't want.