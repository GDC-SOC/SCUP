"""Interface for interacting with AWS Secrets Manager to obtain secrets
needed for the SCUP settings but stored in Secrets Manager.
"""

import boto3 as __boto3
from botocore.exceptions import ClientError

class SCUPSecrets:
    """Interface for retriving secrets from AWS Secrets Manager for use in the
    SCUP settings.
    """
    def __init__(self):
        self.__secrets = {
            "ALLOWED_HOSTS": [],
            "SECRET_KEY": "",
            "DBENGINE"
            "DBNAME": "",
            "DBUSER": "",
            "DBPASS": "",
            "DBHOST": "",
            "DBPORT": "",
            "CSRF_TRUSTED_ORIGINS": []
        }
        try:
            self.__smclient = __boto3.client("secretsmanager")
            self.get_secrets()
        except Exception as e:
            print(str(e))

    @property
    def allowed_hosts(self) -> list:
        """Retrieves the ALLOWED_HOSTS secret
        """
        return self.__secrets.get("ALLOWED_HOSTS", [])
    
    @property
    def secret_key(self) -> str:
        """Retrieves the SECRET_KEY secret
        """
        return self.__secrets.get("SECRET_KEY", "")
    
    @property
    def dbengine(self) -> str:
        """Retrieves the DBENGINE secret
        """
        return self.__secrets.get("DBENGINE", "")
    
    @property
    def dbname(self) -> str:
        """Retrieves the DBNAME secret
        """
        return self.__secrets.get("DBNAME", "")

    @property
    def dbuser(self) -> str:
        """Retrieves the DBUSER secret
        """
        return self.__secrets.get("DBUSER", "")

    @property
    def dbpass(self) -> str:
        """Retrieves the DBPASS secret
        """
        return self.__secrets.get("DBPASS", "")
    
    @property
    def dbhost(self) -> str:
        """Retrieves the DBHOST secret
        """
        return self.__secrets.get("DBHOST", "")
    
    @property
    def dbport(self) -> str:
        """Retrieves the DBPORT secret
        """
        return self.__secrets.get("DBPORT", "")
    
    @property
    def csrf_trusted_origins(self) -> list:
        """Retrieves the CSRF_TRUSTED_ORIGINS"""
        return self.__secrets.get("CSRF_TRUSTED_ORIGINS", [])

    def read_secrets(self):
        """Retrieves all secrets from AWS and temporarily loads them to
        self.__secrets.

        See AWS documentation below for more information on batch_get_secrets:
            https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager/client/batch_get_secret_value.html
        """
        # This API pages, but we don't use enough secrets **yet** to require it
        try:
            result = self.__smclient.batch_get_secret_value(
                SecretIdList=self.__secrets.keys()
            )
            secrets = result.get("SecretValues", [])
            errors = result.get("Errors", [])
            # Check for errors - raise a RuntimeError for any
            if errors:
                # Builds an error message from all returned errors. All in the form of
                # 'Secret Id' - 'Error Code' - 'Message', 'Secret Id' - ...
                error_str = ", ".join([f"{error.get('SecretId', 'No Secret Id')} - {error.get('ErrorCode', 'No Error Code')} - {error.get('Message', 'No Message')}" for error in errors])
                raise RuntimeError(error_str)
        except ClientError as e:
            print(str(e))
        except RuntimeError as e:
            print(str(e))
