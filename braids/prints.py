def stringify_triangles_pretty(trs, prefix="", justify=4):
  return prefix + "  ".join([
    "".join(
      [str(y) for y in x]
    ).ljust(justify) for x in [tuple(sorted(t)) for t in trs]
  ])


def print_triangles_pretty(*args, **kwargs):
  print(stringify_triangles_pretty(*args, **kwargs))


def basis2str(basis):
  return \
    '(' + \
    ','.join([
      "".join([str(z) for z in sorted(v, key=lambda s: str(s))]) for v in basis
    ]) + \
    ')'
