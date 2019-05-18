import matplotlib.pyplot as plt
import numpy as np
import json
from matplotlib.widgets import CheckButtons

with open('database_profit.json') as f:
    database = json.load(f)

with open('gdps.json') as f:
    gdp_info = json.load(f)

found_years = {'DIS': 1962, 'MGM': 1990, 'TWX': 1992, 'FOX': 1987,
               'UVV': 1988, 'LGF': 1998, 'NFLX': 2002, 'DRH': 2005}


def build_stock_gdp():
    axes = []
    for comp in found_years:
        x = np.arange(found_years[comp], 2019)
        if comp == 'LGF':
            x = np.arange(found_years[comp], 2017)
        lst = []
        for el in database:
            if database[el][1][comp] is not None:
                lst.append(database[el][1][comp])
        y = np.array(lst)
        axes.extend([x, y])

    lst = []
    x = np.arange(1962, 2019)
    for el in gdp_info:
        if int(el) >= 1962:
            lst.append(gdp_info[el]/100)
    y = np.array(lst)
    axes.extend([x, y])

    fig, ax = plt.subplots()
    l1, = plt.plot(axes[0], axes[1], linestyle='solid')
    l2, = plt.plot(axes[2], axes[3],  linestyle='solid')
    l3, = plt.plot(axes[4], axes[5],  linestyle='solid')
    l4, = plt.plot(axes[6], axes[7], linestyle='solid')
    l5, = plt.plot(axes[8], axes[9], linestyle='solid')
    l6, = plt.plot(axes[10], axes[11], linestyle='solid')
    l7, = plt.plot(axes[12], axes[13],  linestyle='solid')
    l8, = plt.plot(axes[14], axes[15],  linestyle='solid')
    l9, = plt.plot(axes[16], axes[17], linestyle='solid')

    plt.subplots_adjust(left=0.3)
    lgnd = ax.legend(list(found_years.keys()),
                     loc='upper center', ncol=4, fontsize='xx-small', shadow=True)

    lgnd.get_frame().set_facecolor('#ffb19a')

    rax = plt.axes([0.04, 0.5, 0.17, 0.37],
                   facecolor='lightgoldenrodyellow')
    check = CheckButtons(rax, tuple(found_years.keys()), (True,
                                                          True, True, True, True, True, True, True))

    def func(label):
        for line, comp in zip([l1, l2, l3, l4, l5, l6, l7, l8], list(found_years.keys())):
            if label == comp:
                line.set_visible(not line.get_visible())
        plt.draw()

    check.on_clicked(func)

    plt.show()


def build_stock_boxoffice():
    axes = []
    for comp in found_years:
        stock_pr = []
        years_with_rev = []
        box_office = []
        for el in database:
            if database[el][1][comp] is not None:
                if comp == 'NFLX' and int(el) > 2017:
                    continue
                stock_pr.append(database[el][1][comp])
            try:
                if len(database[el][0][comp]) != 0 and int(el) >= found_years[comp]:
                    years_with_rev.append(int(el))
                    box_office.append(
                        round((sum(database[el][0][comp])/len(database[el][0][comp]))/10000000, 2))
            except:
                continue
        x = np.array(
            years_with_rev + years_with_rev[::-1] + list(range(found_years[comp], 2019)))
        if comp == 'LGF':
            x = np.array(years_with_rev + years_with_rev[::-1] +
                         list(range(found_years[comp], 2017)))
        if comp == 'NFLX':
            x = np.array(years_with_rev + years_with_rev[::-1] +
                         list(range(found_years[comp], 2018)))
        y = np.array(box_office + box_office[::-1] + stock_pr)
        axes.extend([x, y])

    fig, ax = plt.subplots()
    l1, = plt.plot(axes[0], axes[1], linestyle='solid')
    l2, = plt.plot(axes[2], axes[3],  linestyle='solid')
    l3, = plt.plot(axes[4], axes[5],  linestyle='solid')
    l4, = plt.plot(axes[6], axes[7], linestyle='solid')
    l5, = plt.plot(axes[8], axes[9], linestyle='solid')
    l6, = plt.plot(axes[10], axes[11], linestyle='solid')
    l7, = plt.plot(axes[12], axes[13],  linestyle='solid')
    l8, = plt.plot(axes[14], axes[15],  linestyle='solid')

    plt.subplots_adjust(left=0.3)
    lgnd = ax.legend(list(found_years.keys()),
                     loc='upper center', ncol=5, fontsize='xx-small', shadow=True)

    lgnd.get_frame().set_facecolor('#ffb19a')

    rax = plt.axes([0.04, 0.5, 0.17, 0.37],
                   facecolor='lightgoldenrodyellow')
    check = CheckButtons(rax, tuple(found_years.keys()), (True,
                                                          True, True, True, True, True, True, True))

    def func(label):
        for line, comp in zip([l1, l2, l3, l4, l5, l6, l7, l8], list(found_years.keys())):
            if label == comp:
                line.set_visible(not line.get_visible())
        plt.draw()

    check.on_clicked(func)

    plt.show()


def build_gdp_boxoffice():
    axes = []
    for comp in found_years:
        x1 = np.arange(found_years[comp], 2019)
        if comp == 'LGF':
            x1 = np.arange(found_years[comp], 2017)
        years_with_rev = []
        box_office = []
        for el in database:
            try:
                if len(database[el][0][comp]) != 0:
                    years_with_rev.append(int(el))
                    box_office.append(
                        round((sum(database[el][0][comp])/len(database[el][0][comp]))/1000000, 2))
            except:
                continue

        x = np.array(years_with_rev)
        y = np.array(box_office)
        axes.extend([x, y])

    lst = []
    x = np.arange(1962, 2019)
    for el in gdp_info:
        if int(el) >= 1962:
            lst.append(gdp_info[el]/10)
    y = np.array(lst)
    axes.extend([x, y])

    fig, ax = plt.subplots()
    l1, = plt.plot(axes[0], axes[1], linestyle='solid')
    l2, = plt.plot(axes[2], axes[3],  linestyle='solid')
    l3, = plt.plot(axes[4], axes[5],  linestyle='solid')
    l4, = plt.plot(axes[6], axes[7], linestyle='solid')
    l5, = plt.plot(axes[8], axes[9], linestyle='solid')
    l6, = plt.plot(axes[10], axes[11], linestyle='solid')
    l7, = plt.plot(axes[12], axes[13],  linestyle='solid')
    l8, = plt.plot(axes[14], axes[15],  linestyle='solid')
    l9, = plt.plot(axes[16], axes[17], linestyle='solid')

    plt.subplots_adjust(left=0.3)
    lgnd = ax.legend(list(found_years.keys()),
                     loc='upper center', ncol=5, fontsize='xx-small', shadow=True)

    lgnd.get_frame().set_facecolor('#ffb19a')

    rax = plt.axes([0.04, 0.5, 0.17, 0.37],
                   facecolor='lightgoldenrodyellow')
    check = CheckButtons(rax, tuple(found_years.keys()), (True,
                                                          True, True, True, True, True, True, True))

    def func(label):
        for line, comp in zip([l1, l2, l3, l4, l5, l6, l7, l8], list(found_years.keys())):
            if label == comp:
                line.set_visible(not line.get_visible())
        plt.draw()

    check.on_clicked(func)

    plt.show()
