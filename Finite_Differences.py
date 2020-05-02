from math import *

f = lambda x: sin(x)

x = 0

orig_value = cos(x)


def forward_differences(f, h, x):
	""" 
    Forward Finite Differences. 
  
    Approximating the derivative using the Forward 
    Finite Method. 
  
    Parameters: 
    f : function to be used
    h : Step size to be used
    x : Given point
  
    Returns: Approximation
  
    """
	return (f(x + h) - f(x)) / h

def backward_differences(f, h, x):
	""" 
    Forward Finite Differences. 
  
    Approximating the derivative using the Backward
    Finite Method. 
  
    Parameters: 
    f : function to be used
    h : Step size to be used
    x : Given point
  
    Returns: Approximation
  
    """
	return (f(x) - f(x - h)) / h

def central_differences(f, h, x):
	""" 
    Forward Finite Differences. 
  
    Approximating the derivative using the Central
    Finite Method. 
  
    Parameters: 
    f : function to be used
    h : Step size to be used
    x : Given point
  
    Returns: Approximation
  
    """
	return (f(x + h) - f(x - h)) / (2 * h)

def rel_error(deriv, orig):
	""" 
    Relative Error. 
  
    Calculating the relative error after approximating the 
    derivative. 
  
    Parameters: 
    deriv : approximation
    orig : actual value
  
    Returns: Relative Error
  
    """
	return abs(orig - deriv) / abs(orig)

def print_result(h, deriv, rel_error):
	""" 
    Printing the results. 
  
    Printing the approximation and the relative error. 
  
    Parameters: 
    h : Step size
    deriv : approximation
    re_error : Relative Error
  
    """
	print(f"For h = {h}, f'(x) = {round(deriv, 8)}\t relative error = {round(rel_error, 8)}")

# Forward Differences

first_deriv_for1 = forward_differences(f, 0.1, x)
first_deriv_for2 = forward_differences(f, 0.01, x)
first_deriv_for3 = forward_differences(f, 0.001, x)
first_deriv_for4 = forward_differences(f, 0.0001, x)

rel_error_for1 = rel_error(first_deriv_for1, orig_value)
rel_error_for2 = rel_error(first_deriv_for2, orig_value)
rel_error_for3 = rel_error(first_deriv_for3, orig_value)
rel_error_for4 = rel_error(first_deriv_for4, orig_value)

print_result(0.1, first_deriv_for1, rel_error_for1)
print_result(0.01, first_deriv_for2, rel_error_for2)
print_result(0.001, first_deriv_for3, rel_error_for3)
print_result(0.0001, first_deriv_for4, rel_error_for4)

# Backward Differences

first_deriv_back1 = backward_differences(f, 0.1, x)
first_deriv_back2 = backward_differences(f, 0.01, x)
first_deriv_back3 = backward_differences(f, 0.001, x)
first_deriv_back4 = backward_differences(f, 0.0001, x)

rel_error_back1 = rel_error(first_deriv_back1, orig_value)
rel_error_back2 = rel_error(first_deriv_back2, orig_value)
rel_error_back3 = rel_error(first_deriv_back3, orig_value)
rel_error_back4 = rel_error(first_deriv_back4, orig_value)

print_result(0.1, first_deriv_back1, rel_error_back1)
print_result(0.01, first_deriv_back2, rel_error_back2)
print_result(0.001, first_deriv_back3, rel_error_back3)
print_result(0.0001, first_deriv_back4, rel_error_back4)

# Central Differences
first_deriv_cen1 = central_differences(f, 0.1, x)
first_deriv_cen2 = central_differences(f, 0.01, x)
first_deriv_cen3 = central_differences(f, 0.001, x)
first_deriv_cen4 = central_differences(f, 0.0001, x)

rel_error_cen1 = rel_error(first_deriv_cen1, orig_value)
rel_error_cen2 = rel_error(first_deriv_cen2, orig_value)
rel_error_cen3 = rel_error(first_deriv_cen3, orig_value)
rel_error_cen4 = rel_error(first_deriv_cen4, orig_value)

print_result(0.1, first_deriv_cen1, rel_error_cen1)
print_result(0.01, first_deriv_cen2, rel_error_cen2)
print_result(0.001, first_deriv_cen3, rel_error_cen3)
print_result(0.0001, first_deriv_cen4, rel_error_cen4)




