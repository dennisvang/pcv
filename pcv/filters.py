import logging
from datetime import datetime


logger = logging.getLogger(__name__)


def as_date(value):
    """
    convert an iso 8601 date string to a datetime.date, return current date
    if string is not a valid iso string (e.g. empty string or "present")
    """
    try:
        return datetime.fromisoformat(value).date()
    except ValueError as e:
        logger.debug(e)
        return datetime.today().date()


def reformat(value, format_string='%Y, %b %d'):
    """
    re-format an iso 8601 date string to the specified format, except "present"
    """
    date_string = 'present'
    if value.lower() != date_string:
        date_string = as_date(value).strftime(format_string)
    return date_string


def as_circles(value, max_value=5):
    """
    represent an integer value as black and white circles, on a scale of 0 to
    max_value (we assume integers here...)
    """
    return '●' * value + '○' * (max_value - value)


def sort_and_group(item_list, date_field, group_field, reverse=True):
    """
    sort a list of items by date_field, and "group" successive items with
    identical group_field by removing redundant group_field values
    """
    item_list.sort(key=lambda i: as_date(i[date_field]), reverse=reverse)
    current_group = None
    for item in item_list:
        group = item[group_field].lower()
        if group == current_group:
            del item[group_field]
            logger.debug(f'field deleted: {group}')
        else:
            current_group = group
    return item_list