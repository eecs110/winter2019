import helpers

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

html_text = template.format(
    header='This is my page title',
    image_url='../sample_files/kittens.jpg',
    summary='This is a very cute photo of a kitten'
)

file_path = helpers.get_file_path('cat_page.html', subdirectory='results')
f = open(file_path, 'w')
f.write(html_text)
f.close()