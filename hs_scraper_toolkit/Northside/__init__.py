"""
Northside College Prep specific scrapers.

This module contains scrapers designed specifically for Northside College Prep's
websites and platforms, including athletics schedules and general school events.
"""

from .AthleticsSchedule import AthleticsSchedule
from .GeneralEvent import GeneralEvent

__all__ = ['AthleticsSchedule', 'GeneralEvent']