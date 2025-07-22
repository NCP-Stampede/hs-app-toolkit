"""
hs-scraper-toolkit: A comprehensive toolkit for scraping high school sports data.

This package provides tools for scraping athletic data from various websites including
MaxPreps and Athletic.net, with support for roster information and event schedules.
"""

__version__ = "1.0.1"
__author__ = "Tanmay Garg"
__email__ = "stampede.ncp@gmail.com"

# Import main classes for easy access
from .Athletics.AthleticNetTrackField import AthleticNetTrackField
from .Athletics.MaxPrepRoster import MaxPrepRoster

__all__ = ["AthleticNetTrackField", "MaxPrepRoster"]
