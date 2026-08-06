"""
Application Programming CCGC 5003  Summer 2026
Humber College Institute of Technology and Advanced Learning
Waypoint - Domain Engine
Part 1/2 - Distance value type + operator overloading (WP-101, WP-202)
Developed by (IATIDEL AKIK N10038365)

Description:
This module defines the Distance class, a value type representing a
length measurement with a magnitude and a unit ("km" or "mi"). It
validates that magnitude is never negative and that unit is one of
the two allowed values, exposes read-only access to both, and can
convert between units via convert().

It also overloads arithmetic and comparison operators so Distance
behaves like a real quantity: +, -, ==, <, >, plus readable str()/repr().

Design decision on mixed units (documented per WP-202):
- __add__ and __sub__ REJECT mixed units (raise ValueError). Silently
  auto-converting could hide unit mistakes from the caller, and it
  breaks the immutability/validation philosophy used everywhere else
  in this class - we always fail loudly rather than guess.
- __lt__ and __gt__ also REJECT mixed units (raise ValueError), for
  the same reason - ordering "3 km" vs "3 mi" is ambiguous unless the
  caller explicitly converts one first.
- __eq__ is the one exception: by Python convention, equality must
  NEVER raise an error (built-in tools like sorting, "in", and
  dictionaries rely on == always returning a safe bool). So mixed
  units simply compare as NOT EQUAL (False), not an error.
- In all cases, the caller can convert explicitly first:
  a + b.convert(a.unit)

Classes:
    Distance(magnitude, unit) : represents a distance value

Class methods:
    magnitude (property) : read-only access to the magnitude
    unit (property)      : read-only access to the unit
    convert(to_unit)      : returns a NEW Distance in the other unit
    __add__(other)        : adds two same-unit Distances
    __sub__(other)        : subtracts two same-unit Distances
    __eq__(other)         : True if same unit AND same magnitude
    __lt__(other)         : True if this magnitude is less, same unit only
    __gt__(other)         : True if this magnitude is greater, same unit only
    __str__()             : human-readable string, e.g. "5.0 km"
    __repr__()            : developer string, e.g. "Distance(5.0, 'km')"
"""

# Conversion factor: 1 km = 0.621371 miles
KM_TO_MI = 0.621371

# Conversion factor: 1 mi = 1.60934 km
MI_TO_KM = 1.60934


class Distance:
    """
    Represents a distance with a magnitude and a unit ("km" or "mi").
    Rejects negative magnitudes and invalid units. Immutable - all
    operations that "change" a Distance return a brand new one.
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

        # Reject any unit that isn't "km" or "mi"
        if unit not in ["km", "mi"]:
            raise ValueError("Unit must be either 'km' or 'mi'")

        # Store privately - accessed only through read-only properties below
        self._magnitude = magnitude
        self._unit = unit

    @property
    def magnitude(self):
        """
        Read-only accessor for magnitude.
        Parameters: None
        Returns:
            magnitude (float): the stored distance value
        """
        return self._magnitude

    @property
    def unit(self):
        """
        Read-only accessor for unit.
        Parameters: None
        Returns:
            unit (str): the stored unit ("km" or "mi")
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
        # No conversion needed if already in the target unit
        if self._unit == to_unit:
            return Distance(self._magnitude, to_unit)

        # Convert km -> mi
        if self._unit == "km" and to_unit == "mi":
            converted_magnitude = self._magnitude * KM_TO_MI
        # Convert mi -> km
        elif self._unit == "mi" and to_unit == "km":
            converted_magnitude = self._magnitude * MI_TO_KM
        else:
            raise ValueError("Invalid unit conversion")

        # Return a brand new Distance - self is left untouched
        return Distance(converted_magnitude, to_unit)

    def __add__(self, other):
        """
        Adds two Distance objects of the SAME unit. Mixed units are
        rejected (not auto-converted) - see module docstring for why.
        Parameters:
            other (Distance): the distance to add
        Returns:
            Distance: a new Distance with the summed magnitude
        """
        # other isn't a Distance (e.g. someone wrote distance + 5).
        # Returning NotImplemented lets Python try other._radd__(self) or
        # raise its own clear TypeError, instead of us crashing here.
        if not isinstance(other, Distance):
            return NotImplemented

        if self._unit != other._unit:
            raise ValueError(
                f"Cannot add mixed units ({self._unit} + {other._unit}). "
                f"Convert one first, e.g. other.convert('{self._unit}')."
            )
        return Distance(self._magnitude + other._magnitude, self._unit)

    def __sub__(self, other):
        """
        Subtracts one Distance from another, same unit only.
        Parameters:
            other (Distance): the distance to subtract
        Returns:
            Distance: a new Distance with the difference
        """
        if not isinstance(other, Distance):
            return NotImplemented

        if self._unit != other._unit:
            raise ValueError(
                f"Cannot subtract mixed units ({self._unit} - {other._unit}). "
                f"Convert one first, e.g. other.convert('{self._unit}')."
            )
        return Distance(self._magnitude - other._magnitude, self._unit)

    def __eq__(self, other):
        """
        Checks equality of two Distance objects. Unlike +/-/</>, this
        NEVER raises - mixed units are simply treated as not equal,
        since Python convention requires == to always be safe to call.
        Parameters:
            other (object): the object to compare against
        Returns:
            bool: True if same unit AND same magnitude, False otherwise
        """
        if not isinstance(other, Distance):
            return False
        if self._unit != other._unit:
            # Different units are never equal - no error, just False
            return False
        return self._magnitude == other._magnitude

    def __lt__(self, other):
        """
        Checks if this Distance is less than another, same unit only.
        Parameters:
            other (Distance): the distance to compare
        Returns:
            bool: True if this magnitude is less than other's
        """
        if not isinstance(other, Distance):
            return NotImplemented

        if self._unit != other._unit:
            raise ValueError(
                f"Cannot compare mixed units ({self._unit} < {other._unit}). "
                f"Convert one first, e.g. other.convert('{self._unit}')."
            )
        return self._magnitude < other._magnitude

    def __gt__(self, other):
        """
        Checks if this Distance is greater than another, same unit only.
        Parameters:
            other (Distance): the distance to compare
        Returns:
            bool: True if this magnitude is greater than other's
        """
        if not isinstance(other, Distance):
            return NotImplemented

        if self._unit != other._unit:
            raise ValueError(
                f"Cannot compare mixed units ({self._unit} > {other._unit}). "
                f"Convert one first, e.g. other.convert('{self._unit}')."
            )
        return self._magnitude > other._magnitude

    def __str__(self):
        """
        Returns a human-readable string representation of this Distance.
        Called by str(distance) and print(distance).
        Parameters: None
        Returns:
            str: formatted string like "5.0 km"
        """
        return f"{self._magnitude} {self._unit}"

    def __repr__(self):
        """
        Returns a developer-friendly, unambiguous string representation
        of this Distance. Called by repr(distance), and shown when a
        Distance appears inside a list/dict in the console.
        Parameters: None
        Returns:
            str: formatted string like "Distance(5.0, 'km')"
        """
        return f"Distance({self._magnitude}, '{self._unit}')"