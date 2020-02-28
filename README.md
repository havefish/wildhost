# Wildhost
Checks wildcard domain names.

## Install
```
pip install wildhost
```

## Usage
Import the module

```python
>>> import wildhost
```
Pass a domain name to the `check` function.

```python
>>> wildhost.check(hostname)
```

If none of the levels of the name are wildcards, `None` will be returned.
```python
>>> wildhost.check('mail.google.com')
```

This returns `None` as neither `google.com` nor `mail.google.com` are wildcards.

For a wildcard name, the _lowest_ level wildcard name will be returned.
```python
>>> wildhost.check('foo.bar.spam.grok.sharefile.com')
'sharefile.com'
```