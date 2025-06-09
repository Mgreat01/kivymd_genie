from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd_cards.base_card import BaseCard
from kivy.core.window import Window # Optional: for setting window size

class CardDemoApp(MDApp):
    def build(self):
        # Optional: Set a window size for better viewing on desktop
        Window.size = (400, 600)

        root_screen = MDScreen()

        # Main layout to center cards
        main_layout = MDBoxLayout(
            orientation='vertical',
            adaptive_height=True,
            spacing='20dp',
            padding='20dp',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        # Set size_hint_x to None and width to a specific value if you want to constrain card width
        # main_layout.size_hint_x = None
        # main_layout.width = "300dp"


        # Card 1
        card1 = BaseCard()
        card1.update_content(title_text="Card 1", content_text="This is the first animated card.")
        # You might want to set a specific size for the card if adaptive_height in layout is tricky
        # card1.size_hint_y = None
        # card1.height = "150dp"


        # Card 2
        card2 = BaseCard(
            # You can also set properties directly
            # orientation="vertical", # Already default in BaseCard
            # size_hint_y=None, # Already default in BaseCard
            # height="180dp" # Example of setting height
        )
        card2.update_content(title_text="Another Card", content_text="KivyMD makes card creation easy.\nWith animations!")

        main_layout.add_widget(card1)
        main_layout.add_widget(card2)

        root_screen.add_widget(main_layout)

        return root_screen

if __name__ == '__main__':
    CardDemoApp().run()
