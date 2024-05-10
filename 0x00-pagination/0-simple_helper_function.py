#!/usr/bin/env python3
''' bassic pagination'''


def index_range(page, page_size):
    '''return a tuple of size two containing  start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
    '''
    if page:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index
