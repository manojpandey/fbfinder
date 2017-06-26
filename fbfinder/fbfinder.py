#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author: @manojpandey
# Last modified: Jun 26, 2017 20:31:06

from bs4 import BeautifulSoup
import requests
import sys
import argparse

class FbFinder:

    @staticmethod
    def find_id(url):
        '''Returns the facebook user ID taking the profile URL as the input

        :url: of the form "https://www.facebook.com/someusername"
        '''
        # Check if the url is valid
        try:
            response = requests.get(url)
            if response.status_code == 200 and \
                response.cookies.list_domains()[0] == ".facebook.com":
                # url is vaid and from facebook domain

                # Check if we have the id in the string itself
                # so that we don't have to parse the page
                # Ex: https://www.facebook.com/profile.php?id=24353623

                if 'php' in url:
                    return url.split('/')[-1].split('?')[-1].split(
                        '=')[1].split('&')[0]

                # If we don't find the id in the url, we'll have to find manually
                else:
                    webpage = response.content
                    # Create a BeautifulSoup object
                    soup = BeautifulSoup(webpage, "lxml")
                    # First place to check
                    title_url = soup.find("meta",  property="al:android:url")
                    try:
                        user_id = title_url["content"].split('/')[-1]
                        return user_id
                    except TypeError:
                        title_url = soup.find("meta",  property="al:android:url")
                        try:
                            user_id = title_url["content"].split('/')[-1]
                            return user_id
                        except TypeError:
                            return "Unable to figure out, contact the developer"
            elif response.status_code == 404:
                return "Wrong URL. Check again"
        except requests.exceptions.RequestException:
            return "Invalid URL"


def main():
    '''Main program
    '''
    # Use argparse with mutual exclusion of arguments;
    # As we need only one of the two to use at a time
    parser = argparse.ArgumentParser(description='Description of your program')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-u', '--url', help='facebook url')
    group.add_argument('--id', help='facebook username')
    args = parser.parse_args()
    # If user handle is given
    if args.id is not None:
        base_url = "https://facebook.com/"
        build_url = base_url + args.id
        print("ID:", FbFinder.find_id(build_url))

    # otherwise, it must be a URL to the profile
    else:
        print("ID:", FbFinder.find_id(args.url))

if __name__ == '__main__':
    main()
