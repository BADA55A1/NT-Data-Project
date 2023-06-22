def forward_run(current_solution):
    new_solution = [*current_solution]
    max_var = max(new_solution)
    increment_index = None
    for i in reversed(range(len(new_solution))):
        if new_solution[i] < max_var:
            increment_value = None
            for increment in sorted(new_solution[i + 1:]):
                if increment_value is None:
                    if increment > new_solution[i]:
                        increment_value = increment
                else:
                    if increment < increment_value and increment > new_solution[i]:
                        increment_value = increment

            if increment_value:
                increment_index = i
                decrement_index = new_solution.index(increment_value)
                break

    if increment_index is not None:
        new_solution[increment_index] = current_solution[decrement_index]
        new_solution[decrement_index] = current_solution[increment_index]
        new_solution[increment_index + 1:] = sorted(new_solution[increment_index + 1:])
        return new_solution
    else:
        return None


def dim_1_neighbourhood(current_solution):
    back_run = forward_run(list(reversed(current_solution)))
    if back_run is not None:
        back_run = list(reversed(back_run))
    return [back_run,
            forward_run(current_solution)]


def _two_opt_swap(route, i, j):
    new_route = route[:i] + route[i:j + 1][::-1] + route[j + 1:]
    return new_route


def two_opt(route):
    new_routes = []
    for i in range(1, len(route) - 1):
        for j in range(i + 1, len(route)):
            new_routes.append(_two_opt_swap(route, i, j))
    return new_routes

def test():
    example_solution = [1, 2, 3, 5]  # is missing as is the starting and end point
    new_solution = (None, [*example_solution])

    solution_len = 0

    for i in range(10000):
        print(new_solution[1])
        new_solution = dim_1_neighbourhood(new_solution[1])
        print(new_solution)
        solution_len += 1
        if new_solution[1] is None:
            break
    print(solution_len)

    solution_len = 0
    new_solution = (list(reversed(example_solution)), None)
    for i in range(10000):
        new_solution = dim_1_neighbourhood(new_solution[0])
        print(new_solution)
        solution_len += 1
        if new_solution[0] is None:
            break
    print(solution_len)
# test()
