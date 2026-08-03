"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Wayooint - Domain Engine
Part 1 - The Trail Model (WP-101)
Developed by ( IATIDEL AKIK N10038365)

Description:
This Module defines the distance class, a value type that represent 
a lenght measurement with a magnitude and a unit ("km" or "mi").
It validates that magnitude is a non-negative, exposes read-only access 
to its data, and can convert between units.

Classes:
    Distance (magintude, unit) : represents a distance value 

Class methods:
    magnitude(property) : read-only access to the magnitude
    unit(property) : read-only access to the unit
    convert(to_unit) : returns a new Distance in the other unit
"""

# Conversion factor: 1 km = 0.621371 miles
KM_TO_MI = 0.621371

# Conversion factor: 1 mi = 1.60934 km
MI_TO_KM = 1.60934

class Distance:
    """
    Represents a distance with a magnitude and a unit ("km" or "mi").
    Rejects negative magnitudes and invalid units.
    """
    def __init__(self, magnitude, unit):
        """
        Constructor: creates a Distance object.
        Parameters:
            magnitude (float): the distance value, must be non-negative
            unit (str): the unit of measurement, must be "km" or "mi"
        Returns:
            None
        """
         # Reject negative magnitudes - a distance can't be negative
        if magnitude < 0:
            raise ValueError("Magnitude cannot be negative")

        # Reject invalid units - only "km" and "mi" are allowed
        if unit not in ["km", "mi"]:
            raise ValueError("Unit must be either 'km' or 'mi'")

        # Store the magnitude and unit as private attributes
        self._magnitude = magnitude
        self._unit = unit

    @property
    def magnitude(self):
        """
        Read-only property to access the magnitude of the distance.
        Parameters:
            None
        Returns:
             magnitude (float): the stored distance value
        """
        return self._magnitude

    @property
    def unit(self):
        """
        Read-only property to access the unit of the distance.
        Parameters:
            None
        Returns:
            unit (str): the stored unit of measurement ("km" or "mi")
        """
        return self._unit

    def convert(self, to_unit):
        """
         Converts this distance to the given unit and returns a NEW
        Distance object - it does not modify the current object.
        Parameters:
            to_unit (str): the unit to convert to, "km" or "mi"
        Returns:
            Distance: a new Distance object holding the converted value
        """
        # No conversion needed if already in the requested unit
        if self._unit == to_unit:
            return Distance(self._magnitude, to_unit)

        # Convert km to mi
        if self._unit == "km" and to_unit == "mi":
            converted_magnitude = self._magnitude * KM_TO_MI
        # Convert mi to km
        elif self._unit == "mi" and to_unit == "km":
            converted_magnitude = self._magnitude * MI_TO_KM
        else:
            raise ValueError("Invalid unit conversion")

        # Return a new Distance object with the converted magnitude and requested unit
        return Distance(converted_magnitude, to_unit)
