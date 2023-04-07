import aiohttp
import typing
import logging

class HCaptchaVerificationError(Exception):
    """
    An exception raised when the hcaptcha verification API returns an error.
    """

    def __init__(self, error_codes: typing.Union[str, typing.List[str]]):
        """
        Initialize a new HCaptchaVerificationError instance.

        Args:
            error_codes (Union[str, List[str]]): A list of error codes returned by the hcaptcha verification API.
        """
        self.error_codes = error_codes

    def __str__(self):
        return f"HCaptcha verification failed with error codes: {self.error_codes}"

class HCaptchaVerifier:
    """
    A class for verifying hcaptcha responses using the hcaptcha verification API.
    """

    def __init__(self, secret_key: str, logger: typing.Optional[logging.Logger] = None):
        """
        Initialize a new HCaptchaVerifier instance.

        Args:
            secret_key (str): The hcaptcha secret key for your site.
        """
        self.secret_key = secret_key
        self.verification_url = "https://hcaptcha.com/siteverify"
        self.logger = logger

    async def verify(self, response: str, remote_ip: typing.Optional[str] = None) -> bool:
        """
        Verify an hcaptcha response using the hcaptcha verification API.

        Args:
            response (str): The hcaptcha response token to verify.
            remote_ip (str, optional): The remote IP address of the user who solved the captcha.

        Returns:
            bool: True if the response is valid, False otherwise.
        """
        if self.logger:
            self.logger.debug(f"HCAPTCHA VERIFICATION REQUEST: response: {response}, remote_ip: {remote_ip}, secret_key: {self.secret_key}")
        if not response:
            if self.logger:
                self.logger.error("No hcaptcha response input provided.")
            raise HCaptchaVerificationError("No hcaptcha response input provided.")
        async with aiohttp.ClientSession() as session:
            data = {
                "secret": self.secret_key,
                "response": response
            }
            if remote_ip:
                data["remoteip"] = remote_ip
            async with session.post(self.verification_url, data=data) as reqresponse:
                result = await reqresponse.json()
                error_codes = result.get("error-codes", [])
                if len(error_codes) > 0:
                    if self.logger:
                        self.logger.debug(f"HCaptcha verification failed with error codes: {error_codes}")
                    return {"success": False, "errors": error_codes}
                status = result["success"]
                if self.logger:
                    self.logger.debug(f"HCAPTCHA VERIFICATION RESULT: success: {status}, response: {response}, remote_ip: {remote_ip}, secret_key: {self.secret_key}")
                return {"success": status}
