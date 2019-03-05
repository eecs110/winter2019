import bs4
import helpers

# What methods are available for a list?
helpers.print_title('Lists')
a = [1, 2, 3]
print(a)
print(type(a))
print(dir(a))

# What methods are available for a dictionary?
helpers.print_title('Dictionaries')
b = {'a': 1, 'b': 2, 'c': 3}
print(b)
print(type(b))
print(dir(b))


# What methods are available in the Beautiful Soup module?
helpers.print_title('Beautiful Soup')
soup = bs4.BeautifulSoup('''
<html>
    <head>
        <title>Webpage Title</title>
    </head>
    <body>
        <h1>Webpage header</h1>
        <p>Hello world!</p>
    </body>
</html>
''', features='lxml')
print(soup)
print(type(soup))
print(dir(soup))