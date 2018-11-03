import pytest


class FormulaTokenizer:
    pass


class Formula:

    def __init__(self, *args):
        pass

    @classmethod
    def from_string(cls, *args):
        return Formula(*args)

    def eval(self, **kwargs):
        pass


@pytest.mark.parametrize(
    'formula, inputs, result',
    [
        ('C0 * x + 10', dict(x=1.0, C0=2.0), 12.0),
        ('sin(x) + 2 * cos(x)', dict(x=0.7), 2.1739021),
        ('log(x) + 3', dict(x=2.71828182846), 4.0),
        pytest.param('hypos(x, y)', dict(x=3, y=4), 5.0,
                     marks=pytest.mark.xfail(reason='not implemented: #102')),
        pytest.param('x + 3', dict(x=1.0), 4.0, id='add'),  # pytest -k "add"
        pytest.param('x - 1', dict(x=6.0), 5.0, id='sub'),
    ]
)
def test_formula_parsing(formula, inputs, result):
    tokenizer = FormulaTokenizer()
    formula = Formula.from_string(formula, tokenizer)
    assert formula.eval(**inputs) == pytest.approx(result)
