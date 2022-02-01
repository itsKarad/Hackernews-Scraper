import scrapy
import json

PAGINATION_MAX_INDEX = 3

HN_POSTS = []


class QuotesSpider(scrapy.Spider):

    name = "hacker-news"

    def start_requests(self):
        for i in range(1, PAGINATION_MAX_INDEX):
            yield scrapy.Request(
                url="https://news.ycombinator.com/news?p={}".format(i),
                callback=self.parse,
            )

    # Method to parse the response
    def parse(self, response):
        posts = response.css("tr.athing")
        posts_subtext = response.css("td.subtext")

        for post, post_subtext in zip(posts, posts_subtext):
            post_link = post.css("td.title a.titlelink::attr(href)").get() or "N/A"
            post_title = post.css("td.title a.titlelink::text").get() or "N/A"
            post_rank = post.css("td.title span.rank::text").get() or "N/A"
            post_points = post_subtext.css(".score::text").get() or "N/A"
            post_author = post_subtext.css(".hnuser::text").get() or "N/A"

            yield {
                "post_rank": post_rank,
                "post_title": post_title,
                "post_link": post_link,
                "post_points": post_points,
                "post_author": post_author,
            }

            new_post = {post_rank, post_title, post_link, post_points, post_author}
            HN_POSTS.append(new_post)

        # If you want to custom-format
        # with open("hackernews-data.txt", "w") as f:
        #     f.write(str(HN_POSTS))
