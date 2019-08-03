# Solution to SSRF Me

By visiting `http://139.180.128.86`, you can see the code in [code.txt](code.txt)

You can soon identify it as a python script using Flask, and then try to format it. The formatted version is at [code-formatted.py](code-formatted.py)

## Analyzing the code

### Reading the file

`http://139.180.128.86/De1ta` reads in one argument `param` and two cookies `action` and `sign`. Then, it will call task.Exec()

In task.Exec(), it'll first check if the `sign` matches with the signature generated with secret key, `param`, and `action`. If `sign` does not match, the server returns error msg "Sign Error"

If `action` = `scan`, it'll read file with path `param` and write it into a temporary file.

You would then need to use `scan` action to retrieve the temporary file.

### Signature

The signature consists of three part:

1. a random generated secret secret key
2. the `param` parameter in the web request
3. the `action` cookies in the web request

You can visit `http://139.180.128.86/geneSign?param=[your_param]` to get signature with `action = scan`, and `param = [your_param]`

## Solution

### Action *`if`*-statements

First, let's take a look at the action switches:

```python
if "scan" in self.action:
    # code omitted
    pass

if "read" in self.action:
    # opens the temp file containing content from scan()
    f = open("./%s/result.txt" % self.sandbox, 'r')
    result['code'] = 200
    result['data'] = f.read()
```

which means that as long as the string `self.action` contains `"read"`, the flag will be returned.

For example, simply set `action = readscan` would do the job. You can test this out using [the script](if-switch.py)

### Structure of signature

Then, let's took a closer look at the structure of the signature:

```python
def getSign(action, param):
    return hashlib.md5(secert_key + param + action).hexdigest()
```

### Obtain signature

If we set `action = readscan`, as stated above, the correct signature would be `hashlib.md5(secert_key + "flag.txt" + "readscan").hexdigest()`

Moreover, we can easily come to the conclusion that the two strings below are equivalent.

```python
secert_key =
str1 = secert_key + "flag.txt" + "readscan"
str2 = secert_key + "flag.txtread" + "scan"
```
You can test this out with [signature.py](signature.py)

Therefore, we can obtain the correct signature from the URL `http://139.180.128.86/geneSign?param=flag.txtread` *(like `str2`)*

### Capture the flag

Finally, we can send a request to `http://139.180.128.86/De1ta?param=flag.txt` with cookies `action = readscan` *(like `str1`)* and `sign = [the one you've just obtained]`

Therefore, the server would first read `flag.txt`, write it to the temporary file, and return the temporary file in the format below.

```json
{"code": 200, "data": "de1ctf{27782fcffbb7d00309a93bc49b74ca26}"}
```

Congratulations! This is the flag.
