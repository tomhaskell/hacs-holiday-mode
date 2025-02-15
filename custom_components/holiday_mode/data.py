"""Custom types for holiday_mode."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from homeassistant.config_entries import ConfigEntry
    from homeassistant.loader import Integration

    from .api import HolidayModeApiClient
    from .coordinator import BlueprintDataUpdateCoordinator


type HolidayModeConfigEntry = ConfigEntry[HolidayModeData]


@dataclass
class HolidayModeData:
    """Data for the Blueprint integration."""

    client: HolidayModeApiClient
    coordinator: BlueprintDataUpdateCoordinator
    integration: Integration
