from main import build_stock_gdp, build_stock_boxoffice, build_gdp_boxoffice


def print_beginning():
    print('Hello, this is our research that shows dependance between')
    print('economic state in the USA and success of cinematography.')
    print('There are three parameteres we have analyzed:')
    print(' - GDP in USA')
    print(' - stock prices of eight different companies')
    print(' - box offices of their movies')
    print('We have modeled three graphics for you to visualize our results.')
    print('Enter 1 to see graphic of stock price - box office')
    print('Enter 2 to see graphic of stock price - GDP')
    print('Enter 3 to see graphic of box office - GDP')
    print('Enter exit to close the programm')


def choose_func(num):
    if num == '1':
        build_stock_boxoffice()
    if num == '2':
        build_stock_gdp()
    if num == '3':
        build_gdp_boxoffice()


def main():
    print_beginning()
    num = ''
    while num != 'exit':
        num = input('\nPlease enter graphic number: ')
        choose_func(num)


if __name__ == '__main__':
    main()
