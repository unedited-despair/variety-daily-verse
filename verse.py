import json
import re

import requests
from variety.plugins.IQuoteSource import IQuoteSource


class DailyVerse(IQuoteSource):
    def __init__(self):
        super(IQuoteSource, self).__init__()

    @classmethod
    def get_info(cls):
        return {
            "name": "bible-api.com's Verse of the Day",
            "description": "A daily word of exultation",
            "author": "Michael Bauer",
            "version": "1.0.1",
        }

    def supports_search(self):
        return True

    @staticmethod
    def get_verse(version):
        response = json.loads(
            requests.get(f"https://bible-api.com/data/{version}/random").content
        )
        v = response["random_verse"]
        text = re.sub(r" +", " ", v["text"])
        return [
            dict(
                quote=text,
                author=f"{v['book']} {v['chapter']}:{v['verse']} ({version.upper()})",
                sourceName="bible-api.com",
                link="https://bible-api.com",
            )
        ]

    def get_random(self):
        return self.get_verse("asv")

    def get_for_author(self, author):
        return self.get_random()

    def get_for_keyword(self, keyword):
        return self.get_random()
