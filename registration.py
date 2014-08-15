
_functions = {}

def usercode(name):
    def helper(func):
        global _functions
        if name in _functions:
            raise Exception("Name '{0}' already registered.".format(name))
        _functions[name] = func
        return func
    return helper

def get_user_funcs():
    global _functions
    return _functions.values()
