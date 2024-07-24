#!/usr/bin/env python3
BaseCaching = __import__("0-basic_cache").BaseCaching


class FIFOCache (BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        print("Putting key: {} and item: {} into cache".format(key, item))
        if len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS:
            for first_key in self.cache_data.keys():
                print("DISCARD:", first_key)
                del self.cache_data[first_key]
                break
        if key and item is not None:
            # print("Key and item are not None, proceeding to put them into cache")
            self.cache_data[key] = item
            print("Successfully put key: {} and item: {} into cache".format(key, item))

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
