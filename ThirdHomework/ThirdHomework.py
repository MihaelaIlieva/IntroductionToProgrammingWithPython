import operator

class Candy():
    def __init__(self, mass, uranium):
        self.mass = mass
        self.uranium = uranium

    def get_uranium_quantity(self):
        return self.mass * self.uranium

    def get_mass(self):
        return self.mass
    

class Person():
    type_of_class = "person"

    def __init__(self, position):
        self.position = position
    
    def get_position(self):
        return self.position
    
    def set_position(self, new_position):
        self.position = new_position
    
    def get_type_of_class(self):
        return self.type_of_class


class Kid(Person):
    type_of_class = "kid"

    def __init__(self, position, initiative):
        super().__init__(position)
        self.initiative = initiative
        self._basket = []
        self._uranium_sum = 0
        self.visited_hosts = []
    
    def get_initiative(self):
        return self.initiative
    
    def add_candy(self, candy):
        self._basket.append(candy)
    
    def is_critical(self):
        self._uranium_sum = 0
        for candy in self._basket:
            self._uranium_sum += candy.get_uranium_quantity()
        return self._uranium_sum > 20
    

class Host(Person):
    type_of_class = "host"
    
    def __init__(self, position, candies):
        super().__init__(position)
        self._basket = []
        self.treated_kids = list()
        self.kids_to_be_treated = list()
        self.candies = candies
        for candy in self.candies:
            self._basket.append(Candy(candy[0], candy[1]))  
    
    def remove_candy(self, function):
        if len(self._basket) == 0:
            return None
        else:
            candy = function(self._basket)
            self._basket.remove(candy)
            return candy
        

class FluxCapacitor():

    def __init__(self, participants):
        self.participants = participants
        self.victims = set()
        self._kids = []
        self._hosts = []

    def split_participants(self):
        for participant in self.participants:
            if participant.get_type_of_class() == "kid":
                self._kids.append(participant)
            else:
                self._hosts.append(participant)

    def give_Candy(self, kid, host):
        max_uranium_candy = 0
        candy_to_give = Candy(0, 0)
        for candy in host._basket:
            if candy.get_uranium_quantity() > max_uranium_candy:
                max_uranium_candy = candy.get_uranium_quantity()
                candy_to_give = candy       
        if len(host._basket) > 0:
            kid.add_candy(candy_to_give)
            host._basket.remove(candy_to_give)
    
    def take_initiative(self, kid):
        return kid.get_initiative()
    
    def order_kids(self, kids, host):
        kids.sort(key = self.take_initiative, reverse = True)
        return kids

    def get_distance(self, kid, host):
        (x_kid, y_kid) = kid.get_position()
        (x_host, y_host) = host.get_position()
        return abs(x_kid - x_host) + abs(y_kid - y_host)

    def get_nearest_nonvisited_host(self, kid, visited_hosts):
        all_distances = dict()

        for host in self._hosts:
            if host not in visited_hosts:
                current_distance = self.get_distance(kid, host)
                all_distances[host] = current_distance
        if len(all_distances) != 0:
            sorted_distances_to_hosts = sorted(all_distances.items(), key = operator.itemgetter(1))
            min_distance = sorted_distances_to_hosts[0][1]
            nearest_hosts = [host for host, distance in sorted_distances_to_hosts if distance == min_distance]
            if len(nearest_hosts) == 1:
                return nearest_hosts[0]
            else:
                sorted_hosts = sorted(nearest_hosts, key = lambda x: (x.get_position()[0], x.get_position()[1]))
                return sorted_hosts[0]
        return None

    def set_kid_to_be_treated_by_host(self, kid, host):
        kid.visited_hosts.append(host)
        host.treated_kids.append(kid)
        host.kids_to_be_treated.append(kid)    
        kid.set_position(host.get_position())

    def get_victim(self):
        self.split_participants()
        kids_that_have_visited_everyone = set()
        hosts_that_have_treated_everyone = set()

        while(len(self.victims) == 0):
            for kid in self._kids:
                if len(kid.visited_hosts) == len(self._hosts):
                    kids_that_have_visited_everyone.add(kid)
                nearest_host = self.get_nearest_nonvisited_host(kid, kid.visited_hosts)
                if nearest_host != None:
                    self.set_kid_to_be_treated_by_host(kid, nearest_host)

            for host in self._hosts:
                if len(host.treated_kids) == len(self._kids):
                    hosts_that_have_treated_everyone.add(host)
                ordered_kids = self.order_kids(host.kids_to_be_treated, host)

                for kid in ordered_kids:
                    self.give_Candy(kid, host)
                    if kid.is_critical():
                        self.victims.add(kid)
                host.kids_to_be_treated = list()

            if len(self.victims) != 0:
                break
            if len(kids_that_have_visited_everyone) == len(self._kids) and len(hosts_that_have_treated_everyone) == len(self._hosts):
                break
                
        if len(self.victims) != 0:
            return self.victims
        else:
            return None