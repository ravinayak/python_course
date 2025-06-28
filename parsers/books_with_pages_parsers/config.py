"""
Configuration Module

Centralized configuration settings for the book scraper application.
"""

from typing import Dict, Any
from dataclasses import dataclass, field


@dataclass
class ScraperConfig:
    """Configuration for the web scraper."""
    base_url: str = 'https://books.toscrape.com/'
    url_template: str = 'https://books.toscrape.com/catalogue/page-{}.html'
    timeout: int = 10
    max_retries: int = 3
    retry_delay: float = 1.0


@dataclass
class AppConfig:
    """Configuration for the application."""
    max_books_to_show: int = 5
    log_file: str = 'logs.text'
    log_level: str = 'INFO'
    enable_debug_logging: bool = False


@dataclass
class RatingConfig:
    """Configuration for rating mappings."""
    rating_map: Dict[str, int] = field(default_factory=lambda: {
        'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
    })
    
    def get_rating_value(self, rating: str) -> int:
        """Get numeric value for a rating string."""
        return self.rating_map.get(rating, 0)


# Example of how to extend the configuration system
@dataclass
class DatabaseConfig:
    """Configuration for database settings (example extension)."""
    host: str = 'localhost'
    port: int = 5432
    database: str = 'books_db'
    username: str = 'user'
    password: str = 'password'


@dataclass
class Config:
    """Main configuration class combining all settings."""
    scraper: ScraperConfig = field(default_factory=ScraperConfig)
    app: AppConfig = field(default_factory=AppConfig)
    rating: RatingConfig = field(default_factory=RatingConfig)
    # database: DatabaseConfig = field(default_factory=DatabaseConfig)  # Uncomment to add database config
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if self.scraper.timeout <= 0:
            raise ValueError("Timeout must be positive")
        if self.app.max_books_to_show <= 0:
            raise ValueError("Max books to show must be positive")
        if self.scraper.max_retries < 0:
            raise ValueError("Max retries cannot be negative")


# Default configuration instance
DEFAULT_CONFIG = Config() 