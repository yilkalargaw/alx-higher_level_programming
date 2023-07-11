#!/usr/bin/python3
"""Inheritance Practice"""


class MyInt(int):
    """Int >> MyInt"""

    def __eq__(self, other: object) -> bool:
        """
        Returns False if the MyInt object is equal to the given object.
        Args:
            other: The object to compare to.
        Returns:
            F/T
        """
        return not super().__eq__(other)

    def __ne__(self, other: object) -> bool:
        """
        Returns True if the MyInt object is not equal to the given object.
        Args:
            other:
        Returns:
            T/F
        """
        return super().__eq__(other)
