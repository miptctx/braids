def sort_triangulation(*args):
  return tuple([set(x) for x in sorted(args, key=lambda s: tuple(sorted(s, key=lambda r: str(r))))])
