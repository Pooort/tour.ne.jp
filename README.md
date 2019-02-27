# Trial test

1. Explore https://www.tour.ne.jp/ and fetch all available Japan (domestic) hotels by using most
fastest and best way to do it using Scrapy engine. (max 2 hours to fetch all into clean database).
Describe the method and explain why did you choose it. Output storage format – MongoDB. Each
hotel should include: hotel name, hotel type, region, prefecture, city, hotel address, geocoordinates,
number of reviews, offers from what additional source are available. (booking, agoda and etc).

**Description.**

Scrapy is the async scraping framework, so it's pretty powerfull in case of performance. We just need to:
a) find a list of items (number of requests depends on items amount in the result)
in best case we can get data just from the list but if we can't we should
b) get data for every item.

So.

Number of requests = number of list requests + number of items

If site has no protection in access we can set big enough amount of CONCURRENT_REQUESTS.

But usually the sites (like this one) has the access protection (by IP for example). So we should make less requests per second. 



If 2 requests per second doesn't blocked. It will be 120 * 60 = 7200 requests per hour. 

There are 13519 items so just with one cuncurrent request without proxies and DOWNLOAD_DELAY = 0.5 it will be < 2 hours.

If this speed isn't enough we should use proxies: 
 * rotating_proxies middleware + ours or public proxies
 * services like stormproxies
 * use layer in docker with proxing
 
Provide the following details when done:

There is a statistic.py file printing this data.

a) Total count of all available hotels found. Arrange the list by region/prefecture.

Total count of all available hotels found: 25855

Arrange the list by prefecture:

[{'_id': '長野県', 'count': 1942},
 {'_id': '京都府', 'count': 1679},
 {'_id': '静岡県', 'count': 1459},
 {'_id': '東京都', 'count': 1343},
 {'_id': '沖縄県-本島', 'count': 945},
 {'_id': '大阪府', 'count': 827},
 {'_id': '兵庫県', 'count': 807},
 {'_id': '神奈川県', 'count': 766},
 {'_id': '新潟県', 'count': 759},
 {'_id': '群馬県', 'count': 703},
 {'_id': '山梨県', 'count': 675},
 {'_id': '千葉県', 'count': 654},
 {'_id': '栃木県', 'count': 614},
 {'_id': '福島県', 'count': 592},
 {'_id': '愛知県', 'count': 592},
 {'_id': '大分県', 'count': 590},
 {'_id': '北海道-道央', 'count': 583},
 {'_id': '岐阜県', 'count': 535},
 {'_id': '鹿児島県', 'count': 512},
 {'_id': '福岡県', 'count': 511},
 {'_id': '熊本県', 'count': 477},
 {'_id': '三重県', 'count': 471},
 {'_id': '石川県', 'count': 457},
 {'_id': '沖縄県-離島', 'count': 415},
 {'_id': '和歌山県', 'count': 377},
 {'_id': '広島県', 'count': 375},
 {'_id': '山形県', 'count': 373},
 {'_id': '宮城県', 'count': 360},
 {'_id': '岩手県', 'count': 348},
 {'_id': '茨城県', 'count': 312},
 {'_id': '長崎県', 'count': 310},
 {'_id': '北海道-道東', 'count': 308},
 {'_id': '福井県', 'count': 307},
 {'_id': '北海道-道北', 'count': 286},
 {'_id': '愛媛県', 'count': 259},
 {'_id': '岡山県', 'count': 255},
 {'_id': '奈良県', 'count': 235},
 {'_id': '滋賀県', 'count': 231},
 {'_id': '香川県', 'count': 230},
 {'_id': '秋田県', 'count': 224},
 {'_id': '青森県', 'count': 223},
 {'_id': '富山県', 'count': 221},
 {'_id': '島根県', 'count': 218},
 {'_id': '埼玉県', 'count': 212},
 {'_id': '山口県', 'count': 210},
 {'_id': '鳥取県', 'count': 209},
 {'_id': '宮崎県', 'count': 201},
 {'_id': '高知県', 'count': 172},
 {'_id': '徳島県', 'count': 171},
 {'_id': '北海道-道南', 'count': 168},
 {'_id': '佐賀県', 'count': 152}]

b) List all available accomodation types (hotel, guesthouse, villa and etc) and total hotels per each
type.

There are just types ids, we could find names in any way.

[{'_id': '1', 'count': 9816},
 {'_id': '3', 'count': 8908},
 {'_id': '2', 'count': 6994},
 {'_id': '4', 'count': 109},
 {'_id': '', 'count': 28}]

2. Every hotel has N number of reviews. You need to update them all daily, but only ones that was
changed in some way (new reviews, hotel gave the response to the guest comment and etc.) That
job should be done within 1 hour no matter how many reviews exist. Best and the fastest way to do
it?

**Answer.**

We need to know how the data is structured to anwser this question (there are no reviews on the current site). 
In theory it could be even one request.
So it will be from 1 to n requests.

3. What does `*args and **kwargs` means in Python?

**Answer.**

*args - contains positional arguments
**kwargs - contains keyword arguments

4. What is the best way to run background job when using Flask?

**Answer.**

Tools like Redis Queue or Celery.

5. What is the reverse proxy?

**Answer.**

Reverse proxy is a type of proxy that stay between client and backend servers, client make a request to the reverse proxy and 
it sends the request to one of the backend servers and the answer to the client. So client doesn't need to know about service
besides reverse proxy. Nginx is the most common.