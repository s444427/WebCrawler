import wikipedia


class Wikiscraper:
    def __init__(self):
        self.link_list = []
        self.visited_links = []

    def get_links(self, title: str):
        if title not in self.visited_links:
            search = wikipedia.page(title)

            html = search.html()

            place_see = html.find('<span class="mw-headline" id="See_also">See also</span>')
            place_ref = html.find('<span class="mw-headline" id="References">References</span>')

            html = html[place_see: place_ref - 9]

            if html.find('<li>') > 0:
                html = html.split('<li>')[1:]

                for item in html:
                    item = item[item.find(' title="')+8:]
                    parser = item.find('"')
                    item = item[:parser]

                    if item not in self.link_list and item not in self.visited_links:
                        self.link_list.append(item)

            self.visited_links.append(title)
            self.link_list.pop(0)
