def func(x):
    intermediate_var = x ** 2 + x + 1

    if intermediate_var % 2:
        y = intermediate_var ** 3
    else:
        y = intermediate_var ** 3 + 1

    # set attributes here
    func.optional_return = intermediate_var
    func.is_awesome = 'yes, my func is awesome.'

    return y

y = func(3)
print('final answer is: ', y)

# accessing func attributes
print('show calculations --> ', func.optional_return)
print('is my function awesome? --> ', func.is_awesome)