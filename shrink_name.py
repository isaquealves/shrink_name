"""Module which contains a single function 'shrink_name'
"""
def shrink_name(fullname: str='') -> str:
    """Takes a person's full name as parameter and returns
    its first 13 characters.
    """
    name = ''
    if not fullname:
        return name
    try:

        if len(fullname) <= 13:
                return fullname
        fullname = fullname[:13]
        name = fullname.split(' ')
        name[-1] = '{0}.'.format(name[-1][0])
        return ' '.join(name)
    except TypeError:
        return name