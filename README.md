# hcaptcha
hcaptcha is a Python module (unofficial) that provides an easy-to-use interface for verifying hcaptcha responses using the hcaptcha verification API.

## Installation
You can install hcaptcha using pip:

```bash
pip install hcaptcha
```

## Usage
To use hcaptcha, you'll need an hcaptcha secret key for your site. You can get one by signing up for an account at [hcaptcha website](https://hCaptcha.com/?r=cc7220f46013).

```python
from hcaptcha.hcaptcha import HCaptchaVerifier, HCaptchaVerificationError

# Initialize the verifier with your hcaptcha secret key
verifier = HCaptchaVerifier(your_hcaptcha_secret_key)

# Verify an hcaptcha response
try:
    is_valid = await verifier.verify(user_response_token)
    if is_valid:
        print("Captcha verified successfully.")
    else:
        print("Captcha verification failed.")
except HCaptchaVerificationError as e:
    print(f"Verification failed with error: {str(e)}")
```
## Documentation
Documentation for hcaptcha is available [here](https://github.com/VaibhavSys/hcaptcha/blob/master/docs/sources/api/hcaptcha.md)

## Contributing
If you find a bug or have a feature request, please open an issue on [GitHub](https://github.com/VaibhavSys/hcaptcha).

## Licence
hcaptcha is distributed under the MIT License. See LICENSE for more information.