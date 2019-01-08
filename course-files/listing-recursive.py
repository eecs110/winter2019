""" Build index from directory listing

make_index.py </path/to/directory> [--header <header text>]
"""
from __future__ import print_function
import os.path, time

INDEX_TEMPLATE = r"""---
layout: default
nav_order: 4
title: ${title}
nav_exclude: ${exclude}
---

# ${title}

[${header}](.)

<table class="tbl-files">
    <tbody>
        <tr>
            <th valign="top"></th>
            <th>Name</th>
            <th>Last modified</th>
            <th>Size</th>
            <th>Preview</th>
        </tr>
        <tr>
            <td valign="top"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAmlJREFUeNpsU0toU0EUPfPysx/tTxuDH9SCWhUDooIbd7oRUUTMouqi2iIoCO6lceHWhegy4EJFinWjrlQUpVm0IIoFpVDEIthm0dpikpf3ZuZ6Z94nrXhhMjM3c8895977BBHB2PznK8WPtDgyWH5q77cPH8PpdXuhpQT4ifR9u5sfJb1bmw6VivahATDrxcRZ2njfoaMv+2j7mLDn93MPiNRMvGbL18L9IpF8h9/TN+EYkMffSiOXJ5+hkD+PdqcLpICWHOHc2CC+LEyA/K+cKQMnlQHJX8wqYG3MAJy88Wa4OLDvEqAEOpJd0LxHIMdHBziowSwVlF8D6QaicK01krw/JynwcKoEwZczewroTvZirlKJs5CqQ5CG8pb57FnJUA0LYCXMX5fibd+p8LWDDemcPZbzQyjvH+Ki1TlIciElA7ghwLKV4kRZstt2sANWRjYTAGzuP2hXZFpJ/GsxgGJ0ox1aoFWsDXyyxqCs26+ydmagFN/rRjymJ1898bzGzmQE0HCZpmk5A0RFIv8Pn0WYPsiu6t/Rsj6PauVTwffTSzGAGZhUG2F06hEc9ibS7OPMNp6ErYFlKavo7MkhmTqCxZ/jwzGA9Hx82H2BZSw1NTN9Gx8ycHkajU/7M+jInsDC7DiaEmo1bNl1AMr9ASFgqVu9MCTIzoGUimXVAnnaN0PdBBDCCYbEtMk6wkpQwIG0sn0PQIUF4GsTwLSIFKNqF6DVrQq+IWVrQDxAYQC/1SsYOI4pOxKZrfifiUSbDUisif7XlpGIPufXd/uvdvZm760M0no1FZcnrzUdjw7au3vu/BVgAFLXeuTxhTXVAAAAAElFTkSuQmCC "
                alt="[PARENTDIR]"></td>
            <td><a href="../">Parent Directory</a></td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>

        % for dir in dirnames:
        <tr>
            <td valign="top"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAd5JREFUeNqMU79rFUEQ/vbuodFEEkzAImBpkUabFP4ldpaJhZXYm/RiZWsv/hkWFglBUyTIgyAIIfgIRjHv3r39MePM7N3LcbxAFvZ2b2bn22/mm3XMjF+HL3YW7q28YSIw8mBKoBihhhgCsoORot9d3/ywg3YowMXwNde/PzGnk2vn6PitrT+/PGeNaecg4+qNY3D43vy16A5wDDd4Aqg/ngmrjl/GoN0U5V1QquHQG3q+TPDVhVwyBffcmQGJmSVfyZk7R3SngI4JKfwDJ2+05zIg8gbiereTZRHhJ5KCMOwDFLjhoBTn2g0ghagfKeIYJDPFyibJVBtTREwq60SpYvh5++PpwatHsxSm9QRLSQpEVSd7/TYJUb49TX7gztpjjEffnoVw66+Ytovs14Yp7HaKmUXeX9rKUoMoLNW3srqI5fWn8JejrVkK0QcrkFLOgS39yoKUQe292WJ1guUHG8K2o8K00oO1BTvXoW4yasclUTgZYJY9aFNfAThX5CZRmczAV52oAPoupHhWRIUUAOoyUIlYVaAa/VbLbyiZUiyFbjQFNwiZQSGl4IDy9sO5Wrty0QLKhdZPxmgGcDo8ejn+c/6eiK9poz15Kw7Dr/vN/z6W7q++091/AQYA5mZ8GYJ9K0AAAAAASUVORK5CYII= "
                alt="[DIR]"></td>
            <td><a href="${dir['name']}">${dir['name']}</a></td>
            <td align="right">${dir['time']}</td>
            <td>${dir['size']}</td>
            <td>&nbsp;</td>
        </tr>
        % endfor
        % for f in filenames:
        <tr class="click-to-preview">
            <td>
                % if f['name'].find('.py') != -1:
                <i class="fab fa-lg fa-python"></i>
                % elif f['name'].find('.ipynb') != -1:
                    <img class="icon-jupyter" src="{{ site.baseurl }}/assets/images/jupyter-icon.png" />
                % else:
                <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAABnRSTlMAAAAAAABupgeRAAABHUlEQVR42o2RMW7DIBiF3498iHRJD5JKHurL+CRVBp+i2T16tTynF2gO0KSb5ZrBBl4HHDBuK/WXACH4eO9/CAAAbdvijzLGNE1TVZXfZuHg6XCAQESAZXbOKaXO57eiKG6ft9PrKQIkCQqFoIiQFBGlFIB5nvM8t9aOX2Nd18oDzjnPgCDpn/BH4zh2XZdlWVmWiUK4IgCBoFMUz9eP6zRN75cLgEQhcmTQIbl72O0f9865qLAAsURAAgKBJKEtgLXWvyjLuFsThCSstb8rBCaAQhDYWgIZ7myM+TUBjDHrHlZcbMYYk34cN0YSLcgS+wL0fe9TXDMbY33fR2AYBvyQ8L0Gk8MwREBrTfKe4TpTzwhArXWi8HI84h/1DfwI5mhxJamFAAAAAElFTkSuQmCC " alt="[DIR]">
                % endif
            </td>
            <td nowrap>
                % if f['name'].endswith('md'):
                    <a href="${f['name'].replace('.md', '')}">
                        ${f['name'].replace('.md', '').title()}
                    </a>
                % else:
                    <a href="${f['name']}">${f['name']}</a>
                % endif
            </td>
            <td align="right">${f['time']}</td>
            <td>${f['size']}</td>
            <td>
                % if f['name'].endswith(('py', 'ipynb', 'txt', 'html')):
                    <a href="${github_path}/${header}${f['name']}" 
                        target="_blank"><i class="fab fa-github fa-lg"></i></a>
                % endif
                <!-- a href="${f['name']}"><i class="fas fa-download"></i></a -->
            </td>
        </tr>
        % endfor
    </tbody>
</table>
"""

