from sage.all import *
from braids import braiding
from braids.utils import sort_triangulation
from braids.prints import print_triangles_pretty

F = SR

z_1,z_2,z_3,z_4,z_5,z_6 = var("z_1,z_2,z_3,z_4,z_5,z_6")

assume(z_1 < z_2)
assume(z_2 < z_3)
assume(z_3 < z_4)
assume(z_4 < z_5)
assume(z_5 < z_6)

subs_vars_val = {z_1: 1, z_2: 2, z_3: 3, z_4: 4, z_5: 5, z_6: 6}
# subs_vars_val = {z_1: 11, z_2: 2, z_3: 31, z_4: 40, z_5: 515, z_6: 16}
# subs_vars_val = {z_1: 1/2, z_2: 2/3, z_3: 3/1, z_4: 4/3, z_5: 5/5, z_6: 6/7}


T = sort_triangulation({z_1,z_3,z_4}, {z_1,z_5,z_6}, {z_1,z_2,z_6}, {z_1,z_4,z_5}, {z_2,z_3,z_4}, {z_2,z_4,z_5}, {z_2,z_5,z_6})

##################################
##### trefoil on 3 strands #######
##################################
t, m_t = braiding(T,
                {z_2,z_5},{z_1,z_6},{z_2,z_4},{z_5,z_6},{z_3,z_4},
                {z_2,z_4},{z_1,z_5},{z_2,z_6},{z_5,z_4},{z_3,z_6},
                F=F)

m_p = matrix([
  [1,0,0,0,0,0,0],
  [0,1,0,0,0,0,0],
  [0,0,0,1,0,0,0],
  [0,0,1,0,0,0,0],
  [0,0,0,0,1,0,0],
  [0,0,0,0,0,0,1],
  [0,0,0,0,0,1,0]
])

m_t = m_t*m_p    # согласование базиса

print()
print('######  matrix result for trefoil  ######')
tref_trace = m_t.trace()
print("Trace:", latex(tref_trace))
print("Simplified trace:", latex(tref_trace.simplify_full()))


################################
##### Conjugated trefoil #######
################################

t_top, m_top = braiding(T, {z_2,z_5},{z_1,z_4},{z_5,z_6},{z_3,z_4}, F=F)
t_bot, m_bot = braiding(T, {z_2,z_4},{z_1,z_5},{z_5,z_6},{z_3,z_4}, F=F)
assert t_top == t_bot

print_triangles_pretty(T)
print_triangles_pretty(t)
print_triangles_pretty(t_top)

m = m_bot.subs({z_4:z_5, z_5:z_6, z_6:z_4})*m_t
m = m.subs({z_4:z_5, z_5:z_4})*m_top

print()
print('######  matrix result conjugated trefoil ######')
conj_tref_trace = m.trace()
print("Trace:", latex(conj_tref_trace))
print("Simplified trace:", latex(conj_tref_trace.simplify_full()))


print()
print("#### Check ####")
m_check = m_bot.subs({z_4:z_5, z_5:z_4})*m_top
m_check = m_check.simplify_full()
show(m_check)


tref_traces = []
conj_tref_traces = []
permuts = []
found = False
for x_1, x_2, x_3, x_4, x_5, x_6 in Permutations(subs_vars_val.keys()):
  # print(x_1, x_2, x_3, x_4, x_5, x_6)
  permuts.append((x_1, x_2, x_3, x_4, x_5, x_6))
  tref_traces.append(tref_trace.subs({z_1:x_1, z_2:x_2, z_3:x_3, z_4:x_4, z_5:x_5, z_6:x_6}).subs(subs_vars_val))
  conj_tref_traces.append(conj_tref_trace.subs({z_1:x_1, z_2:x_2, z_3:x_3, z_4:x_4, z_5:x_5, z_6:x_6}).subs(subs_vars_val))


print()
print("search for similar traces")
success_results = []
for i, t in enumerate(tref_traces):
  try:
    conj_index = conj_tref_traces.index(t)
    success_results.append((t, permuts[i], permuts[conj_index]))
    print(permuts[i], 'sucess', "-->", permuts[conj_index], ", trace:", t)
    found = True
  except ValueError as error:
    pass


print()
print(f'{len(success_results)} traces found' if found else 'similar traces NOT found')
print("success permutations:")
for t, p1, p2 in success_results:
  print(t, "\t", p1, "-->", p2)


exit()

print()
similar_traces = []
for t, p_1, p_2 in success_results:
  print("Trace int value:", t, "permutations:", p_1, "-->", p_2)
  x_1, x_2, x_3, x_4, x_5, x_6 = p_1
  subs_vars = {z_1:x_1, z_2:x_2, z_3:x_3, z_4:x_4, z_5:x_5, z_6:x_6}
  tref_trace_vars = tref_trace.subs(subs_vars).simplify_full()
  # print("Regular trefoil traces:", tref_trace_vars)
  x_1, x_2, x_3, x_4, x_5, x_6 = p_2
  subs_vars = {z_1:x_1, z_2:x_2, z_3:x_3, z_4:x_4, z_5:x_5, z_6:x_6}
  conj_tref_trace_vars = conj_tref_trace.subs(subs_vars).simplify_full()
  # print("Conjugated trefoil traces:", conj_tref_trace_vars)
  if tref_trace_vars == conj_tref_trace_vars:
    print("Similar trace found!!!")
    print("  Trace:", tref_trace_vars)
    print("  Perutations", p_1, p_2)
    similar_traces.append(tref_trace_vars)

if len(similar_traces) == 0:
  print("Similar symbols variables traces NOT found!")
