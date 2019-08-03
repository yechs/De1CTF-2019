# Solution to SSRF Me

## Code analyzing

### signature

The signature consists of three part:

1. a random generated secret secret key
2. the `param` parameter in the web request
3. the `action` cookies in the web request

You can visit `http://139.180.128.86/geneSign?param=[your_param]` to get signature with `action = scan`, and `param = [your_param]`

### file reading

`http://139.180.128.86/De1ta` reads in one parameter `param` and two cookies `action` and `sign`. Then, it will call task.Exec()

In task.Exec(), it'll first check if the `sign` matches with the signature generated with secret key, `param`, and `action`. If `sign` does not match, the server returns error msg "Sign Error"

If `action` = `scan`, it'll read file with path `param` and write it into a temporary file.

You would then need to use `scan` action to retrieve the temporary file.

## Get sign for `action = scan`, `param = flag.txt`

Since function geneSign() specifies variable `action = "scan"`, we can use the following URL to get the signature

GET `http://139.180.128.86/geneSign?param=flag.txt`

## Have the flag written in the temp file

Set cookies `action` = `scan` and `sign` = [the signature you retrieved from the above process]

GET `http://139.180.128.86/De1ta?param=flag.txt`

## Read from the temp file

Similar to the above process, however you would need to set `action = read` and `sign = ???`

*TO-DO*
