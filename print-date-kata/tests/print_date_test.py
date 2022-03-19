import unittest
from unittest.mock import Mock

from print_date import PrintDate, Calendar, Printer


TODAY_VALUE = '2022-03-19'


class PrintDateTest(unittest.TestCase):
    def test_using_unittest_mock(self):
        calendar = Mock(Calendar)
        printer = Mock(Printer)
        calendar.today = Mock(return_value=TODAY_VALUE)

        print_date = PrintDate(calendar, printer)

        print_date.print_current_date()

        printer.print_line.assert_called_with(TODAY_VALUE)

    def test_using_own_mocks(self):
        calendar = CalendarDouble()
        printer = PrinterDouble()
        print_date = PrintDate(calendar, printer)

        print_date.print_current_date()

        self.assertTrue(printer.print_line_have_been_called_with(TODAY_VALUE))


class CalendarDouble(Calendar):
    def today(self):
        return TODAY_VALUE


class PrinterDouble(Printer):
    def __init__(self):
        self.print_line_have_been_called_value = None

    def print_line(self, line):
        self.print_line_have_been_called_value = line

    def print_line_have_been_called_with(self, value):
        return self.print_line_have_been_called_value == value
