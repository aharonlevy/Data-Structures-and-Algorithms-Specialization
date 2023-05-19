from sys import stdin


def min_refills(distance, tank, stops):
    '''
    Returns the minimum number of gas stops when driving the 'distance'
    '''
    # write your code here
    cur_location = 0
    cur_tank = tank
    stop_counter = 0

    for stop in stops:
        max_distance = update_max_distance(cur_location, cur_tank)
        if max_distance >= distance:
            # can get to finish line so finish
            return stop_counter
        if max_distance < stop:
            #refill gas
            stop_counter += 1
            cur_tank = tank
            max_distance = update_max_distance(cur_location, cur_tank)
        if max_distance >= stop:
            # if we have the fuel we'll go to the next station
            cur_tank -= stop - cur_location
            cur_location = stop
        else:
            return -1
    if cur_location + cur_tank < distance:
        stop_counter += 1
        cur_tank = tank
        max_distance = update_max_distance(cur_location, cur_tank)
    if cur_location + cur_tank >= distance:
        return stop_counter
    return -1

def update_max_distance(location, gas):
    '''
    return the new max distance the car can drive
    '''
    return location + gas

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
