# Find maximus values
def find_max_values(e):
    max_values = []
    for i in range(1, len(e['x']) - 1):
        if e['x'][i] >= e['x'][i - 1] and e['x'][i] >= e['x'][i + 1] and e['x'][i] > 0:
            max_values.append(i)

    i = 0
    while i < len(max_values) - 1:
        if max_values[i + 1] - max_values[i] <= 3:
            val1 = e['x'][max_values[i]]
            val2 = e['x'][max_values[i + 1]]

            if val1 > val2:
                max_values.pop(i + 1)
            else:
                max_values.pop(i)
        else:
            i += 1

    return max_values


# Find minimus values
def find_min_values(e):
    min_values = []
    for i in range(1, len(e['x']) - 1):
        if e['x'][i] <= e['x'][i - 1] and e['x'][i] <= e['x'][i + 1] and e['x'][i] < 0:
            min_values.append(i)
    
    i = 0
    while i < len(min_values) - 1:
        if min_values[i + 1] - min_values[i] <= 3:
            val1 = e['x'][min_values[i]]
            val2 = e['x'][min_values[i + 1]]

            if val1 > val2:
                min_values.pop(i + 1)
            else:
                min_values.pop(i)
        else:
            i += 1
    
    return min_values


# Find the period
def find_period(experiment):
    max_values = find_max_values(experiment)
    max_values = max_values[2::]

    period = []
    for i in range(1, len(max_values)):
        period.append(experiment['t'][max_values[i]] - experiment['t'][max_values[i - 1]])
    return period
