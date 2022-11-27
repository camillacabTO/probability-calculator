import copy
import random

# Consider using the modules imported above.


class Hat:

    def __init__(self, **balls):
        self.balls = balls
        self.contents = list()
        self.set_contents()

    def set_contents(self):
        self.contents.clear()
        for color, number in self.balls.items():
            for _ in range(number):
                self.contents.append(color)

    def draw(self, balls_to_draw):
        self.set_contents()
        balls_picked = list()

        if len(self.contents) <= balls_to_draw:
            return self.contents

        for _ in range(balls_to_draw):
            ball = random.randint(0, len(self.contents) - 1)
            balls_picked.append(self.contents[ball])
            self.contents.pop(ball)
        return balls_picked


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    won = 0
    for _ in range(num_experiments):

        balls_drawn_list = hat.draw(num_balls_drawn)
        balls_drawn_dict = dict()

        for ball in balls_drawn_list:
            balls_drawn_dict[ball] = balls_drawn_dict.get(ball, 0) + 1

        # print('drawn dict', balls_drawn_dict)

        all_in = False
        for key, value in expected_balls.items():
            if key in balls_drawn_dict:
                # print(f'key {key} in dic')
                if balls_drawn_dict[key] >= value:
                    # print(f'value {value} of {key} in dic')
                    all_in = True
                    # print(all_in)
                else:
                    all_in = False
                    # print(all_in)
                    # print(f'value {value} of {key} less than in dic')
                    break

            else:
                # print(f'key {key} not in dic')
                all_in = False
                # print(all_in)
                break

        if all_in:
            won = won + 1
            # print('won', won)

    # print('prob', won / num_experiments)
    return won / num_experiments
