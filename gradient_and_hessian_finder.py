import sys
sys.path.append("Utilities")

import sympy as sp
from gradient_hessian import get_function, compute_gradient_and_hessian, evaluate_at_point

f = get_function()
gradient, hessian = compute_gradient_and_hessian(f)

# Stampa la funzione, il gradiente e la Hessiana
print("\nf(x)=")
sp.pprint(f)
print("\n∇f(x)=")
sp.pprint(gradient)
print("\nHf(x)=")
sp.pprint(hessian)

# Calcola e stampa il gradiente e la Hessiana in un punto
gradient_at_point, hessian_at_point, point = evaluate_at_point(gradient, hessian)

print("\nxk=")
sp.pprint(point)
print("\n∇f(xk)=")
sp.pprint(gradient_at_point)
print("\nHf(xk)=")
sp.pprint(hessian_at_point)
