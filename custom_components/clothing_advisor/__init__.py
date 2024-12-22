from homeassistant.core import HomeAssistant

DOMAIN = "clothing_advisor"


async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up the integration from a config entry."""
    hass.data[DOMAIN] = entry.data
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True


async def async_unload_entry(hass: HomeAssistant, entry):
    """Unload the integration."""
    return await hass.config_entries.async_forward_entry_unload(entry, "sensor")
"""The example sensor integration."""
