""" Build index from directory listing

make_index.py </path/to/directory> [--header <header text>]
"""
from __future__ import print_function
import os.path, datetime, time
from excluded import EXCLUDED

INDEX_TEMPLATE = r"""---
layout: default
title: ${title}
% if is_root:
has_children: true
nav_order: 3
% elif not exclude:
parent: Course Files
nav_order: ${num}
% endif
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
            <td valign="top">
                <i class="fa fa-folder-open"></i>
            </td>
            <td><a href="../">Parent Directory</a></td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
        </tr>

        % for dir in dirnames:
        <tr>
            <td valign="top">
                <i class="fa fa-folder"></i>
            </td>
            <td><a href="${dir['name']}">${dir['name']}</a></td>
            <td align="right">${dir['time']}</td>
            <td>${dir['size']}</td>
            <td>&nbsp;</td>
        </tr>
        % endfor
        % for f in filenames:
        <tr class="click-to-preview">
            <td class="first-column">
                % if f['name'].endswith('.py'):
                    <i class="fab fa-lg fa-python"></i>
                % elif f['name'].endswith('.ipynb'):
                    <img class="icon-jupyter" src="{{ site.baseurl }}/assets/images/jupyter-icon.png" />
                % elif f['name'].endswith('.db'):
                    <i class="fas fa-database"></i>
                % elif f['name'].endswith('.zip'):
                    <i class="far fa-file-archive"></i>
                % else:
                    <i class="far fa-file"></i>
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

def get_timestamp(f):
    timestamp = time.ctime(os.path.getmtime(f))
    timestamp_datetime = datetime.datetime.strptime(timestamp, "%a %b %d %H:%M:%S %Y")
    return timestamp_datetime.strftime('%-m/%-d/%Y %-I:%M %p')

def get_metadata(dir, filenames):
    metadata = []
    for fname in filenames:
        size = sizeof_fmt(os.path.getsize(dir + fname))
        timestamp = get_timestamp(dir + fname)
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
    filenames.sort()
    print(dirnames)
    dirnames.sort()
    print(dirnames)
    file_metadata = get_metadata(dir, filenames)
    dir_metadata = get_metadata(dir, dirnames)

    f = open(dir+'/index.md','w')
    header = dir
    header = header.replace('.././', 'course-files/')
    # print(header)
    title = header.split('/')[-2]
    title = title.replace('-', ' ')
    title = title.replace('_', ' ')
    title = title.title()
    do_exclude = not header in [
        'course-files/',
        'course-files/lectures/',
        'course-files/homework/',
        'course-files/tutorials/',
        'course-files/projects/',
        'course-files/practice_exams/'
    ]
    is_root = header == 'course-files/'
    kwargs = {
        'dirnames': dir_metadata,
        'filenames': file_metadata, 
        'header': header,
        'ROOTDIR': rootdir,
        'github_path': 'https://github.com/eecs110/winter2019/blob/master',
        'num': counter,
        'title': title,
        'exclude': do_exclude,
        'is_root': is_root
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