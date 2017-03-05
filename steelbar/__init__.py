#!/usr/bin/env python
"""Simple multilayered progress bar for Python 3."""
import datetime

__author__ = 'Vytautas Valiukonis <https://github.com/SSteel2>'
__version__ = '1.0'


class SteelBar:
    """Class implementing simple console progress bar.
    ~ Because it is not fun waiting hours without knowing how many hours. ~
    """

    # TODO: add colors with ANSI/VT100 comands
    # TODO: add time estimation
    # TODO: add incrementation for any level not only last

    # Static level counter
    s_current_level = 0
    s_max_level = 0

    def __init__(self, total_steps, flavor_text=None):
        """Initializes progress bar.

        Parameters:
            total_steps - number of total steps to completion
            flavor_text - text to display when starting progress calculation
        """
        if SteelBar.s_current_level > 0:
            print()
        SteelBar.s_current_level += 1
        if SteelBar.s_current_level > SteelBar.s_max_level:
            SteelBar.s_max_level = SteelBar.s_current_level
        self.total = total_steps
        self.current = 0
        self.percentage_number = 0
        self.is_named = flavor_text is not None
        if self.is_named:
            print(flavor_text)
        else:
            print()

        # Bar size constant
        self.BAR_SIZE = 50

        self._DrawBar()
        self.start_time = datetime.datetime.now()

    def Increment(self):
        """Increments counter by one. Redraws if necessary."""
        self.current += 1
        new_percentage_number = self.current * 100 // self.total
        if new_percentage_number > self.percentage_number:
            self.percentage_number = new_percentage_number
            self._DrawBar()

    def _DrawBar(self):
        """Draws progress bar."""
        if self.current > self.total:
            return

        completed_glyphs = self.current * self.BAR_SIZE // self.total
        empty_glyphs = self.BAR_SIZE - completed_glyphs
        bar_string = '[' + ('=' * completed_glyphs) + (' ' * empty_glyphs) + \
            '] ' + str(self.percentage_number) + ' %  '
        print('\r' + bar_string, end='')

        if self.current == self.total:
            self._Finalize()

    def _Finalize(self):
        """Finalizes progress bar output."""
        end_time = datetime.datetime.now()
        if SteelBar.s_current_level > 1:
            print(
                '   Elapsed {}\r\x1b[A'.format(
                    str(end_time - self.start_time)), end='')
            if self.is_named:
                print('{}\r\x1b[A'.format(' ' * 78), end='')
        else:
            print(
                '   Elapsed {}\r\n\x1b[{}B\n\n'.format(
                    str(end_time - self.start_time),
                    (SteelBar.s_max_level - 1) * 2), end='')
            SteelBar.s_max_level = 0
        SteelBar.s_current_level -= 1
