import numpy as np

class SPSOctupoles(object):

    def __init__(self, optics='Q20'):
        if optics == 'Q20':
            self.coeffs = {
                'daxx_f': 1205.698449,
                'daxy_f': -847.9317337,
                'dayy_f': 149.1236132,
                'daxx_d': 144.5327317,
                'daxy_d': -815.9641992,
                'dayy_d': 1151.951103,
                'd_q2x_f': 2898.820363,
                'd_q2y_f': -1019.595679,
                'd_q2x_d': 398.0100862,
                'd_q2y_d': -1124.794026 }
        elif optics == 'Q26':
            self.coeffs = {
                'daxx_f': 1156.693205,
                'daxy_f': -553.9169211,
                'dayy_f': 66.34457277,
                'daxx_d': 63.94645202,
                'daxy_d': -532.3795391,
                'dayy_d': 1108.526017,
                'd_q2x_f': 390.7589796,
                'd_q2y_f': -93.41756217,
                'd_q2x_d': 25.02161632,
                'd_q2y_d': -104.1276824 }        
        else:
            raise ValueError("Optics %s unknown! Use either 'Q20' or 'Q26'."%
                             optics)
            
    def get_anharmonicities(self, KLOF, KLOD):
        axx = self.coeffs['daxx_f'] * KLOF + self.coeffs['daxx_d'] * KLOD
        axy = self.coeffs['daxy_f'] * KLOF + self.coeffs['daxy_d'] * KLOD
        ayy = self.coeffs['dayy_f'] * KLOF + self.coeffs['dayy_d'] * KLOD

        return axx, axy, ayy

    def get_q2(self, KLOF, KLOD):
        q2x = self.coeffs['d_q2x_f'] * KLOF + self.coeffs['d_q2x_d'] * KLOD
        q2y = self.coeffs['d_q2y_f'] * KLOF + self.coeffs['d_q2y_d'] * KLOD

        return q2x, q2y

    def get_q1_feeddown(self, KLOF, KLOD, dp_offset=-1.7e-4):
        q2x, q2y = self.get_q2(KLOF, KLOD)
        q1x_fd = q2x * dp_offset
        q1y_fd = q2y * dp_offset

        return q1x_fd, q1y_fd