from postcards.postcards import Postcards
from postcards.plugin_pexels.util.pexels import get_random_image_url, read_from_url
import sys
import json
import os
import random
import nltk
from datetime import date

birthday_location = os.path.dirname(os.path.realpath(__file__)) + '/birthdays.json'


class PostcardsBirthdays(Postcards):
    """
    Send a postcard if its somebody's birthday today.

    """

    def enhance_send_subparser(self, parser):
        parser.add_argument('--days-ahead', default=None, type=str,
                            help='number of days ahead of birthday card should be sent')

    def get_img_text_recipient(self, payload, cli_args):

        birthdays_info = self._read_birthdays()
        birthdays=birthday_inof.get("birthdays")
        wishes = birthday_info.get("wishes")

        text = random.choice(wishes)

        if cli_args.days_ahead:
            days_ahead = cli_args.days_ahead

        url = get_random_image_url(keyword="birthday")

        birthday_entry = _get_first_birthday_entry(birthdays)

        if not birthday_entry:
            print(" nobody's birthday")
            self.logger.error("today is nobody's birthday")
            exit(1)

        return {
            'img': read_from_url(url),
            'text': postcard_text,
            'recipient': birthday_entry.get("recipient")
        }

    @staticmethod
    def _read_birthday_info():
        with open(birthdays_location, 'r') as f:
            birthdays = json.loads(f)
            return birthdays
    @staticmethod
    def _get_first_birthday_entry(birthdays):
        for birthday_entry in birthday:
            birthdate=birthday_entry.get('birthdate')
            if _is_today_this_date(birthdate):
                return birthday_entry

    @staticmethod
    def _is_today_this_date(date):
        today = str(date.today())
        return date == today



def main():
    PostcardsBirthdays().main(sys.argv[1:])


if __name__ == '__main__':
    main()
