from collections import namedtuple
from faker import Faker
from collections import defaultdict
from collections import Counter
from functools import reduce
from dateutil.relativedelta import relativedelta
from datetime import date
import time
from functools import wraps

faker = Faker()
user_count = 10


def timer(num):
    """
    Timer decorator that takes a paramter `num` the number of time to run the decorated function and calculate the average
    :param num: int signifying the number of time to run the function
    :return: the decorator for timing `fn` `num` times' average
    """

    def dec(fn):
        """The decorator that uses a closure for calculating average run time"""

        @wraps(fn)
        def inner(*args, **kwargs):
            """the inner most function responsible for carrying out the funtion runs 'num' time and return the average seconds"""

            start = time.perf_counter()
            for i in range(num):
                result = fn(*args, **kwargs)
            end = time.perf_counter()
            print(f"Average time taken to run function {fn} over {num} times = {(end - start) / num} seconds")
            return result

        return inner

    return dec


def task1(to_print=False):
    """
    To use namedtuples and Faker library to generate 10000 random user profiles and do the following:
    1) calculate the highest occurring blood type
    2) mean location
    3) oldest person's age
    4) average age

    :return: Tuple for the tasks' results in same order as above
    """
    fake = faker.profile()
    record_dict = defaultdict(list)

    Profile = namedtuple("Profile", fake.keys())
    Profile.__doc__ = "`named tuple` for fake profile containing various fields providing information about each user's basic details"

    for field_ in Profile._fields:
        getattr(Profile,
                field_).__doc__ = f"field `{field_}` containing information for a particular user's {field_} details"

    for _ in range(user_count):
        fake_profile = Profile(**faker.profile())

        record_dict['blood_group'].append(fake_profile.blood_group)
        record_dict['current_location'].append(fake_profile.current_location)
        record_dict['dob'].append(fake_profile.birthdate)

    today = date.today()

    most_common_blood_group = Counter(record_dict['blood_group']).most_common(1)[0][0]

    mean_location = reduce(lambda x, y: ((x[0] + y[0]) / 2, (x[1] + y[1]) / 2), record_dict['current_location'])

    max_age = relativedelta(today, min(record_dict['dob']))

    avg_age = reduce(lambda x, y: ((x[0] + y[0]) / 2, (x[1] + y[1]) / 2, (x[2] + y[2]) / 2),
                     [(relativedelta(today, x).years, relativedelta(today, x).months, relativedelta(today, x).days) for
                      x in record_dict['dob']])
    if to_print:
        print(help(Profile))
        print(f"Highest occurring blood group= {most_common_blood_group}")
        print(f"Mean location= {mean_location}")
        print(f"Maximum age= {max_age.years}years {max_age.months}months {max_age.days}days")
        print(f"Average age= {avg_age[0]}years {avg_age[1]}months {avg_age[2]}days")

    return most_common_blood_group, mean_location, max_age, avg_age


def task2(to_print=False):
    """
    To use dictionary and Faker library to generate 10000 random user profiles and do the following:
    1) calculate the highest occurring blood type
    2) mean location
    3) oldest person's age
    4) average age

    :return: Tuple for the tasks' results in same order as above
    """
    record_dict = defaultdict(dict)
    for _ in range(user_count):
        fake_profile = faker.profile()
        record_dict[fake_profile['ssn']] = fake_profile

    most_common_blood_group = Counter([b['blood_group'] for a, b in record_dict.items()]).most_common(1)[0][0]

    mean_location = reduce(lambda x, y: ((x[0] + y[0]) / 2, (x[1] + y[1]) / 2),
                           [b['current_location'] for a, b in record_dict.items()])

    today = date.today()
    max_age = relativedelta(today, min([b['birthdate'] for a, b in record_dict.items()]))

    avg_age = reduce(lambda x, y: ((x[0] + y[0]) / 2, (x[1] + y[1]) / 2, (x[2] + y[2]) / 2), [(relativedelta(today, b[
        'birthdate']).years, relativedelta(today, b['birthdate']).months, relativedelta(today, b['birthdate']).days) for
                                                                                              a, b in
                                                                                              record_dict.items()])
    if to_print:
        print(f"Highest occurring blood group= {most_common_blood_group}")
        print(f"Mean location= {mean_location}")
        print(f"Maximum age= {max_age.years}years {max_age.months}months {max_age.days}days")
        print(f"Average age= {avg_age[0]}years {avg_age[1]}months {avg_age[2]}days")

    return most_common_blood_group, mean_location, max_age, avg_age


@timer(num=100)
def run_task_1():
    """Calls task1() using the decorator `timer` """
    task1()


@timer(num=100)
def run_task_2():
    """Calls task2() using the decorator `timer` """
    task2()


print(run_task_1())
print(run_task_2())