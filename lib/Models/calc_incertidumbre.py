from scipy.stats import linregress

def calc_line_error(obj):
    x_plus = []
    x_minus = []

    y_plus = []
    y_minus = []

    for i in range(obj.num_rows):
        x_plus.append(obj.x[i] + obj.dx)
        x_minus.append(obj.x[i] - obj.dx)

        y_plus.append(obj.y[i] + obj.dy)
        y_minus.append(obj.y[i] - obj.dy)

    obj.dx_plus = x_plus
    obj.dx_minus = x_minus

    obj.dy_plus = y_plus
    obj.dy_minus = y_minus

    regress_plus = linregress(x_plus, y_plus)
    regress_minus = linregress(x_minus, y_minus)

    m_plus = regress_plus.slope
    m_minus = regress_minus.slope

    b_plus = regress_plus.intercept
    b_minus = regress_minus.intercept

    return (abs((m_plus - m_minus) / 2), abs((b_plus - b_minus) / 2))






