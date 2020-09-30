# **Session 10 - Tuples and Named Tuples**

## **Assignment**
1. Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings)
2. Do the same thing above using a dictionary. Prove that namedtuple is faster.
3. Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple. 


## The Jupyter Notebook has results for 10K profiles as well Stock Exchange details (Top 100 companies stock details, Stock Index, High for the day, low close for the day)

> Tuples as a Data Structure

> Named Tuple

> Named Tuple - Modifying & Extending

> Named Tuple - DocString & Default Values

The primary reason for using namedtuples is to provide programmer with the flexibility of having named references for immutable data structure which is subclass of `tuple` and avoid errors during writing a program with non-pythonic way by using position idices to refer elements of a tuple.

Although `class` could be used in place of tuples to add more functionality, classed have additional over head.

Named Tuples come handy while accessing attributes like classes and unlike normal tuples.

`namedtuple` is a class factory.

Named tuples can be accessed by: 1) index 2) slice 3) iterate

Mutation of namedtuple throws error as underlying data structure is still a tuple which happens to be immutable.

The `rename` argument helps to initialize a namedtuple class without illegal identifier as attribute and replaces it with the positional int value prefixed by underscore.

`_fields` helps to get a tuple of all the attributes of a namedtuple instance.

`_asdict` helps to get an OrderedDict having key value pairs for all attributes and the corresponding values for a namedtuple instance.

  
## **Functions**

### 1. timer(num):
    """
    Timer decorator that takes a paramter `num` the number of time to run the decorated function and calculate the average
    :param num: int signifying the number of time to run the function
    :return: the decorator for timing `fn` `num` times' average
    """


### 2. calculate_metrics_namedtuples(to_print=False, *, fake_profiles: list) -> tuple:
    """
    To use all fake profiles passed by user and do the following:
    1) calculate the highest occurring blood type
    2) mean location
    3) oldest person's age
    4) average age

    :return: Tuple for the tasks' results in same order as above
    """
### 3. calculate_metrics_dictionary(to_print=False, *, fake_profiles: list) -> tuple:
    """
    1) calculate the highest occurring blood type
    2) mean location
    3) oldest person's age
    4) average age

    :return: Tuple for the tasks' results in same order as above
    """
    
### 4. get_profiles_namedtuples():
    """
    To use namedtuples and Faker library to generate 10000 random user profiles
    """
### 5. get_profiles_dictionary():
    """
    To use dictionary and Faker library to generate 10000 random user profiles
    """

### 6. @timer(num=100)
    def run_task_namedtuple_metrics():
        """Calls calculate_metrics_namedtuples() feeding profiles from get_profiles_namedtuples() using the decorator `timer` """

### 7. @timer(num=100)
    def run_task_dictionary_metrics():
        """Calls calculate_metrics_dictionary() feeding profiles from get_profiles_dictionary() which returns a dictionary of profiles the decorator `timer` """
