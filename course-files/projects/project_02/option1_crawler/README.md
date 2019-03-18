---
layout: default
title: Homework 5
nav_exclude: True
---

# P2: SEARCH ENGINE PROJECT
For the Web Crawler / Search Engine project, please follow [the instructions in the Google Doc](https://docs.google.com/document/d/1-uZyL8kPUBDn8vJTSnQfi5DTW9jT4rULZmUKl-vSMpc/edit?usp=sharing).


## Resources & Tips
We have also compiled a list of resources to help you complete the project:

### 1. Database Functionality
For database tips, refer to Lecture 13 and specifically:
1. [How to insert a row to a table](https://github.com/eecs110/winter2019/blob/master/course-files/lectures/lecture_13/scripts/12_insert.py)
2. [How to update a row in a table](https://github.com/eecs110/winter2019/blob/master/course-files/lectures/lecture_13/scripts/13_update.py)
3. How to querying by keyword<br>Take a look at these links:
  * [https://www.w3schools.com/sql/sql_like.asp](https://www.w3schools.com/sql/sql_like.asp)
  * [https://stackoverflow.com/questions/3498844/sqlite-string-contains-other-string-query](https://stackoverflow.com/questions/3498844/sqlite-string-contains-other-string-query)

### 2. HTML
Take a look at the HTML sample files from [Lecture 16](https://eecs110.github.io/winter2019/course-files/lectures/lecture_16/sample_files/).

### 3. Errors
Sometimes the URL you're trying to crawl doesn't exist or doesn't have any content. If this is the case, your soup variable will be empty (e.g. soup is None will be True). If this happens, then just ignore the url and move onto the next one.