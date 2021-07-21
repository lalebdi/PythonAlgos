""""
Bloom Filters: "lightweight" version of a hash table. Efficient insertions and lookups.
More space efficient than hash table, but this comes at the cost of having "false positives" for entry lookup.
consists of a bit vector and non cryptographic hash function -> Murmur and FNV both in pyhash
"""

import pyhash

bit_vector = [0] * 20

# Non cryptographic hash functions
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

# Calculate the output of FNV and Murmur hash functions for Pickachu and Charmander

fnv_pika = fnv("Pickachu") % 20 # -> so it will be between 0 and 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pickachu") % 20
murmur_char = murmur("Charmander") % 20

bit_vector[fnv_pika] = 1
bit_vector[fnv_char] = 1

bit_vector[murmur_pika] = 1
bit_vector[murmur_char] = 1

print(bit_vector)