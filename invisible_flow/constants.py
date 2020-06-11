FOIA_RESPONSE_FIELD_NAME = 'foia_response'

JOB_DB_BIND_KEY = 'jobdb'
COPA_DB_BIND_KEY = 'copadb'
VALID_STATUSES = ['STARTED', 'COMPLETED - SUCCESSFUL', 'COMPLETED - ERROR']

SCRAPE_URL = 'https://data.cityofchicago.org/resource/mft5-nfa8'
VALID_BEATS = [111, 112, 113, 114, 121, 122, 123, 124, 131, 132, 133,
               211, 212, 213, 214, 215, 221, 222, 223, 224, 225, 231,
               232, 233, 234, 235, 311, 312, 313, 314, 321, 322, 323,
               324, 331, 332, 333, 334, 411, 412, 413, 414, 421, 422,
               423, 424, 431, 432, 433, 434, 511, 512, 513, 522, 523,
               524, 531, 532, 533, 611, 612, 613, 614, 621, 622, 623,
               624, 631, 632, 633, 634, 711, 712, 713, 714, 715, 722,
               723, 724, 725, 726, 731, 732, 733, 734, 735, 811, 812,
               813, 814, 815, 821, 822, 823, 824, 825, 831, 832, 833,
               834, 835, 911, 912, 913, 914, 915, 921, 922, 923, 924,
               925, 931, 932, 933, 934, 935, 1011, 1012, 1013, 1014, 1021,
               1022, 1023, 1024, 1031, 1032, 1033, 1034, 1111, 1112, 1113, 1114,
               1115, 1121, 1122, 1123, 1124, 1125, 1131, 1132, 1133, 1134, 1135,
               1211, 1212, 1213, 1214, 1215, 1221, 1222, 1223, 1224, 1225, 1231,
               1232, 1233, 1234, 1235, 1411, 1412, 1413, 1414, 1421, 1422, 1423,
               1424, 1431, 1432, 1433, 1434, 1511, 1512, 1513, 1522, 1523, 1524,
               1531, 1532, 1533, 1611, 1612, 1613, 1614, 1621, 1622, 1623, 1624,
               1631, 1632, 1633, 1634, 1651, 1652, 1653, 1654, 1655, 1711, 1712,
               1713, 1722, 1723, 1724, 1731, 1732, 1733, 1811, 1812, 1813, 1814,
               1821, 1822, 1823, 1824, 1831, 1832, 1833, 1834, 1911, 1912, 1913,
               1914, 1915, 1921, 1922, 1923, 1924, 1925, 1931, 1932, 1933, 1934,
               1935, 2011, 2012, 2013, 2022, 2023, 2024, 2031, 2032, 2033, 2211,
               2212, 2213, 2221, 2222, 2223, 2232, 2233, 2234, 2411, 2412, 2413,
               2422, 2423, 2424, 2431, 2432, 2433, 2511, 2512, 2513, 2514, 2515,
               2521, 2522, 2523, 2524, 2525, 2531, 2532, 2533, 2534, 2535, 3100]

RACE_MAPPER = {
    "White": "White",
    "Unknown": "Unknown",
    "Black or African American": "Black",
    "Hispanic, Latino, or Spanish Origin": "Hispanic",
    "Asian or Pacific Islander": "Asian/Pacific",
    "Middle Eastern or North African": "Middle Eastern or North African",
    "American Indian or Alaska Native": "Native American/Alaskan Native"
}
