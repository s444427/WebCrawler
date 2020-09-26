from Wikiscraper import *

if __name__ == '__main__':

    wikiscraper = Wikiscraper()
    wikiscraper.link_list.append('Online chat')

    while len(wikiscraper.link_list) > 0:
        try:
            wikiscraper.get_links(wikiscraper.link_list[0])

            print(wikiscraper.visited_links, wikiscraper.link_list)
        except wikipedia.exceptions.PageError:
            pass
