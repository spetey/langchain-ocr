"""Module for Google LLM settings."""

from pydantic import Field
from pydantic_settings import BaseSettings


class GoogleSettings(BaseSettings):
    """Settings for Google LLMs.

    Attributes
    ----------
    model_name : str
        The name of the Google model to use. Defaults to "gemini-pro".
    google_api_key : str
        The Google API key.

    """

    class Config:
        """Config class for reading Fields from env."""

        env_prefix = "GOOGLE_"
        case_sensitive = False

    model_name: str = Field(
        default="gemini-pro",
        description="The name of the Google model to use.",
    )
    google_api_key: str = Field(description="The Google API key.")
