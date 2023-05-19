from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # take care of empty segment list
    # or one segment in the list
    if len(segments) == 0:
        return points
    if len(segments) == 1:
        return [segments[0].end]
    #sort list increasing start points
    segments.sort(key=lambda x: x.start)
    # get first segment as closest end
    closest_end = segments[0]
    for segment in segments[1:]:
        if segment.start <= closest_end.end:
            # this segment is shorter then closest_end
            if segment.end <= closest_end.end:
                closest_end = segment
            else:
                continue
        else:
            points.append(closest_end.end)
            closest_end = segment
    points.append(closest_end.end)
    return points

def manual_test(segments, expected):
    '''
    will print error if test fails or passed test if all good'''
    test_result = optimal_points(segments)
    for result, expect in zip(test_result, expected):
        if result != expect:
            print("# error! expected: ", expect, " but received: ", result)
            print("# expected:" , expected)
            print(test_result)
            return
    print("# passed manual test :D")

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
