from homeassistant import config_entries
import voluptuous as vol

from homeassistant.const import CONF_ENTITY_ID

DOMAIN = "clothing_advisor"


class TemperatureWearConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Temperature Wear."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Clothing Advisor", data=user_input)

        sensors = [
            entity_id
            for entity_id in self.hass.states.async_entity_ids("sensor")
            if "temperature" in entity_id
        ]

        schema = vol.Schema({vol.Required(CONF_ENTITY_ID): vol.In(sensors)})

        return self.async_show_form(step_id="user", data_schema=schema)
