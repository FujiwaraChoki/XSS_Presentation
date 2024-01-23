# XSS Presentation Repository

## Contents

- Frontend, which is vulnerable to XSS
- Backend, which has a keylogger built in

## Base 64

### Encoding

```bash
node b64.js -e "alert('XSS')"
```

### Decoding

```bash
node b64.js -d "YWxlcnQoJ1hTUycp"
```
