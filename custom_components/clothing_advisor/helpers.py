def get_clothing_for_temperature(temperature: float, key: str) -> str:
    """Get the applicable clothing based on the given temperature.

    :param temperature: The temperature for which to get the clothing.
    :return: The applicable bodysuit ('sleeveless', another type, or 'None').
    """
    temperature_info = {
        15: {
            "tog": 3.5,
            "pyjamas": "long sleeve",
            "bodysuit": "sleeveless",
            "top": None,
        },
        17: {
            "tog": 3.5,
            "pyjamas": "long sleeve",
            "bodysuit": "sleeveless",
            "top": None,
        },
        19: {"tog": 3.5, "pyjamas": "long sleeve", "bodysuit": None, "top": None},
        21: {
            "tog": 2.5,
            "pyjamas": "long sleeve",
            "bodysuit": "sleeveless",
            "top": None,
        },
        23: {"tog": 1.0, "pyjamas": "long sleeve", "bodysuit": None, "top": None},
        25: {"tog": 0.2, "pyjamas": "long sleeve", "bodysuit": None, "top": None},
        27: {
            "tog": 0.2,
            "pyjamas": None,
            "bodysuit": "sleeveless",
            "top": None,
        },
    }

    # Find the closest temperature key
    closest_temp = min(temperature_info.keys(), key=lambda t: abs(t - temperature))

    # Get the bodysuit for the closest temperature
    return temperature_info[closest_temp].get(key) or "None"
