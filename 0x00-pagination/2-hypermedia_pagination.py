#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List


def index_range(page, page_size):
    '''return a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters.
    '''
    if page:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset


    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves the specified page of the dataset.

        Parameters:
            page (int): The page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: The specified page of the dataset.
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0

        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.dataset()):
            return []
        dataset = self.dataset()
        return dataset[start_index:end_index]
    
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """ returns a dictionary """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        total_pages = math.floor(len(self.dataset()) / page_size)
        return {'page_size': len(self.get_page(page, page_size)),
                'page': page,
                'data': self.get_page(page, page_size),
                'next_page': page + 1 if page + 1 < total_pages else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }