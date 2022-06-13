# hidden Input

## Location

```
http://ip/?page=recover
```
## Breach

The password recovery page  has only a submit button wich is weird, normally in this pages we ask the user for his email to send the passord recovery instruction.
so we looked in it and we found a hidden field bu changing it's value we got the flag.

i'm not sure how exactly an attacker could benefit from it other than changing the email value by his email address and receive the email and check on any sensitive data if the website send really the recovery instructiom to that hidden email.

## Solution

The page should asks for the user's email and send recovery instruction email related to that email if found in the database and not use hidden input for this kind of operations cause "It's not really hidden"