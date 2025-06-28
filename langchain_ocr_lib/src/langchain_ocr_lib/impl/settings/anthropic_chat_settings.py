"""Module for Anthropic LLM settings."""

from pydantic import Field
from pydantic_settings import BaseSettings


class AnthropicSettings(BaseSettings):
    """Settings for Anthropic LLMs.

    Attributes
    ----------
    model_name : str
        The name of the Anthropic model to use. Defaults to "claude-2".
    anthropic_api_key : str
        The Anthropic API key.

    """

    class Config:
        """Config class for reading Fields from env."""

        env_prefix = "ANTHROPIC_"
        case_sensitive = False

    model_name: str = Field(
        default="claude-2",
        description="The name of the Anthropic model to use.",
    )
    anthropic_api_key: str = Field(description="The Anthropic API key.")
