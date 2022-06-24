import random


class Hat:

    def __init__(self, **kwargs):
        self.dic = kwargs
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, drawn):
        if drawn > len(self.contents):
            sample = random.sample(self.contents, len(self.contents))
        else:
            sample = random.sample(self.contents, drawn)
        return sample

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        expected_occur_list = []
        sample = hat.draw(num_balls_drawn)
        for key in expected_balls.keys():
            expected_occur_list.append(sample.count(key))
        if list(expected_balls.values()) <= expected_occur_list:
            success += 1
    prob = success / num_experiments
    print(prob)

