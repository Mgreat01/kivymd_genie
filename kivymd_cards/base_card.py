from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.uix.behaviors import ScaleBehavior

class BaseCard(MDCard, ScaleBehavior):
    def __init__(self, title_text="Title", content_text="Content", **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.ripple_behavior = True # Ensure ripple effect is enabled
        self.scale_value_x = 1.0
        self.scale_value_y = 1.0
        self.opacity = 0 # Start fully transparent for entry animation
        self.size_hint_y = None
        self.height = "200dp"  # Default height, can be adjusted

        # Store normal shadow properties
        self.elevation_normal = self.elevation
        self.shadow_softness_normal = self.shadow_softness
        self._mouse_over = False # Keep track of mouse over state


        # Layout for card content
        card_layout = BoxLayout(orientation='vertical', padding="10dp", spacing="10dp")

        # Title Label
        self.title_label = MDLabel(
            text=title_text,
            halign="center",
            theme_text_color="Primary",
            font_style="H6"
        )
        card_layout.add_widget(self.title_label)

        # Content Label
        self.content_label = MDLabel(
            text=content_text,
            halign="left",
            theme_text_color="Secondary"
        )
        card_layout.add_widget(self.content_label)

        self.add_widget(card_layout)
        Window.bind(mouse_pos=self.on_mouse_pos)

    def on_mouse_pos(self, window, pos):
        if not self.get_root_window():
            return # Widget is not displayed
        # Check if mouse is over the widget
        if self.collide_point(*self.to_widget(*pos)):
            if not self._mouse_over:
                self.on_enter()
                self._mouse_over = True
        else:
            if self._mouse_over:
                self.on_leave()
                self._mouse_over = False

    def on_enter(self):
        """Called when mouse pointer enters the widget area."""
        Animation(elevation=10, shadow_softness=20, duration=0.2).start(self)

    def on_kv_post(self, base_widget):
        """Called after the kv string is processed."""
        super().on_kv_post(base_widget)
        Animation(opacity=1, duration=0.5).start(self)

    def on_leave(self):
        """Called when mouse pointer leaves the widget area."""
        Animation(elevation=self.elevation_normal, shadow_softness=self.shadow_softness_normal, duration=0.2).start(self)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            Animation(scale_value_x=0.98, scale_value_y=0.98, duration=0.1).start(self)
            # It's important to call super to propagate the touch event,
            # which is necessary for ripple_behavior and other touch events.
            return super().on_touch_down(touch)
        return False # Touch not on widget

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos) or (self.scale_value_x != 1.0): # Check if touch up is on widget or if it was scaled
            Animation(scale_value_x=1.0, scale_value_y=1.0, duration=0.1).start(self)
            return super().on_touch_up(touch)
        return False # Touch not on widget

    def update_content(self, title_text=None, content_text=None):
        if title_text:
            self.title_label.text = title_text
        if content_text:
            self.content_label.text = content_text
