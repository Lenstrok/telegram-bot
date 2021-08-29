from dataclasses import dataclass


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
