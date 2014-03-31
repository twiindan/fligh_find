__author__ = 'artanis'

from configuration import DEPARTURE_MAX, DEPARTURE_MIN, ARRIVAL_MAX, ARRIVAL_MIN, DAYS


days_dict = []

from datetime import date


def calculate_ranges():
    print DEPARTURE_MAX, DEPARTURE_MIN, ARRIVAL_MIN, ARRIVAL_MAX

    for x in range(DEPARTURE_MIN, DEPARTURE_MAX):
        for y in range(ARRIVAL_MIN, ARRIVAL_MAX):
            if daysdifference(str(x), str(y)) >= DAYS:
                days = {'fecha_origen': reorder_dates(x),
                        'fecha_destino': reorder_dates(y)}
                days_dict.append(days)
    return days_dict


def reorder_dates(fecha):
    fecha = str(fecha)
    nueva_fecha = '{}/{}/{}'.format(fecha[-2:], fecha[4:6], fecha[0:4])
    print 'FECHA: {}'.format(fecha)
    print 'NUEVA_FECHA: {}'.format(nueva_fecha)
    return nueva_fecha


def daysdifference(date1, date2):

    d1 = date(int(date1[0:4]), int(date1[4:6]), int(date1[-2:]))
    d2 = date(int(date2[0:4]), int(date2[4:6]), int(date2[-2:]))
    diff = d2 - d1

    return diff.days
