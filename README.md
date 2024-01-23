# XSS Presentation Repository

## Contents

- Frontend, which is vulnerable to XSS
- Backend, which has a keylogger built in

## Usage

To start both the front- and backend, run the following commands:

```bash
chmod +x run.sh
./run.sh
```

## Keylogger

You will find the malicious XSS Input in the `malicious_xss_injection.txt` file.
Simply copy it, and paste it into the input field on the frontend.

## Base 64

### Encoding

```bash
node b64.js -e "alert('XSS')"
```

### Decoding

```bash
node b64.js -d "YWxlcnQoJ1hTUycp"
```
