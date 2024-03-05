def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = ["dos", 3, 5]
#print(type(args))
#test_args_kwargs(*args)

kwargs = {"arg3": 3, "arg2": "dos", "arg1": 5}
test_args_kwargs(**kwargs)