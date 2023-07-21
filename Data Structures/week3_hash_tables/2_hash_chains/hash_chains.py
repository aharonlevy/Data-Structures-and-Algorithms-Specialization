# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == "check":
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # crate a list for every bucket
        self.elems = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print("yes" if was_found else "no")

    def write_chain(self, chain):
        print(" ".join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            if len(self.elems[query.ind]) == 0:
                print()
            else:
                # use reverse order, because we append strings to the end
                self.write_chain([cur for cur in self.elems[query.ind]])
        else:
            has_value = self._hash_func(query.s)
            if query.type == "find":
                if query.s not in self.elems[has_value]:
                    self.write_search_result(False)
                else:
                    self.write_search_result(True)
            elif query.type == "add":
                if query.s not in self.elems[has_value]:
                    self.elems[has_value].insert(0, query.s)
            else:
                if query.s in self.elems[has_value]:
                    self.elems[has_value].remove(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == "__main__":
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
