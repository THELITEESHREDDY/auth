from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
   
    DATABASE_URL: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM:str
    SECRET_KEY:str
    MAIL_USERNAME:str
    MAIL_PASSWORD:str
    MAIL_FROM:str
    MAIL_PORT:str
    MAIL_SERVER:str
    
    #Add the SettingsConfigDict to read from the .env file
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Ignores extra fields in the .env that aren't defined here
    )

settings = Settings()