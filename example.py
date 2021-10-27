"""
    Create a method that will return the same list but soreted and without its largest and smallest element
    For list with less than 3 elements it should return empty list.

    When supplied value is not a list or cannot be sorted it should raise a ValueError with message:
    'You need to supply an array with sortable elements'

    Examples:
    [1,2,3] produces [2]
    [4,2,1,3] produces [2,3]
    [1,2] produces []
    [1] produces []
    [2,2,2,2,2,2] produces [2,2,2,2]
    ['ccc', 'aaa', 'ddd', 'eee', 'bbb'] produces ['bbb', 'ccc', 'ddd']

"""

def getSortedWithoutMinMax(numbers):
    """
    Returns given list sorted in ascending order without its
    min and max values.

    Raises ValueError when list is not supplied or when 
    list contains of elements that cannot be sorted
    """

    try:
        len(numbers)
        numbers.sort()
    except:
        raise ValueError("You need to supply an array with sortable elements")

    if (len(numbers) < 3):
        return []

    numbers.sort()

    return numbers[1:-1]

