"""
hs-scraper-toolkit: A comprehensive toolkit for scraping high school sports data.

This package provides tools for scraping athletic data from various websites including
MaxPreps and Athletic.net, with support for roster information and event schedules.
Also includes school-specific modules for targeted data extraction.
"""

__version__ = "1.1.0"
__author__ = "Tanmay Garg"
__email__ = "stampede.ncp@gmail.com"

# Import main classes for easy access
from .Athletics.AthleticNetTrackField import AthleticNetTrackField
from .Athletics.MaxPrepRoster import MaxPrepRoster

# Import school-specific modules
from .Northside.AthleticsSchedule import AthleticsSchedule
from .Northside.GeneralEvent import GeneralEvent

__all__ = [
    "AthleticNetTrackField", 
    "MaxPrepRoster",
    "AthleticsSchedule",
    "GeneralEvent"
]
