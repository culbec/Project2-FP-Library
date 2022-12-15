# Bingo sort
def min_max(iterable, key, reverse):
    """
    Searches the minimum and maximum element in iterable
    :param iterable: something iterable
    :param key: the parameter that we'll sort from
    :param reverse: True - descending order, False - ascending order
    :return: (minimum, maximum)
    """
    mini = maxi = next(elem for elem in iterable)
    for elem in iterable:
        if key(mini, elem, reverse):
            mini = elem
        if not key(maxi, elem, reverse):
            maxi = elem
    return mini, maxi


def bingo_sort(iterable, key=None, reverse=False):
    """
    Bingo sort the 'iterable' entity
    :param iterable: something iterable
    :param key: the parameter that we'll sort from
    :param reverse: True - descending order, False - ascending
    :return: -
    """
    mini, maxi = min_max(iterable, key, reverse)
    current_bingo = mini
    next_bingo = maxi
    next_pos = 0
    while key(current_bingo, next_bingo, reverse):
        for index in range(0, len(iterable)):
            if current_bingo == iterable[index]:
                current_bingo, iterable[next_pos] = iterable[next_pos], current_bingo
                next_pos = next_pos + 1
            elif key(iterable[index], next_bingo, reverse):
                next_bingo = iterable[index]

        current_bingo = next_bingo
        next_bingo = maxi
    return iterable


# Merge sort - Recursive method
def merge_sort(iterable, key=None, reverse=False):
    """
    Merge sorts the passed 'iterable' entity.
    :param iterable: something iterable
    :param key: the parameter we'll sort from
    :param reverse: True - descending order, False - ascending
    :return: -
    """
    if len(iterable) <= 1:
        return iterable
    mid = len(iterable) // 2
    left_list = iterable[:mid]
    right_list = iterable[mid:]
    left_list = merge_sort(left_list, key, reverse)
    right_list = merge_sort(right_list, key, reverse)
    return merge(left_list, right_list, key, reverse)


def merge(iterable_left, iterable_right, key, reverse: bool):
    """
    Merges the two halves of the array by applying 'Divide and Conquer' strategy
    :param iterable_left: something iterable
    :param iterable_right: something iterable
    :param key: the parameter we'll sort from
    :param reverse: True - descending order, False - ascending
    :return: -
    """
    # declaring the result list
    result_list = []

    # declaring the sizes of the two halves
    size_iterable_left = len(iterable_left)
    size_iterable_right = len(iterable_right)

    # declaring the indexes to go through the two halves
    index_iterable_left = 0
    index_iterable_right = 0

    # starting the merging of the iterables
    while index_iterable_left < size_iterable_left and index_iterable_right < size_iterable_right:
        if key(iterable_left[index_iterable_left], iterable_right[index_iterable_right], reverse):
            result_list.append(iterable_left[index_iterable_left])
            index_iterable_left += 1
        else:
            result_list.append(iterable_right[index_iterable_right])
            index_iterable_right += 1

    # adding the remaining elements of the left iterable
    while index_iterable_left < size_iterable_left:
        result_list.append(iterable_left[index_iterable_left])
        index_iterable_left += 1

    # adding the remaining elements of the right iterable
    while index_iterable_right < size_iterable_right:
        result_list.append(iterable_right[index_iterable_right])
        index_iterable_right += 1

    return result_list


# Keys
def compare_names_clients(tuple_pairs: tuple, other: tuple, reverse: bool):
    """
    Compares the name of the clients based on the 'reverse' parameter
    :param tuple_pairs: tuple
    :param other: tuple
    :param reverse: boolean
    :return: True or False comparisons of the names of the clients based on 'reverse'
    """
    if reverse:
        return tuple_pairs[0].get_name() >= other[0].get_name()
    return tuple_pairs[0].get_name() <= other[0].get_name()


def compare_client_rentals(tuple_pairs: tuple, other: tuple, reverse: bool):
    """
    Compares the number of rentals of the clients based on the 'reverse' parameter
    :param tuple_pairs: tuple
    :param other: tuple
    :param reverse: boolean
    :return: True or False comparisons of the names of the clients based on 'reverse'
    """
    if reverse:
        return tuple_pairs[1] >= other[1]
    return tuple_pairs[1] <= other[1]


def compare_rentals_books(tuple_pairs: tuple, other: tuple, reverse: bool):
    """
    Compares the rentals of the books based on 'reverse' parameter
    :param tuple_pairs: tuple
    :param other: tuple
    :param reverse: boolean
    :return: True or False based on the comparisons
    """
    if reverse:
        return tuple_pairs[1] >= other[1]
    return tuple_pairs[1] <= other[1]


def compare_names_books(tuple_pairs: tuple, other: tuple, reverse: bool):
    """
    Compares the name of both the books based on the 'reverse' parameter
    :param tuple_pairs: tuple
    :param other: tuple
    :param reverse: boolean
    :return: True or False comparisons of the names of the books based on 'reverse'
    """
    if reverse:
        return tuple_pairs[0].get_title() >= other[0].get_title()
    return tuple_pairs[0].get_title() <= other[0].get_title()
