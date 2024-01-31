class Effect:

    def __init__(self, name, function):
        self.name = name
        self.function = function
        self.intensity = 1

    def __call__(self, argument_of_function):
        if self.intensity == 0:
            raise TypeError("Effect is depleted.")
        else:
            for _ in range(self.intensity):
                self.function(argument_of_function)


class Potion:

    def __init__(self, effects, duration):
        self.effects = dict()
        self.duration = duration
        self.is_potion_used = False
        for name, function in effects.items():
            if name in self.effects.keys():
                self.effects[name].intensity += 1
            else:
                self.effects[name] = Effect(name, function)
        for name, effect in self.effects.items():
            setattr(self, name, effect)

    def __add__(self, other_potion):
        new_duration = max(self.duration, other_potion.duration)
        new_potion = Potion(self.effects, new_duration)
        for name, effect in other_potion.effects.items():
            if name in new_potion.effects.keys():
                new_potion.effects[name].intensity += effect.intensity
            else:
                new_potion.effects[name] = Effect(name, effect.function)
                new_potion.effects[name].intensity = effect.intensity
        return new_potion
    
    def __mul__(self, intensity):
        #potentiation
        if isinstance(intensity, int) and intensity >= 1:
            new_potion = Potion(self.effects, self.duration)
            for name, effect in self.effects.items():
                new_potion.effects[name].intensity *= intensity
            return new_potion
        #dilution
        elif isinstance(intensity, float) and intensity > 0 and intensity < 1:
            new_potion = Potion(self.effects, self.duration)
            for name, effect in new_potion.effects.items():
                current_result = effect.intensity * intensity
                if current_result.is_integer():
                    new_potion.effects[name].intensity = current_result
                else:
                    current_result_fractional_part = current_result % 1
                    if current_result_fractional_part <= 0.5:
                        new_potion.effects[name].intensity = int(current_result // 1)
                    else:
                        new_potion.effects[name].intensity = int(current_result // 1 + 1)
            return new_potion

    def __sub__(self, other_potion):
        for name, effect in other_potion.effects.items():
            if name not in self.effects.keys():
                raise TypeError("Invalid purification")
        new_potion = Potion(self.effects,self.duration)
        for name, effect in self.effects.items():
            if name in other_potion.effects.keys():
                current_intensity = self.effects[name].intensity - other_potion.effects[name].intensity
                if current_intensity <= 0:
                    del new_potion.effects[name]
                else:
                    new_potion.effects[name].intensity = current_intensity
        return new_potion
    
    # didn't quite understand this one
    def __truediv__(self, parts):
        new_collections = tuple(Potion(self.effects, self.duration) for _ in range(parts))
        return new_collections
    
    def __eq__(self, other_potion):
        return self.effects == other_potion.effects and self.duration == other_potion.duration
    
    def __lt__(self, other_potion):
        first_flask_intensity = 0
        second_flask_intensity = 0
        for name, effect in self.effects.items():
            first_flask_intensity += effect.intensity
        for name, effect in other_potion.effects.items():
            second_flask_intensity += effect.intensity
        return first_flask_intensity < second_flask_intensity
    
    def __gt__(self, other_potion):
        first_flask_intensity = 0
        second_flask_intensity = 0
        for name, effect in self.effects.items():
            first_flask_intensity += effect.intensity
        for name, effect in other_potion.effects.items():
            second_flask_intensity += effect.intensity
        return first_flask_intensity > second_flask_intensity
    

class ГоспожатаПоХимия:
    def __init__(self):
        self.name = "Димитричка, обаче настояват да я наричат Диди"
        self.applied_potions = []

    def apply(self, target, potion):
        if potion.is_potion_used:
            raise TypeError("Potion is depleted.")
        if potion in self.applied_potions:
            raise TypeError("Potion is now part of something bigger than itself.") 
        sorted_effects = sorted(potion.effects.values(), key=lambda effect: sum(map(ord, effect.name)), reverse=True)
        for effect in sorted_effects:
            effect(target)
        self.applied_potions.append(potion)
        potion.is_potion_used = True

    def tick(self):
        for potion in self.applied_potions:
            potion.duration -= 1
            if potion.duration <= 0:
                self.applied_potions.remove(potion)