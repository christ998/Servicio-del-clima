# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.3
#
# <auto-generated>
#
# Generated from file `meteorologia.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Meteorologia
_M_Meteorologia = Ice.openModule('Meteorologia')
__name__ = 'Meteorologia'

if 'MedicionDia' not in _M_Meteorologia.__dict__:
    _M_Meteorologia.MedicionDia = Ice.createTempClass()
    class MedicionDia(object):
        def __init__(self, dia='', text='', tempMin='', tempMax='', humedad='', viento='', vientoDireccion=''):
            self.dia = dia
            self.text = text
            self.tempMin = tempMin
            self.tempMax = tempMax
            self.humedad = humedad
            self.viento = viento
            self.vientoDireccion = vientoDireccion

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.dia)
            _h = 5 * _h + Ice.getHash(self.text)
            _h = 5 * _h + Ice.getHash(self.tempMin)
            _h = 5 * _h + Ice.getHash(self.tempMax)
            _h = 5 * _h + Ice.getHash(self.humedad)
            _h = 5 * _h + Ice.getHash(self.viento)
            _h = 5 * _h + Ice.getHash(self.vientoDireccion)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_Meteorologia.MedicionDia):
                return NotImplemented
            else:
                if self.dia is None or other.dia is None:
                    if self.dia != other.dia:
                        return (-1 if self.dia is None else 1)
                else:
                    if self.dia < other.dia:
                        return -1
                    elif self.dia > other.dia:
                        return 1
                if self.text is None or other.text is None:
                    if self.text != other.text:
                        return (-1 if self.text is None else 1)
                else:
                    if self.text < other.text:
                        return -1
                    elif self.text > other.text:
                        return 1
                if self.tempMin is None or other.tempMin is None:
                    if self.tempMin != other.tempMin:
                        return (-1 if self.tempMin is None else 1)
                else:
                    if self.tempMin < other.tempMin:
                        return -1
                    elif self.tempMin > other.tempMin:
                        return 1
                if self.tempMax is None or other.tempMax is None:
                    if self.tempMax != other.tempMax:
                        return (-1 if self.tempMax is None else 1)
                else:
                    if self.tempMax < other.tempMax:
                        return -1
                    elif self.tempMax > other.tempMax:
                        return 1
                if self.humedad is None or other.humedad is None:
                    if self.humedad != other.humedad:
                        return (-1 if self.humedad is None else 1)
                else:
                    if self.humedad < other.humedad:
                        return -1
                    elif self.humedad > other.humedad:
                        return 1
                if self.viento is None or other.viento is None:
                    if self.viento != other.viento:
                        return (-1 if self.viento is None else 1)
                else:
                    if self.viento < other.viento:
                        return -1
                    elif self.viento > other.viento:
                        return 1
                if self.vientoDireccion is None or other.vientoDireccion is None:
                    if self.vientoDireccion != other.vientoDireccion:
                        return (-1 if self.vientoDireccion is None else 1)
                else:
                    if self.vientoDireccion < other.vientoDireccion:
                        return -1
                    elif self.vientoDireccion > other.vientoDireccion:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_Meteorologia._t_MedicionDia)

        __repr__ = __str__

    _M_Meteorologia._t_MedicionDia = IcePy.defineStruct('::Meteorologia::MedicionDia', MedicionDia, (), (
        ('dia', (), IcePy._t_string),
        ('text', (), IcePy._t_string),
        ('tempMin', (), IcePy._t_string),
        ('tempMax', (), IcePy._t_string),
        ('humedad', (), IcePy._t_string),
        ('viento', (), IcePy._t_string),
        ('vientoDireccion', (), IcePy._t_string)
    ))

    _M_Meteorologia.MedicionDia = MedicionDia
    del MedicionDia

if 'MedicionHora' not in _M_Meteorologia.__dict__:
    _M_Meteorologia.MedicionHora = Ice.createTempClass()
    class MedicionHora(object):
        def __init__(self, dia='', hora='', temp='', text='', humedad='', viento='', vientoDireccion=''):
            self.dia = dia
            self.hora = hora
            self.temp = temp
            self.text = text
            self.humedad = humedad
            self.viento = viento
            self.vientoDireccion = vientoDireccion

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.dia)
            _h = 5 * _h + Ice.getHash(self.hora)
            _h = 5 * _h + Ice.getHash(self.temp)
            _h = 5 * _h + Ice.getHash(self.text)
            _h = 5 * _h + Ice.getHash(self.humedad)
            _h = 5 * _h + Ice.getHash(self.viento)
            _h = 5 * _h + Ice.getHash(self.vientoDireccion)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_Meteorologia.MedicionHora):
                return NotImplemented
            else:
                if self.dia is None or other.dia is None:
                    if self.dia != other.dia:
                        return (-1 if self.dia is None else 1)
                else:
                    if self.dia < other.dia:
                        return -1
                    elif self.dia > other.dia:
                        return 1
                if self.hora is None or other.hora is None:
                    if self.hora != other.hora:
                        return (-1 if self.hora is None else 1)
                else:
                    if self.hora < other.hora:
                        return -1
                    elif self.hora > other.hora:
                        return 1
                if self.temp is None or other.temp is None:
                    if self.temp != other.temp:
                        return (-1 if self.temp is None else 1)
                else:
                    if self.temp < other.temp:
                        return -1
                    elif self.temp > other.temp:
                        return 1
                if self.text is None or other.text is None:
                    if self.text != other.text:
                        return (-1 if self.text is None else 1)
                else:
                    if self.text < other.text:
                        return -1
                    elif self.text > other.text:
                        return 1
                if self.humedad is None or other.humedad is None:
                    if self.humedad != other.humedad:
                        return (-1 if self.humedad is None else 1)
                else:
                    if self.humedad < other.humedad:
                        return -1
                    elif self.humedad > other.humedad:
                        return 1
                if self.viento is None or other.viento is None:
                    if self.viento != other.viento:
                        return (-1 if self.viento is None else 1)
                else:
                    if self.viento < other.viento:
                        return -1
                    elif self.viento > other.viento:
                        return 1
                if self.vientoDireccion is None or other.vientoDireccion is None:
                    if self.vientoDireccion != other.vientoDireccion:
                        return (-1 if self.vientoDireccion is None else 1)
                else:
                    if self.vientoDireccion < other.vientoDireccion:
                        return -1
                    elif self.vientoDireccion > other.vientoDireccion:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_Meteorologia._t_MedicionHora)

        __repr__ = __str__

    _M_Meteorologia._t_MedicionHora = IcePy.defineStruct('::Meteorologia::MedicionHora', MedicionHora, (), (
        ('dia', (), IcePy._t_string),
        ('hora', (), IcePy._t_string),
        ('temp', (), IcePy._t_string),
        ('text', (), IcePy._t_string),
        ('humedad', (), IcePy._t_string),
        ('viento', (), IcePy._t_string),
        ('vientoDireccion', (), IcePy._t_string)
    ))

    _M_Meteorologia.MedicionHora = MedicionHora
    del MedicionHora

