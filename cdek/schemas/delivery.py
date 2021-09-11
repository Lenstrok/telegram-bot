from dataclasses import dataclass
from typing import Optional, List


@dataclass
class DeliveryErrorInfo:
    code: str
    message: str


@dataclass
class DeliveryInfo:
    currency: Optional[str] = None  # Валюта, в которой рассчитана стоимость доставки (код СДЭК)
    delivery_sum: Optional[float] = None  # Стоимость доставки
    period_min: Optional[int] = None  # Минимальное время доставки (в рабочих днях)
    period_max: Optional[int] = None  # Максимальное время доставки (в рабочих днях)
    weight_calc: Optional[int] = None  # Расчетный вес (в граммах)
    total_sum: Optional[float] = None  # Стоимость доставки с учетом дополнительных услуг
    services: Optional[list] = None  # Дополнительные услуги (возвращается, если в запросе были переданы доп. услуги)
    errors: Optional[List[DeliveryErrorInfo]] = None
