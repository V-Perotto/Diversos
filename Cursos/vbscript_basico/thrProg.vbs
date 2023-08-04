msgbox(now)
msgbox Day(now),, "dia corrente"
msgbox Hour(now),, "hora corrente sem os minutos"
msgbox Minute(now),, "minuto corrente"
msgbox Second(now),, "Segundo corrente"
msgbox Weekdayname(2, true),, "Hoje e"
msgbox MonthName(10),, "Mes de"

msgbox FormatDateTime(time(), vbShortTime)
msgbox FormatDateTime(Date(), vbLongDate),64