if '_t_Mediciones' not in _M_Meteorologia.__dict__:
    _M_Meteorologia._t_Mediciones = IcePy.defineSequence('::Meteorologia::Mediciones', (), _M_Meteorologia._t_MedicionDia)

if '_t_MedicionesHora' not in _M_Meteorologia.__dict__:
    _M_Meteorologia._t_MedicionesHora = IcePy.defineSequence('::Meteorologia::MedicionesHora', (), _M_Meteorologia._t_MedicionHora)

_M_Meteorologia._t_Conexion = IcePy.defineValue('::Meteorologia::Conexion', Ice.Value, -1, (), False, True, None, ())

if 'ConexionPrx' not in _M_Meteorologia.__dict__:
    _M_Meteorologia.ConexionPrx = Ice.createTempClass()
    class ConexionPrx(Ice.ObjectPrx):

        def reporteSemanal(self, ciudad, context=None):
            return _M_Meteorologia.Conexion._op_reporteSemanal.invoke(self, ((ciudad, ), context))

        def reporteSemanalAsync(self, ciudad, context=None):
            return _M_Meteorologia.Conexion._op_reporteSemanal.invokeAsync(self, ((ciudad, ), context))

        def begin_reporteSemanal(self, ciudad, _response=None, _ex=None, _sent=None, context=None):
            return _M_Meteorologia.Conexion._op_reporteSemanal.begin(self, ((ciudad, ), _response, _ex, _sent, context))

        def end_reporteSemanal(self, _r):
            return _M_Meteorologia.Conexion._op_reporteSemanal.end(self, _r)

        def reportePorHora(self, ciudad, context=None):
            return _M_Meteorologia.Conexion._op_reportePorHora.invoke(self, ((ciudad, ), context))

        def reportePorHoraAsync(self, ciudad, context=None):
            return _M_Meteorologia.Conexion._op_reportePorHora.invokeAsync(self, ((ciudad, ), context))

        def begin_reportePorHora(self, ciudad, _response=None, _ex=None, _sent=None, context=None):
            return _M_Meteorologia.Conexion._op_reportePorHora.begin(self, ((ciudad, ), _response, _ex, _sent, context))

        def end_reportePorHora(self, _r):
            return _M_Meteorologia.Conexion._op_reportePorHora.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Meteorologia.ConexionPrx.ice_checkedCast(proxy, '::Meteorologia::Conexion', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Meteorologia.ConexionPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Meteorologia::Conexion'
    _M_Meteorologia._t_ConexionPrx = IcePy.defineProxy('::Meteorologia::Conexion', ConexionPrx)

    _M_Meteorologia.ConexionPrx = ConexionPrx
    del ConexionPrx

    _M_Meteorologia.Conexion = Ice.createTempClass()
    class Conexion(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::Meteorologia::Conexion')

        def ice_id(self, current=None):
            return '::Meteorologia::Conexion'

        @staticmethod
        def ice_staticId():
            return '::Meteorologia::Conexion'

        def reporteSemanal(self, ciudad, current=None):
            raise NotImplementedError("servant method 'reporteSemanal' not implemented")

        def reportePorHora(self, ciudad, current=None):
            raise NotImplementedError("servant method 'reportePorHora' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Meteorologia._t_ConexionDisp)

        __repr__ = __str__

    _M_Meteorologia._t_ConexionDisp = IcePy.defineClass('::Meteorologia::Conexion', Conexion, (), None, ())
    Conexion._ice_type = _M_Meteorologia._t_ConexionDisp

    Conexion._op_reporteSemanal = IcePy.Operation('reporteSemanal', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Meteorologia._t_Mediciones, False, 0), ())
    Conexion._op_reportePorHora = IcePy.Operation('reportePorHora', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), ((), _M_Meteorologia._t_MedicionesHora, False, 0), ())

    _M_Meteorologia.Conexion = Conexion
    del Conexion

# End of module Meteorologia
