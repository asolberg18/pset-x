import uuid
import random
from datetime import datetime


class LogEvent:

    logged = 0
    countries = ['VI', 'EG', 'US', 'UK',
                 'CN', 'CA', 'DE', 'MX', 'FR', 'BR']
    browsers = ['Chrome', 'Safari', 'IE', 'Firefox', 'Edge']
    os = ['Mac', 'Android', 'Linux', 'IOS', 'windows']
    resp_codes = [501, 100, 200, 201,
                  303, 411, 403, 406, 507, 208, 426]

    schema = {
        "mappings": {
            "properties": {
                "browser": {
                    "type": "keyword"
                },
                "eventTime": {
                    "type": "date"
                },
                "logID": {
                    "type": "text"
                },
                "responseCode": {
                    "type": "integer"
                },
                "ttfb": {
                    "type": "float"
                },
                "ua_country": {
                    "type": "keyword"
                },
                "ua_os": {
                    "type": "text"
                },
                "url": {
                    "type": "keyword"
                },
                "userId": {
                    "type": "text"
                },
                "location": {
                    "type": "geo_point"
                }
            }
        }
    }

    def __init__(self, logID, eventTime, url, ua_country, userId, browser, ua_os, responseCode, ttfb, location):
        self.logID = logID
        self.eventTime = eventTime
        self.url = url
        self.ua_country = ua_country
        self.userId = userId
        self.browser = browser
        self.ua_os = ua_os
        self.responseCode = responseCode
        self.ttfb = ttfb
        self.location = location

    async def log(self, logger, silent=True):
        await logger(self.__dict__, silent=silent)
        LogEvent.logged += 1

    @staticmethod
    def CreateTimestamp(mask):
        y = datetime.today().year + random.randint(-5,
                                                   5) if mask['y'] == '?' else mask['y']
        m = random.randint(1, 12) if mask['m'] == '?' else mask['m']
        d = random.randint(1, 31) if mask['d'] == '?' else mask['d']
        if m == 2 and d > 28:
            d -= 3
        elif m in [9, 4, 6, 11] and d == 31:
            d = 30
        H = random.randint(0, 23) if mask['H'] == '?' else mask['H']
        M = random.randint(0, 59) if mask['M'] == '?' else mask['M']
        S = random.randint(0, 59) if mask['S'] == '?' else mask['S']
        return "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(y, m, d, H, M, S)

    @staticmethod
    def ParseTimestampMask(ts_str):
        t = ts_str.split('T')
        t = t if len(t) == 2 else ts_str.split(' ')
        if len(t) != 2:
            raise ValueError()
        if t[0].lower() == 'today':
            t[0] = datetime.today().strftime('%Y-%m-%d')
        if t[1].lower() == 'now':
            t[1] = datetime.today().strftime('%H:%M:%S')
        ymd = t[0].split('-')
        hms = t[1].split(':')
        if len(ymd) != 3 or len(hms) != 3:
            raise ValueError()
        ymd = [x if x == '?' else int(x) for x in ymd]
        hms = [x if x == '?' else int(x) for x in hms]
        if not ((ymd[0] == '?' or len(str(ymd[0])) == 4) and
                (ymd[1] == '?' or (ymd[1] >= 1 and ymd[1] <= 12)) and
                (ymd[2] == '?' or (ymd[2] >= 1 and ymd[2] <= 31)) and
                (hms[0] == '?' or (hms[0] >= 0 and hms[0] <= 23)) and
                (hms[1] == '?' or (hms[1] >= 0 and hms[1] <= 59)) and
                (hms[2] == '?' or (hms[2] >= 0 and hms[2] <= 59))):
            raise ValueError()
        ts = {'y': ymd[0], 'm': ymd[1], 'd': ymd[2],
              'H': hms[0], 'M': hms[1], 'S': hms[2]}
        return ts

    @staticmethod
    def random_event(ts_mask, countries=countries, browsers=browsers, os=os, resp_codes=resp_codes):
        return LogEvent(
            logID=str(uuid.uuid4()),
            eventTime=LogEvent.CreateTimestamp(ts_mask),
            url="http://example.com/?url={:03d}".format(random.randint(0, 15)),
            ua_country=countries[random.randint(0, len(countries)-1)],
            userId="user{:03d}".format(random.randint(1, 15)),
            browser=browsers[random.randint(0, len(browsers)-1)],
            ua_os=os[random.randint(0, len(os)-1)],
            responseCode=resp_codes[random.randint(
                0, len(resp_codes)-1)],
            ttfb=float(round(random.uniform(0.4, 10.6), 2)),
            location={'lat': round(random.uniform(-90.0, 90.0), 5),
                      'lon': round(random.uniform(-180.0, 180.0), 5)}
        )