EXCLUDED = [
    'listing-recursive.py', 
    'notebook-to-script.py',
    'index.html', 
    'index.md', 
    'drafts', 
    '.ipynb_checkpoints', 
    '.DS_Store', 
    'images'
]

import os
import argparse

# May need to do "pip install mako"
from mako.template import Template

def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def get_metadata(dir, filenames):
    metadata = []
    for fname in filenames:
        size = sizeof_fmt(os.path.getsize(dir + fname))
        timestamp = time.strftime('%-m/%-d/%Y %-I:%M %p', time.gmtime(os.path.getmtime(dir + fname)))
        metadata.append({ 
            'name': fname,
            'time': timestamp,
            'size': size
        })
    return metadata

def fun(dir,rootdir, counter):
    print('Processing: ', dir)

    filenames = [fname for fname in sorted(os.listdir(dir))
              if fname not in EXCLUDED and os.path.isfile(dir+fname)]
    dirnames = [fname for fname in sorted(os.listdir(dir))
            if fname not in EXCLUDED]
    dirnames = [fname for fname in dirnames if fname not in filenames]

    file_metadata = get_metadata(dir, filenames)
    dir_metadata = get_metadata(dir, dirnames)
    relative_path = dir.split('course-files')

    f = open(dir+'/index.md','w')
    header = dir
    header = header.replace('./', 'course-files/')
    title = header.split('/')[-2]
    title = title.replace('-', ' ')
    title = title.title()
    kwargs = {
        'dirnames': dir_metadata,
        'filenames': file_metadata, 
        'header': header,
        'ROOTDIR': rootdir,
        'github_path': 'https://github.com/eecs110/winter2019/blob/master',
        'num': counter,
        'title': title,
        'exclude': (not header == 'course-files/')
    }
    print(Template(INDEX_TEMPLATE).render(**kwargs), file=f)
    f.close()
    for subdir in dirnames:
        counter += 1
        try:
            fun(dir+subdir+"/",rootdir+'../', counter)
        except:
            pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument("--header")
    args = parser.parse_args()
    fun(args.directory+'/','../', 1)

if __name__ == '__main__':
    main()