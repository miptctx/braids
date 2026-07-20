from braids.utils import sort_triangulation


def replace_in_set(s: set, original: list, permutation: list) -> set:
  if len(original) != len(permutation):
    raise ValueError("Списки должны быть одинаковой длины")

  mapping = dict(zip(original, permutation))
  return {mapping.get(x, x) for x in s}


def replace_in_tuple(t: tuple, original: list, permutation: list) -> tuple:
  if len(original) != len(permutation):
    raise ValueError("Списки должны быть одинаковой длины")

  mapping = dict(zip(original, permutation))
  return tuple(mapping.get(x, x) for x in t)


def permute_in_triangulations(trs, original, permutation):
  return sort_triangulation(*tuple([replace_in_set(t, original, permutation) for t in trs]))

def permute_in_flips(fps, original, permutation):
  return tuple([replace_in_set(f, original, permutation) for f in fps])

