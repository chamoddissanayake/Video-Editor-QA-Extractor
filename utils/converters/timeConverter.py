def timeConverterDecimalToString(secondsValueInDecimal):
    hours = secondsValueInDecimal // (60 * 60)
    secondsValueInDecimal %= (60 * 60)
    minutes = secondsValueInDecimal // 60
    secondsValueInDecimal %= 60

    timeInHHMMSS_format = str(hours)+":"+str(minutes)+":"+str(int(secondsValueInDecimal))
    return timeInHHMMSS_format
