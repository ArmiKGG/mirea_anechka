import scipy


def calc(first, second):
    result = []
    if first % 2 != 0:
        result.append(first)
    if second % 2 != 0:
        result.append(second)

    scipy_array = scipy.array(result)

    return scipy_array


class Summator:
    def __init__(self, a, b):
        self.first = a
        self.second = b
        self.head = """
            <head>
            <style>
            .list6a {
                padding:0;
                list-style: none;
            }
            .list6a li{
                padding:6px;
            }
            .list6a li:before {
                padding-right:10px;
                font-weight: bold;
                color: #77AEDB;
                content: "🌠";
                transition-duration: 0.5s;
            }
            .list6a li:hover:before {
                color: #337AB7;
                content: "✨";
            }
            li {
                font-size: 65px;
            }
            </style>
            </head>"""
        self.constructor = '<ul class="list6a">{}</ul>'

    def getOdd(self):
        first_is_odd = True if self.first % 2 != 0 else False
        second_is_odd = True if self.second % 2 != 0 else False
        if all([first_is_odd, second_is_odd]):
            return self.head + self.constructor.format(f"<li>Odd numbers</li> <li>{self.first}</li> <li>{self.second}</li>")

        elif first_is_odd:
            return self.head + self.constructor.format(f"<li>Odd numbers</li> <li>{self.first}</li>")

        elif second_is_odd:
            return self.head + self.constructor.format(f"<li>Odd numbers</li> <li>{self.second}</li>")

        else:
            return self.head + self.constructor.format(f"<li>None of this integers are ODD</li>")

