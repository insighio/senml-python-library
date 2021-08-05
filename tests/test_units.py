#!/usr/bin/env python
# -*- coding: utf-8 -*-


import kpn_senml


def test_enums():
    assert kpn_senml.SenmlUnits.SENML_UNIT_METER == "m"
    assert kpn_senml.SenmlUnits.SENML_UNIT_KILOGRAM == "kg"
    assert kpn_senml.SenmlUnits.SENML_UNIT_GRAM == "g"
    assert kpn_senml.SenmlUnits.SENML_UNIT_SECOND == "s"
    assert kpn_senml.SenmlUnits.SENML_UNIT_AMPERE == "A"
    assert kpn_senml.SenmlUnits.SENML_UNIT_KELVIN == "K"
    assert kpn_senml.SenmlUnits.SENML_UNIT_CANDELA == "cd"
    assert kpn_senml.SenmlUnits.SENML_UNIT_MOLE == "mol"
    assert kpn_senml.SenmlUnits.SENML_UNIT_HERTZ == "Hz"
    assert kpn_senml.SenmlUnits.SENML_UNIT_RADIAN == "rad"
    assert kpn_senml.SenmlUnits.SENML_UNIT_STERADIAN == "sr"
    assert kpn_senml.SenmlUnits.SENML_UNIT_NEWTON == "N"
    assert kpn_senml.SenmlUnits.SENML_UNIT_PASCAL == "Pa"
    assert kpn_senml.SenmlUnits.SENML_UNIT_JOULE == "J"
    assert kpn_senml.SenmlUnits.SENML_UNIT_WATT == "W"
    assert kpn_senml.SenmlUnits.SENML_UNIT_COULOMB == "C"
    assert kpn_senml.SenmlUnits.SENML_UNIT_VOLT == "V"
    assert kpn_senml.SenmlUnits.SENML_UNIT_FARAD == "F"
    assert kpn_senml.SenmlUnits.SENML_UNIT_OHM == "Ohm"
    assert kpn_senml.SenmlUnits.SENML_UNIT_SIEMENS == "S"
    assert kpn_senml.SenmlUnits.SENML_UNIT_WEBER == "Wb"
    assert kpn_senml.SenmlUnits.SENML_UNIT_TESLA == "T"
    assert kpn_senml.SenmlUnits.SENML_UNIT_HENRY == "H"
    assert kpn_senml.SenmlUnits.SENML_UNIT_DEGREES_CELSIUS == "Cel"
    assert kpn_senml.SenmlUnits.SENML_UNIT_LUMEN == "lm"
    assert kpn_senml.SenmlUnits.SENML_UNIT_LUX == "lx"
    assert kpn_senml.SenmlUnits.SENML_UNIT_BECQUEREL == "Bq"
    assert kpn_senml.SenmlUnits.SENML_UNIT_GRAY == "Gy"
    assert kpn_senml.SenmlUnits.SENML_UNIT_SIEVERT == "Sv"
    assert kpn_senml.SenmlUnits.SENML_UNIT_KATAL == "kat"
    assert kpn_senml.SenmlUnits.SENML_UNIT_SQUARE_METER == "m2"
    assert kpn_senml.SenmlUnits.SENML_UNIT_CUBIC_METER == "m3"
    assert kpn_senml.SenmlUnits.SENML_UNIT_LITER == "l"
    assert kpn_senml.SenmlUnits.SENML_UNIT_VELOCITY == "m/s"
    assert kpn_senml.SenmlUnits.SENML_UNIT_ACCELERATION == "m/s2"
    assert kpn_senml.SenmlUnits.SENML_UNIT_CUBIC_METER_PER_SECOND == "m3/s"
    assert kpn_senml.SenmlUnits.SENML_UNIT_LITER_PER_SECOND == "l/s"
    assert kpn_senml.SenmlUnits.SENML_UNIT_WATT_PER_SQUARE_METER == "W/m2"
    assert kpn_senml.SenmlUnits.SENML_UNIT_CANDELA_PER_SQUARE_METER == "cd/m2"
    assert kpn_senml.SenmlUnits.SENML_UNIT_BIT == "bit"
    assert kpn_senml.SenmlUnits.SENML_UNIT_BIT_PER_SECOND == "bit/s"
    assert kpn_senml.SenmlUnits.SENML_UNIT_DEGREES_LATITUDE == "lat"
    assert kpn_senml.SenmlUnits.SENML_UNIT_DEGREES_LONGITUDE == "lon"
    assert kpn_senml.SenmlUnits.SENML_UNIT_PH == "pH"
    assert kpn_senml.SenmlUnits.SENML_UNIT_DECIBEL == "dB"
    assert kpn_senml.SenmlUnits.SENML_UNIT_DECIBEL_RELATIVE_TO_1_W == "dBW"
    assert kpn_senml.SenmlUnits.SENML_UNIT_BEL == "Bspl"
    assert kpn_senml.SenmlUnits.SENML_UNIT_COUNTER == "count"
    assert kpn_senml.SenmlUnits.SENML_UNIT_RATIO == "//"
    assert kpn_senml.SenmlUnits.SENML_UNIT_RELATIVE_HUMIDITY == "%RH"
    assert kpn_senml.SenmlUnits.SENML_UNIT_PERCENTAGE_REMAINING_BATTERY_LEVEL == "%EL"
    assert kpn_senml.SenmlUnits.SENML_UNIT_SECONDS_REMAINING_BATTERY_LEVEL == "EL"
    assert kpn_senml.SenmlUnits.SENML_UNIT_EVENT_RATE_PER_SECOND == "1/s"
    assert kpn_senml.SenmlUnits.SENML_UNIT_EVENT_RATE_PER_MINUTE == "1/min"
    assert kpn_senml.SenmlUnits.SENML_UNIT_BPM == "beat/min"
    assert kpn_senml.SenmlUnits.SENML_UNIT_BEATS == "beats"
    assert kpn_senml.SenmlUnits.SENML_UNIT_SIEMENS_PER_METER == "S/m"
