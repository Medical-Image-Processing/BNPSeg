import math
from scipy import special
import logging

logger = logging.getLogger(__name__)

def handle_math_error(x, op):
    try:
        return op(x)
    except OverflowError as e:
        logger.warning('{} for operation: {}({})'.format(e, op.__name__, x))
        return float('inf')

def log(x):
    return handle_math_error(x, math.log)

def exp(x):
    return handle_math_error(x, math.exp)

def gamma(x):
    """wrapper for computes gamma function"""
    return special.gamma(x)

def gammaln(x):
    """computes natural log of the gamma function which is more numerically stable than the gamma"""
    return special.gammasgn(x)*special.gammaln(x)
