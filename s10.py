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
user_count = 10_000

Profile = namedtuple("Profile", faker.profile().keys())
Profile.__doc__ = "`named tuple` for fake profile containing various fields providing information about each user's basic details"

for field_ in Profile._fields:
    getattr(Profile,
            field_).__doc__ = f"field `{field_}` containing information for a particular user's {field_} details"
print(help(Profile))


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


def calculate_metrics_namedtuples(to_print=False, *, fake_profiles: list) -> tuple:
    """
    To use all fake profiles passed by user and do the following:
    1) calculate the highest occurring blood type
    2) mean location
    3) oldest person's age
    4) average age

    :return: Tuple for the tasks' results in same order as above
    """
    blood_groups = []
    current_locations = []
    dobs = []
    for profile in fake_profiles:
        blood_groups.append(profile.blood_group)
        current_locations.append(profile.current_location)
        dobs.append(profile.birthdate)

    today = date.today()

    most_common_blood_group = Counter(blood_groups).most_common(1)[0][0]

    mean_location = reduce(lambda x, y: ((x[0] + y[0]) / 2, (x[1] + y[1]) / 2), current_locations)

    max_age = relativedelta(today, min(dobs))

    avg_age = reduce(lambda x, y: ((x[0] + y[0]) / 2, (x[1] + y[1]) / 2, (x[2] + y[2]) / 2),
                     [(relativedelta(today, x).years, relativedelta(today, x).months, relativedelta(today, x).days) for
                      x in dobs])
    if to_print:
        print(f"Highest occurring blood group= {most_common_blood_group}")
        print(f"Mean location= {mean_location}")
        print(f"Maximum age= {max_age.years}years {max_age.months}months {max_age.days}days")
        print(f"Average age= {avg_age[0]}years {avg_age[1]}months {avg_age[2]}days")

    return most_common_blood_group, mean_location, max_age, avg_age


def calculate_metrics_dictionary(to_print=False, *, fake_profiles: list) -> tuple:
    """
    1) calculate the highest occurring blood type
    2) mean location
    3) oldest person's age
    4) average age

    :return: Tuple for the tasks' results in same order as above
    """
    record_dict = defaultdict(dict)
    for profile in fake_profiles:
        record_dict[profile['ssn']] = profile

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


def get_profiles_namedtuples():
    """
    To use namedtuples and Faker library to generate 10000 random user profiles
    """
    all_profiles = []
    for _ in range(user_count):
        all_profiles.append(Profile(**faker.profile()))

    return all_profiles


def get_profiles_dictionary():
    """
    To use dictionary and Faker library to generate 10000 random user profiles
    """
    all_profiles = []
    for _ in range(user_count):
        fake = faker.profile()
        all_profiles.append(fake)
    return all_profiles


@timer(num=100)
def run_task_namedtuple_metrics():
    """Calls calculate_metrics_namedtuples() feeding profiles from get_profiles_namedtuples() using the decorator `timer` """
    calculate_metrics_namedtuples(fake_profiles=get_profiles_namedtuples())


@timer(num=100)
def run_task_dictionary_metrics():
    """Calls calculate_metrics_dictionary() feeding profiles from get_profiles_dictionary() which returns a dictionary of profiles the decorator `timer` """
    calculate_metrics_dictionary(fake_profiles=get_profiles_dictionary())


print(run_task_namedtuple_metrics())
print(run_task_dictionary_metrics())
