from .calc_incertidumbre import calc_line_error
from scipy.stats import linregress

class DataTable:
    num_rows: int
    num_cols: int
    name: str
    
    x: list[float] = []
    y: list[float] = []

    dx: float = None
    dy: float = None

    dx_plus: list[float] = []
    dx_minus: list[float] = []
    dy_plus: list[float] = []
    dy_minus: list[float] = []

    regress = []

    error = []

    def __init__(self, name: str, x: list[float], y: list[float]):
        self.name = name
        self.x = x
        self.y = y

        self.num_rows = len(x)
        self.num_cols = 2

    def set_d(self, dx: float, dy: float):
        self.dx = dx
        self.dy = dy

    def calc_d(self):
        self.error = calc_line_error(self)

    def calc_linear_regression(self):
        a = linregress(self.x, self.y)

        m = a.slope
        b = a.intercept
        r = a.rvalue ** 2

        self.regress = [m, b, r]




