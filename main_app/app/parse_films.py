import datetime
import random
import string
from xml.etree import ElementTree as ET

import matplotlib.pyplot as plt
import pandas as pd
import requests
import seaborn as sns
from sklearn.neural_network import MLPRegressor

url = "http://www.cbr.ru/scripts/XML_dynamic.asp"


def execute(days, theme):
    tb, values = get_charts()
    predicted = predict(values, days)

    i = 1
    for future in predicted[0]:
        tb.append([datetime.datetime.now() + datetime.timedelta(days=i), future, "predicted"])
        i = i + 1
    data = pd.DataFrame(tb, columns=("date", "value", "source"))

    imgpath = draw(data, theme)
    return imgpath


def get_charts():
    # Get data
    params = {
        "date_req1": (datetime.datetime.now() - datetime.timedelta(days=90)).strftime("%d/%m/%Y"),
        "date_req2": datetime.datetime.now().strftime("%d/%m/%Y"),
        "VAL_NM_RQ": "R01239"  # R01239 is the ID for the rub/eur
    }
    response = requests.get(url, params=params)
    response_xml = response.text
    rates = ET.fromstring(response_xml)
    values = []
    tb = []

    for record in rates.findall("Record"):
        # Select data
        date = record.attrib["Date"]
        value = record.find("Value").text

        # Clean up data
        value = float(value.replace(",", "."))
        date = datetime.datetime.strptime(date, "%d.%m.%Y")

        # Append data
        values.append(value)
        tb.append([date, value, "actual"])

    return tb, values


def predict(values, days):
    if days % 2 == 0:
        days = days - 1
    divider = days
    tb = []
    past_col = []
    futr_col = []

    for i in range(divider, len(values) - divider):
        t = (values[(i - divider):(i + divider)])
        tb.append(list(t))

    for i in range(divider):
        past_col.append(f'past_{i}')
        futr_col.append(f'futr_{i}')

    data = pd.DataFrame(tb, columns=(past_col + futr_col))

    k = int(len(data[past_col]) / 2 + 1)
    # Test data
    X = data[past_col][:-k]
    Y = data[futr_col][:-k]
    # Train data
    Xt = data[past_col][-k:]
    Yt = data[futr_col][-k:]

    MLP = MLPRegressor(hidden_layer_sizes=(150, 100, 50), max_iter=1000, random_state=42)
    MLP.fit(X, Y)

    prediction = MLP.predict(Xt)
    return prediction[0],


def draw(data, theme):
    sns.set(style="darkgrid")
    if theme == "dark":
        plt.style.use("dark_background")
    else:
        plt.style.use("default")
    f, axes = plt.subplots(figsize=(10, 5))
    ax = sns.lineplot(x="date", y="value", data=data, hue="source", palette="Set1", ax=axes)
    ax.set_title("Exchange rates")
    name = id_generator(48) + ".png"
    plt.savefig(name)
    return name


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))



