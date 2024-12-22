from config.custom_components.clothing_advisor import DOMAIN
from config.custom_components.clothing_advisor.helpers import (
    get_clothing_for_temperature,
)
from homeassistant.components.sensor import SensorEntity
# from . import DOMAIN, get_temperature_info


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up sensors from config entry."""
    temperature_sensor = hass.data[DOMAIN].get("entity_id")
    async_add_entities(
        [
            TOGSensor(hass, temperature_sensor),
            PyjamaSensor(temperature_sensor),
            BodysuitSensor(temperature_sensor),
            TopSensor(temperature_sensor),
        ]
    )


class TOGSensor(SensorEntity):
    """Sensor for TOG."""

    def __init__(self, hass, temperature_sensor):
        self.hass = hass
        self._temperature_sensor = temperature_sensor
        self._state = None

    @property
    def name(self):
        return "TOG Sensor"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Update the TOG based on the temperature."""
        temperature = self.hass.states.get(self._temperature_sensor).state
        if temperature:
            self._state = get_clothing_for_temperature(float(temperature), "tog")


class PyjamaSensor(SensorEntity):
    """Sensor for wear items."""

    def __init__(self, temperature_sensor):
        self._temperature_sensor = temperature_sensor
        self._state = None

    @property
    def name(self):
        return "Pyjama Sensor"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Update the wear items based on the temperature."""
        temperature = self.hass.states.get(self._temperature_sensor).state
        if temperature:
            self._state = get_clothing_for_temperature(float(temperature), "pyjamas")


class TopSensor(SensorEntity):
    """Sensor for wear items."""

    def __init__(self, temperature_sensor):
        self._temperature_sensor = temperature_sensor
        self._state = None

    @property
    def name(self):
        return "Top Sensor"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Update the wear items based on the temperature."""
        temperature = self.hass.states.get(self._temperature_sensor).state
        if temperature:
            self._state = get_clothing_for_temperature(float(temperature), "top")


class BodysuitSensor(SensorEntity):
    """Sensor for wear items."""

    def __init__(self, temperature_sensor):
        self._temperature_sensor = temperature_sensor
        self._state = None

    @property
    def name(self):
        return "Bodysuit Sensor"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Update the wear items based on the temperature."""
        temperature = self.hass.states.get(self._temperature_sensor).state
        if temperature:
            self._state = get_clothing_for_temperature(float(temperature), "bodysuit")
