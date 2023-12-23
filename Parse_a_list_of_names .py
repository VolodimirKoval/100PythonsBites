"""
1. Write a function that accepts a list of names and title cases them and removes duplicates.

2. Next, sort the list in alphabetical descending order by surname.

3. Finally, find the shortest first name.

You can assume that the names in the list are single strings composed of two words: one given name and one surname.

Python built-ins will be very useful for solving these problems in very concise ways. Get it sorted!
"""


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    names = list(set(name.title() for name in names))
    return names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    sorted_names = sorted(dedup_and_title_case_names(names), key=lambda name: name.split()[-1], reverse=True)
    return sorted_names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortest_name = min(names, key=lambda name: len(name.split()[0]))
    return shortest_name.split()[0]


print(shortest_first_name(NAMES))


