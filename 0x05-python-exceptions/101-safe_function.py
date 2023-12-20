#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as e:
        sys.stderr.write(f"Exception: {e}\n")
        return None
