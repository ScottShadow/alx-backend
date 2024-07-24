#!/usr/bin/env python3
BaseCaching = __import__("0-basic_cache").BaseCaching


class LIFOCache (BaseCaching):
    key_list = []

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        # print("Putting key: {} and item: {} into cache".format(key, item))
        if key and item is not None:
            # print("Key and item are not None, proceeding to put them into cache")
            if key not in self.key_list:
                # print("Key is not in key_list, checking cache size")
                if len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
                    # print("Cache is full, discarding last key")
                    discarded_key = self.key_list[-1]
                    print("DISCARD: {}".format(discarded_key))
                    del self.cache_data[discarded_key]
                    self.key_list.pop()
                self.cache_data[key] = item
                self.key_list.append(key)
                # print("Successfully put key: {} and item: {} into cache, LK:{}".format(
                #    key, item, self.key_list[-1]))
            else:
                # print("Key exists, updating cache")
                self.cache_data[key] = item
                self.key_list.remove(key)
                self.key_list.append(key)
                # print("Successfully updated key: {} and item: {} into cache, LK:{}".format(
                #    key, item, self.key_list[-1]))

    def get(self, key):
        # print("Getting key: {} from cache".format(key))
        if key is not None:
            for cache_key in self.cache_data.keys():
                # print("Checking cache key: {}".format(cache_key))
                if cache_key == key:
                    # print("Found key in cache")
                    return self.cache_data[key]
        # print("Key not found in cache")
        return None
