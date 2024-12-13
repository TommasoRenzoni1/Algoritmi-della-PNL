import sys
sys.path.append("Utilities")

from colorama import Fore, Style, Back
import sympy as sp
from scipy.optimize import linprog
from sympy import lcm, gcd

from gradient_hessian import get_function, compute_gradient_and_hessian, evaluate_at_point
from Frank_Wolfe_for_maximum import frank_wolfe_maximum
from Frank_Wolfe_for_minimum import frank_wolfe_minimum
from Projected_gradient_ascent import projected_gradient_ascent, normalize_vector
from Projected_gradient_descent import projected_gradient_descent


def main():
    print(Fore.BLACK + Back.CYAN + "\nEx 4 (Only Frank Wolfe and projected gradient):" + Style.RESET_ALL)
    print(Fore.CYAN + "\nChoose an optimization method:" + Style.RESET_ALL)

    choice = input("1. Maximize (Frank-Wolfe and projected gradient ascent)\n2. Minimize (Frank-Wolfe and projected gradient descent\n"
                   "3. Frank-Wolfe for maximum\n4. Frank-Wolfe for minimum \n5. Projected gradient ascent \n6. Projected gradient descent \nEnter your choice (1-6): ").strip()
    if(choice != "1" and choice != "2" and choice !="3" and choice !="4" and choice != "5" and choice != "6"):
        print(Fore.RED + "Invalid choice! Please run the program again and choose a valid option." + Style.RESET_ALL)
        return
    
    
    # Get the function to optimize
    f = get_function()

    # Compute the gradient and Hessian symbolically
    gradient, hessian = compute_gradient_and_hessian(f)
    print(Fore.CYAN + "\nf(x)=" + Style.RESET_ALL)
    sp.pprint(f)
    print(Fore.CYAN + "\n∇f(x)=" + Style.RESET_ALL)
    sp.pprint(gradient)

    # Evaluate the gradient, Hessian, and initial point numerically
    gradient_at_point, hessian_at_point, xk = evaluate_at_point(gradient, hessian)
    xk = [sp.Rational(val) for val in xk]
    gradient_at_point = [sp.nsimplify(val) for val in gradient_at_point]

    print(Fore.CYAN + "\nxk=" + Style.RESET_ALL)
    sp.pprint(xk)
    print(Fore.CYAN + "\n∇f(xk)=" + Style.RESET_ALL)
    sp.pprint(gradient_at_point)

    # Input for polyhedron Ax <= b
    print(Fore.CYAN + "\nEnter the polyhedron Ax <= b:" + Style.RESET_ALL)
    
    # Matrix A
    rows = int(input("Enter the number of constraints (rows of A): "))
    cols = len(xk)
    A = []
    for i in range(rows):
        row = input(f"Enter row {i+1} of A (space-separated): ").strip().split()
        if len(row) != cols:
            raise ValueError(f"Row {i+1} must have exactly {cols} elements (matching the dimension of xk).")
        A.append([sp.Rational(val) for val in row])

    # Vector b
    b = input("Enter the vector b (space-separated): ").strip().split()
    if len(b) != rows:
        raise ValueError("Vector b must have the same number of elements as the number of rows in A.")
    b = [sp.Rational(val) for val in b]

    # Decide if you want to maximize or minimize
    

    if choice == '1':
        print("\n" + Fore.BLACK + Back.CYAN + "Performing one iteration of Frank-Wolfe for maximum:" + Style.RESET_ALL)
        frank_wolfe_maximum(f, gradient_at_point, xk, A, b)
        print("\n" + Fore.BLACK + Back.CYAN + "Performing one iteration of Projected Gradient Ascent:" + Style.RESET_ALL)
        projected_gradient_ascent(f, gradient_at_point, xk, A, b)
    elif choice == '2':
        print("\n" + Fore.BLACK + Back.CYAN + "Performing one iteration of Frank-Wolfe for minimum:" + Style.RESET_ALL)
        frank_wolfe_minimum(f, gradient_at_point, xk, A, b)
        print("\n" + Fore.BLACK + Back.CYAN + "Performing one iteration of Projected Gradient Descent:" + Style.RESET_ALL)
        projected_gradient_descent(f, gradient_at_point, xk, A, b)
    elif choice == '3':
        print("\n" + Fore.BLACK + Back.CYAN + "Performing one iteration of Frank-Wolfe for maximum:" + Style.RESET_ALL)
        frank_wolfe_maximum(f, gradient_at_point, xk, A, b)
    elif choice == '4':
        print("\n" + Fore.BLACK + Back.CYAN + "Performing one iteration of Frank-Wolfe for minimum:" + Style.RESET_ALL)
        frank_wolfe_minimum(f, gradient_at_point, xk, A, b)
    elif choice == '5':
        print("\n" + Fore.BLACK + Back.CYAN + "Performing one iteration of Projected Gradient Ascent:" + Style.RESET_ALL)
        projected_gradient_ascent(f, gradient_at_point, xk, A, b)
    elif choice == '6':
        print("\n" + Fore.BLACK + Back.CYAN + "Performing one iteration of Projected Gradient Descent:" + Style.RESET_ALL)
        projected_gradient_descent(f, gradient_at_point, xk, A, b)
        

if __name__ == "__main__":
    main()