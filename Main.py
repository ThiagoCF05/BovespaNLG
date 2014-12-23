import Crawler.Crawling
import NLG.ContentSelection

__author__ = 'thiagocastroferreira'

if __name__ == '__main__':
    shares = Crawler.Crawling.run()

    keys = sorted(shares.keys())

    for key in keys:
        shares[key] = sorted(shares[key], key=lambda p: p.date)

        while len(shares[key]) > 0:
            # print shares[key]
            currentHour = shares[key][0].date.hour
            filtered_shares = [share for share in shares[key] if share.date.hour == currentHour]
            shares[key] = [share for share in shares[key] if share.date.hour != currentHour]

            if 'filtered_old_shares' not in locals():
                filtered_old_shares = []
            messages = NLG.ContentSelection.run(sorted(filtered_shares, key=lambda p: p.date), sorted(filtered_old_shares, key=lambda p: p.date))
            filtered_old_shares = filtered_shares

            print str(filtered_shares[0].date)
            print messages
            print 10 * "-"