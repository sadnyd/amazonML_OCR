# Define the mapping of units and their abbreviations
unit_mapping = {
    'width': [
        ('centimeter', 'cm'),
        ('foot', 'ft'),
        ('inch', 'in'),
        ('metre', 'm'),  # Or use ('meter', 'm') for US spelling
        ('millimeter', 'mm'),
        ('yard', 'yd')
    ],
    'depth': [
        ('centimeter', 'cm'),
        ('foot', 'ft'),
        ('inch', 'in'),
        ('metre', 'm'),
        ('millimeter', 'mm'),
        ('yard', 'yd')
    ],
    'height': [
        ('centimeter', 'cm'),
        ('foot', 'ft'),
        ('inch', 'in'),
        ('metre', 'm'),
        ('millimeter', 'mm'),
        ('yard', 'yd')
    ],
    'item_weight': [
        ('gram', 'gm'),
        ('kilogram', 'kg'),
        ('microgram', 'µg'),
        ('milligram', 'mg'),
        ('ounce', 'oz'),
        ('pound', 'lb'),
        ('ton', 't')
    ],
    'maximum_weight_recommendation': [
        ('gram', 'gm'),
        ('kilogram', 'kg'),
        ('microgram', 'µg'),
        ('milligram', 'mg'),
        ('ounce', 'oz'),
        ('pound', 'lb'),
        ('ton', 't')
    ],
    'voltage': [
        ('kilovolt', 'kV'),
        ('millivolt', 'mV'),
        ('volt', 'V')
    ],
    'wattage': [
        ('kilowatt', 'kW'),
        ('watt', 'W')
    ],
    'item_volume': [
        ('centilitre', 'cL'),
        ('cubic foot', 'ft³','cfeet'),
        ('cubic inch', 'in³','cinch'),
        ('cup', 'cup'),
        ('decilitre', 'dL'),
        ('fluid ounce', 'fl oz'),
        ('gallon', 'gal'),
        ('imperial gallon', 'imp gal'),
        ('litre', 'L'),
        ('microlitre', 'µL'),
        ('millilitre', 'mL'),
        ('pint', 'pt'),
        ('quart', 'qt')
    ]
}

# Example usage: printing out the mappings for 'width'
for unit, abbrs in unit_mapping['width']:
    print(f"{unit}: {abbrs}")
