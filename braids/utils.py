from sage.all import *

def sort_triangulation(*args):
  # return tuple([set(x) for x in sorted(args, key=lambda s: tuple(sorted(s, key=lambda r: str(r))))])
  return tuple([
    set(t) for t in sorted(args, key=lambda triangle: tuple(
      sorted(triangle, key=lambda point: point)
    ))
  ])


def get_permutations(var_list=[1,2,3,4,5]):
  unique_cycles = set()

  perms = Permutations(var_list)
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


def rotate_tuple(*t):
    if len(t) != 4 or len(set(t)) != 4:
        raise ValueError(f"Кортеж должен содержать 4 попарно различных числа, len={len(t)}, set={set(t)}")

    min_val = min(t)
    min_idx = t.index(min_val)

    result = t[min_idx:] + t[:min_idx]

    return tuple(result)
