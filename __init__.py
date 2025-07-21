"""
hs-scraper-toolkit: A comprehensive toolkit for scraping high school sports data.

This package provides tools for scraping various high school sports websites
including MaxPreps and other athletic data sources.
"""

__version__ = "1.0.0"
__author__ = "Tanmay Garg"
__email__ = "stampede.ncp@example.com"

from .Athletics.MaxPrepRosterScraper import MaxPrepRosterScraper

__all__ = ["MaxPrepRosterScraper"]
