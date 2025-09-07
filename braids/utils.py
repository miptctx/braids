from sage.all import *

def sort_triangulation(*args):
  return tuple([set(x) for x in sorted(args, key=lambda s: tuple(sorted(s, key=lambda r: str(r))))])


def get_permutations():
  unique_cycles = set()

  perms = Permutations([1,2,3,4,5])
  for perm in perms:
    cycle = list(perm)
    min_index = cycle.index(min(cycle))
    normalized_cycle = tuple(cycle[min_index:] + cycle[:min_index])

    cycle_r = list(reversed(cycle))
    min_index = cycle_r.index(min(cycle_r))
    normalized_cycle_r = tuple((cycle_r[min_index:] + cycle_r[:min_index]))

    if (normalized_cycle in unique_cycles) or (normalized_cycle_r in unique_cycles):
      continue

    unique_cycles.add(normalized_cycle)
  
  return sorted(unique_cycles)
