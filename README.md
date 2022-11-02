# Crawler4Pixiv
A Pixiv Crawler (Spider) with 20 methods to collect Pixiv illustrations can be deployed on Windows or Linux OS.

## Usage

Before you use it, remember to do the following two steps:

1. Requirement (Python3)

- gzip

(Yes, gzip is the only required package)



2. Set config.py

```python
savePath = 'D:/pixiv/'
userID = ''
cookie = ''
```

- Change savePath if you want

- Enter your Pixiv id, which can be found on your Pixiv homepage: 

![image](https://github.com/Yuzi-Liang/Crawler4Pixiv/blob/main/image/1.png)

- Enter your cookie (remember to log in to your Pixiv account when you get the cookie)

  a particular cookie looks like that:
  ![image](https://github.com/Yuzi-Liang/Crawler4Pixiv/blob/main/image/2.png)

  Mosaiced most of the content for privacy



Then run main.py



## Functions

1. Author id:
Download illustrations of a specific author, the author ID should be a string of numbers
2. Illustration id:
Download specific illustration using its ID
3. Daily rank:
Download daily rank for today
4. Daily rank R18:
Download R18 daily rank for today
5. Weekly rank:
Download weekly rank for today
6. Weekly rank R18:
Download R18 weekly rank for today
7. Monthly rank:
Download monthly rank for today
8. Daily male rank:
Download daily male rank
9. Daily male rank R18:
Download R18 daily male rank
10. Daily female rank:
Download daily female rank
11. Daily female rank R18:
Download R18 daily female rank
12. Tag:
Download illustrations with specific tags (sort by time by default)
13. Followed Author in public:
Download public following author's illustrations, when downloading each author's work, need to enter the number of images you need to download
14. Followed Author in private:
Download private following author's illustrations, when downloading each author's work, need to enter the number of images you need to download
15. Followed Author in public without asking:
Download public following author's illustrations
16. Followed Author in private without asking:
Download private following author's illustrations
17. Repair by illustration id:

18. Update illustrations of followed author in public:

19. Update illustrations of followed author in private:

20. Tag & sort:
Download illustrations with specific tags and sort these images by a particular parameter (Views, Bookmarks, or Likes)
