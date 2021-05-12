import pprint
import re

# text = '''[Data        ] [INFO    ] [2021-05-04 14:05:43.834]$$ C) M: 1547, Ave: 4641.000 -> OFF
# [Data        ] [INFO    ] [2021-05-04 14:05:43.866]$$ A) M: 1711, Ave: 5133.000 -> OFF
# [Data        ] [INFO    ] [2021-05-04 14:05:44.202]$$ C) M: 1547, Ave: 4641.000 -> OFF
# [Data        ] [INFO    ] [2021-05-04 14:05:44.233]$$ A) M: 1711, Ave: 5133.000 -> OFF
# [Data        ] [INFO    ] [2021-05-04 14:05:44.249]$$
# [Data        ] [INFO    ] [2021-05-04 14:05:44.250]$$
# [Data        ] [INFO    ] [2021-05-04 14:05:44.250]$$ Starting...
# [Data        ] [INFO    ] [2021-05-04 14:05:44.251]$$ Temperature: 10 C
# [Data        ] [INFO    ] [2021-05-04 14:05:45.336]$$
# [Data        ] [INFO    ] [2021-05-04 14:05:45.336]$$
# [Data        ] [INFO    ] [2021-05-04 14:05:45.337]$$ Starting...
# [Data        ] [INFO    ] [2021-05-04 14:05:45.352]$$ Temperature: 10 C
# [Data        ] [INFO    ] [2021-05-04 14:05:46.563]$$ C) Calibration Done
# [Data        ] [INFO    ] [2021-05-04 14:05:46.576]$$ C) Freq: 1547
# [Data        ] [INFO    ] [2021-05-04 14:05:46.646]$$ C) Freq: 1547
# [Data        ] [INFO    ] [2021-05-04 14:05:46.658]$$ C) Freq: 1547
# [Data        ] [INFO    ] [2021-05-04 14:05:46.670]$$ C) Sensitivity: 2
# [Data        ] [INFO    ] [2021-05-04 14:05:46.682]$$ C) Freq: 0
# [Data        ] [INFO    ] [2021-05-04 14:05:46.694]$$ C) Cal value: 4641.000
# [Data        ] [INFO    ] [2021-05-04 14:05:46.706]$$ C) Threshold High: 4648.426
# [Data        ] [INFO    ] [2021-05-04 14:05:46.718]$$ C) Threshold Low: 4633.574
# [Data        ] [INFO    ] [2021-05-04 14:05:46.730]$$ C) Threshold High Hyst: 4645.950
# [Data        ] [INFO    ] [2021-05-04 14:05:46.742]$$ C) Threshold Low Hyst: 4636.049
# [Data        ] [INFO    ] [2021-05-04 14:05:46.755]$$ A) Calibration Done
# [Data        ] [INFO    ] [2021-05-04 14:05:46.766]$$ A) Freq: 1711
# [Data        ] [INFO    ] [2021-05-04 14:05:46.778]$$ A) Freq: 1711
# '''


def display_match(match: re.Match):
    if match is None:
        return None
    return '<Match: [[%r]]>, groups=[[%r]]' % (match.group(), match.groups())


text = '[Data        ] [INFO    ] [2021-05-04 14:05:45.337]$$ Starting...\n' \
       '[Data        ] [INFO    ] [2021-05-04 14:05:45.352]$$ Temperature: 10 C'

regex = r'\[Data        \]\s\[\w+\s+\]\s\[(?P<dt>.*)\]\${2}\s([\s\w\d):,.\-\>]{1,5})'

for m in re.finditer(regex, text):
    print(m.group())
    print(m.groups())
    print(m.start())
    print(m.end())


    # print(display_match(m))

# fall = pat.findall(text)
# print(fall)
