import re

def parse_wishlist(wished_gifts):
    pattern = re.compile(r'\(([\d.]+)\)\s*([^[]+)\s*\[(\d+)\s*(?:\s*\D*)?\]\s*((?:(?:\s*-|\s*\*\s*)(?:.*?)(?=\n[-*\n]|$))*)', re.DOTALL)
    wishlists_found = pattern.findall(wished_gifts)
    parsed_information = []
    for wishlist_information in wishlists_found:
        niceness, name, age, gifts_list = wishlist_information
        niceness = float(niceness.strip())
        name = str(name.strip())
        age = int(age.strip())

        gifts = re.split(r'\s*\-\s*(?!\S)', gifts_list)
        new_gifts = []
        for gift in gifts:
            collection = re.split(r'\s*\*\s*(?!\S)', gift)
            for element in collection:
                new_gifts.append(element)
                
        valid_gifts = []
        for gift in new_gifts:
            if gift != "":
                valid_gifts.append(gift.strip())
        parsed_information.append((niceness, name, age, tuple(valid_gifts)))
    return parsed_information