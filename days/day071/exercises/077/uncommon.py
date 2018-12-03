def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    all_cities = list(set(my_cities + other_cities))
    return 2 * len(all_cities) - len(my_cities) - len(other_cities)