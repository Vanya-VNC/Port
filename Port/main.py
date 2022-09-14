from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import shuffle


class Container(BoxLayout):
    def Image_press(self):
        global this_card
        self.img.source = card_names[mixed_numbers_cards[this_card]]
        if this_card < len(mixed_numbers_cards) - 1:
            this_card += 1
        else:
            shuffle(mixed_numbers_cards)
            this_card = 0


class PortApp(App):
    def build(self):
        return Container()


card_names = [
    "imgs/2b.jpg", "imgs/2c.jpg",
    "imgs/2k.jpg", "imgs/2p.jpg",
    "imgs/3b.jpg", "imgs/3c.jpg",
    "imgs/3k.jpg", "imgs/3p.jpg",
    "imgs/4b.jpg", "imgs/4c.jpg",
    "imgs/4k.jpg", "imgs/4p.jpg",
    "imgs/5b.jpg", "imgs/5c.jpg",
    "imgs/5k.jpg", "imgs/5p.jpg",
    "imgs/6b.jpg", "imgs/6c.jpg",
    "imgs/6k.jpg", "imgs/6p.jpg",
    "imgs/10b.jpg", "imgs/10c.jpg",
    "imgs/10k.jpg", "imgs/10p.jpg",
    "imgs/qb.jpg", "imgs/qc.jpg",
    "imgs/qk.jpg", "imgs/qp.jpg",
    "imgs/tb.jpg", "imgs/tc.jpg",
    "imgs/tk.jpg", "imgs/tp.jpg",
]
mixed_numbers_cards = []
this_card = 0
for i in range(len(card_names)):
    mixed_numbers_cards.append(i)

shuffle(mixed_numbers_cards)
print(mixed_numbers_cards)


if __name__ == '__main__':
    PortApp().run()
