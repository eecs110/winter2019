import helpers

# one template:
template = '''
    <html>
        <head><title>{header}</title></head>
        <body>
            <h1>{header}</h1>
            <p>{summary}</p>
            <img src="{image_url}" />
        </body>
    </html>
'''

# lots of data:
data = [
    {
        'header': 'This is my first page title',
        'image_url': '../sample_files/kittens.jpg',
        'summary': 'This is a very cute photo of a kitten'
    },{
        'header': 'This is my second page title',
        'image_url': '../sample_files/kittens.jpg',
        'summary': 'This is a very cute photo of a kitten'
    },{
        'header': 'This is my third page title',
        'image_url': '../sample_files/kittens.jpg',
        'summary': 'This is a very cute photo of a kitten'
    },{
        'header': 'This is my fourth page title',
        'image_url': '../sample_files/kittens.jpg',
        'summary': 'This is a very cute photo of a kitten'
    },{
        'header': 'This is my fifth page title',
        'image_url': '../sample_files/kittens.jpg',
        'summary': 'This is a very cute photo of a kitten'
    }
]

# generate an HTML file for each item in the list
counter = 1
for item in data:
    html_text = template.format(**item)
    file_path = helpers.get_file_path('cat_page_{0}.html'.format(counter), subdirectory='results')
    f = open(file_path, 'w')
    f.write(html_text)
    f.close()
    counter += 1