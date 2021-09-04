from dataclasses import dataclass
from typing import Optional


@dataclass
class RegionInfo:
    region: str
    region_code: int


@dataclass
class CityInfo:
    city: str
    code: int


@dataclass
class OfficeInfo:
    address_full: str
    code: str


@dataclass
class LocationInfo:
    code: Optional[int] = None
    postal_code: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
