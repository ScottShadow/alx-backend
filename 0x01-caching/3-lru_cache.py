#!/usr/bin/env python3
BaseCaching = __import__("0-basic_cache").BaseCaching


class LRUCache (BaseCaching):
    key_list = {}
    least_rel = None
    ins_rel = 0

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        # print("Putting key: {} and item: {} into cache".format(key, item))
        if key and item is not None:
            # print("Key and item are not None, proceeding to put them into cache")
            if key not in self.key_list:
                # print("Key is not in key_list, checking cache size")
                if len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                    # print("Cache is full, discarding lest relevant key")
                    # print(self.key_list, f"LRK: {self.least_rel}")
                    for temp, _ in self.key_list.items():
                        if self.least_rel is None:
                            self.least_rel = temp
                        elif self.key_list[temp] < self.key_list[self.least_rel]:
                            self.least_rel = temp
                    discarded_key = self.least_rel
                    print("DISCARD: {}".format(discarded_key))
                    del self.cache_data[discarded_key]
                    del self.key_list[discarded_key]
                    self.least_rel = None
                self.cache_data[key] = item
                self.key_list[key] = self.ins_rel
                self.ins_rel += 1
                # print("Successfully put key: {} and item: {} into cache, LK:{}".format(
                #    key, item, self.key_list[-1]))
            else:
                # print("Key exists, updating cache")
                self.cache_data[key] = item
                self.key_list[key] += 1
                # print("Successfully updated key: {} and item: {} into cache, LK:{}".format(
                #    key, item, self.key_list[-1]))

    def get(self, key):
        # print("Getting key: {} from cache".format(key))
        if key is not None:
            if key in self.cache_data:
                # rint("Found key in cache")
                self.key_list[key] = self.ins_rel
                print(self.key_list)
                return self.cache_data[key]
        # print("Key not found in cache")
        return None
