#


## HCaptchaVerifier
[source](https://github.com/VaibhavSys/hcaptcha/blob/main/hcaptcha/hcaptcha.py/#L22)
```python 
HCaptchaVerifier(
   secret_key: str, logger: typing.Optional[logging.Logger] = None
)
```


---
A class for verifying hcaptcha responses using the hcaptcha verification API.


**Methods:**


### .verify
[source](https://github.com/VaibhavSys/hcaptcha/blob/main/hcaptcha/hcaptcha.py/#L38)
```python
.verify(
   response: str, remote_ip: typing.Optional[str] = None
)
```

---
Verify an hcaptcha response using the hcaptcha verification API.


**Args**

* **response** (str) : The hcaptcha response token to verify.
* **remote_ip** (str, optional) : The remote IP address of the user who solved the captcha.


**Returns**

* **bool**  : True if the response is valid, False otherwise.


### .__init__
[source](https://github.com/VaibhavSys/hcaptcha/blob/main/hcaptcha/hcaptcha.py/#L27)
```python
.__init__(
   secret_key: str, logger: typing.Optional[logging.Logger] = None
)
```

---
Initialize a new HCaptchaVerifier instance.


**Args**

* **secret_key** (str) : The hcaptcha secret key for your site.


----


## HCaptchaVerificationError
[source](https://github.com/VaibhavSys/hcaptcha/blob/main/hcaptcha/hcaptcha.py/#L5)
```python 
HCaptchaVerificationError(
   error_codes: typing.Union[str, typing.List[str]]
)
```


---
An exception raised when the hcaptcha verification API returns an error.
