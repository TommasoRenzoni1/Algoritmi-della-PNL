import sys
sys.path.append("Utilities")

from colorama import Fore, Style, Back
import sympy as sp
from gradient_hessian import get_function, compute_gradient_and_hessian, evaluate_at_point

# Gradient ascent with fixed step size
def fss_grad_ascent(f, gradient_at_point, hessian_at_point, xk, step=None):

    if step==None:
        hessian_list = hessian_at_point.tolist()
        max_abs_hessian = max(abs(hessian_list[i][j]) for i in range(len(hessian_list)) for j in range(len(hessian_list[i])))
        L = max_abs_hessian
        step = sp.Rational(2, L)
        print(f"The Lipschitz constant is L = {int(L)}")
        print(f"Automatically chosen step size: η = 2/L = {step}")

    x_new = [xk[i] + step * gradient_at_point[i] for i in range(len(xk))]
    xk_str = f"[{', '.join(map(str, xk))}]"
    grad_str = f"[{', '.join(map(str, gradient_at_point))}]"
    print(f"x_new = {xk_str} + {step} * {grad_str} = {x_new}")

    xk_values = {sp.symbols('x1'): xk[0], sp.symbols('x2'): xk[1]}
    xnew_values = {sp.symbols('x1'): x_new[0], sp.symbols('x2'): x_new[1]}
    
    f_at_xk = f.subs(xk_values)
    f_at_xnew = f.subs(xnew_values)

    print(f"f(xk) = f{tuple(xk)} = {f_at_xk}")
    print(f"f(x_new) = f{tuple(x_new)} = {f_at_xnew}")

# Gradient ascent with optimal step size
def oss_grad_ascent(f, gradient_at_point, xk):
    t = sp.symbols('t', real=True, positive=True)
    
    x_t = [xk[i] + t * gradient_at_point[i] for i in range(len(xk))]
    xk_str = f"[{', '.join(map(str, xk))}]"
    grad_str = f"[{', '.join(map(str, gradient_at_point))}]"
    print(f"r : {xk_str} + t * {grad_str} = {x_t}")

    x_symbols = sp.symbols(f'x1:{len(xk)+1}')
    x_t_subs = {x_symbols[i]: x_t[i] for i in range(len(xk))}
    g_t = f.subs(x_t_subs)
    print(f"ϕ(t) = f({x_t}) = {g_t}")
    g_t_expanded = sp.expand(g_t)
    print(f"ϕ(t) (canonical form) = {g_t_expanded}")

    g_t_prime = sp.diff(g_t, t)
    print(f"ϕ'(t) = {g_t_prime}")
    t_critical = sp.solve(g_t_prime, t)
    print(f"Critical t points: {t_critical}")
    t_valid = [t_val for t_val in t_critical if t_val.is_real and t_val > 0]

    if t_valid:
        g_values = [(t_val, g_t.subs(t, t_val)) for t_val in t_valid]
        g_values_only = [g_t.subs(t, t_val) for t_val in t_valid]
        print(f"ϕ values for each (valid) critical point: {g_values_only}")
        t_optimal, max_value = max(g_values, key=lambda item: item[1])
        print(f"Optimal step size t* = {t_optimal} (maximizes ϕ(t*) = {max_value})")
        fss_grad_ascent(f, gradient_at_point, None, xk, t_optimal)

    else:
        print("No valid optimal step size found.")
        return


# Newton's method for maximum
def newton(f, gradient_at_point, hessian_at_point, xk):

    print("Constant step size: 1")
    
    hessian_inv = sp.Matrix(hessian_at_point).inv()
    hessian_inv = hessian_inv.applyfunc(lambda x: sp.nsimplify(x))
    print(f"Inverted Hessian matrix [Hf(xk)]^-1:")
    sp.pprint(hessian_inv)
    print()

    d = hessian_inv * sp.Matrix(gradient_at_point)
    print(f"[Hf(xk)]^-1 * ∇f(xk) = [", *[elem for elem in d],"]", sep=" ")

    x_new = [sp.Rational(xk[i] - d[i]) for i in range(len(xk))]
    xk_str = f"[{', '.join(map(str, xk))}]"
    d_str = f"[{', '.join(map(str, d))}]"
    print(f"x_new = {xk_str} - {d_str} = {x_new}")

    xk_values = {sp.symbols('x1'): xk[0], sp.symbols('x2'): xk[1]}
    xnew_values = {sp.symbols('x1'): x_new[0], sp.symbols('x2'): x_new[1]}
    f_at_xk = f.subs(xk_values)
    f_at_xnew = f.subs(xnew_values)

    print(f"f(xk) = f{tuple(xk)} = {f_at_xk}")
    print(f"f(x_new) = f{tuple(x_new)} = {f_at_xnew}")


# Armijo-Goldstein-Wolfe method for maximum
def armijo_wolfe(gradient, xk, passo_iniziale, alfa=0.1, beta=0.7):
    print("\n3. Armijo-Goldstein-Wolfe method:")

def main():
    print(Fore.BLACK + Back.CYAN + "\nAlgorithms for unconstrained max: \ngradient ascent (fixed and optimal step size), Newton's method, Armijo-Goldstein-Wolfe method\n" + Style.RESET_ALL)
    f = get_function()

    gradient, hessian = compute_gradient_and_hessian(f)  # symbolic
    print(Fore.CYAN + "\nf(x)=" + Style.RESET_ALL)
    sp.pprint(f)
    print(Fore.CYAN +"\n∇f(x)="+ Style.RESET_ALL)
    sp.pprint(gradient)
    print(Fore.CYAN +"\nHf(x)="+ Style.RESET_ALL)
    sp.pprint(hessian)

    gradient_at_point, hessian_at_point, xk = evaluate_at_point(gradient, hessian)  # numerical

    xk = [sp.Rational(val) for val in xk]
    #gradient_at_point = [sp.Rational(val) for val in gradient_at_point]
    gradient_at_point = [sp.nsimplify(val) for val in gradient_at_point]

    print(Fore.CYAN + "\nxk=" + Style.RESET_ALL)
    sp.pprint(xk)
    print(Fore.CYAN +"\n∇f(xk)="+ Style.RESET_ALL)
    sp.pprint(gradient_at_point)
    print(Fore.CYAN +"\nHf(xk)="+ Style.RESET_ALL)
    sp.pprint(hessian_at_point)

    print("\n" + Fore.BLACK + Back.CYAN + "1. Gradient ascent with fixed step size:" + Style.RESET_ALL)
    fss_grad_ascent(f, gradient_at_point, hessian_at_point, xk)

    print("\n" + Fore.BLACK + Back.CYAN + "2. Gradient ascent with optimal step size:" + Style.RESET_ALL)
    oss_grad_ascent(f, gradient_at_point, xk)

    print("\n" + Fore.BLACK + Back.CYAN + "3. Newton's method for maximum:" + Style.RESET_ALL)
    newton(f, gradient_at_point, hessian_at_point, xk)

    
if __name__ == "__main__":
    main()
