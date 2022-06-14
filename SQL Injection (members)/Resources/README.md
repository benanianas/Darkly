# SQL Injection

## Location

```
http://ip/?page=member
```
## Breach
in the input we tried the value 1 or 1=1  to check if there is an sql injection possibiltie and we got a response,
so we tried to look more into it by getting some database information using the next query
```
1337 or 1=1 UNION select table_name, column_name FROM information_schema.columns
```
after multiple queries combinations with the next query we succeeded to get some useful dinstructions to get our flag
```
1337 or 1=1 union select countersign, Commentaire from users
```
Decrypt this password -> then lower all the char. Sh256 on it and it's good !
5ff9d0165b4f92b14994e5c685cdce28

## Solution

the best approach is controlling and vetting user input to watch for attack patterns. 
use Parametrized queries or an database orm.