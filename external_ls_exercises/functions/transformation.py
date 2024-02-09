def python_rules(offending_string):
    trimmed = offending_string.strip("Ruby")  # aggressively remove ruby
    true_captain = trimmed + "Python"  # promote the true captain
    return true_captain


print(python_rules("Captain Ruby"))
