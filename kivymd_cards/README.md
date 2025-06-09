# KivyMD Card Widgets

This directory contains custom KivyMD card widgets with enhanced animations.

## `BaseCard`

`BaseCard` is a versatile card widget built upon KivyMD's `MDCard` and includes several built-in animations and customization options.

### Features

*   **Content Display**: Easily set a title and content text.
*   **Hover Animation**: The card elevates and increases shadow softness on mouse hover.
*   **Click/Tap Animation**: Provides a ripple effect and a subtle scaling animation on click or tap.
*   **Entry Animation**: The card fades in smoothly when it's added to the screen.

### How to Use

1.  **Import `BaseCard`:**
    ```python
    from kivymd_cards.base_card import BaseCard
    ```

2.  **Create an instance of `BaseCard`:**
    ```python
    my_card = BaseCard()
    ```

3.  **Update Content:**
    Use the `update_content` method to set the title and main text of the card:
    ```python
    my_card.update_content(title="My Card Title", content="This is some descriptive content for the card.")
    ```

4.  **Add to Layout:**
    Add the card to any KivyMD layout, like `MDBoxLayout` or `MDScreen`.
    ```python
    layout = MDBoxLayout()
    layout.add_widget(my_card)
    ```

### Animations

*   **Hover Effect**: Enabled by default. The card slightly raises (`elevation`) and its shadow becomes softer (`shadow_softness`) when the mouse pointer is over it. It reverts to its normal state when the mouse leaves.
*   **Ripple and Scale on Press**: Enabled by default. When the card is clicked or tapped, it shows a ripple effect (standard KivyMD behavior for `ripple_behavior=True`) and scales down slightly for immediate feedback, then scales back up on release.
*   **Fade-In on Entry**: Enabled by default. The card starts with an opacity of 0 and animates to full opacity when it's initialized and added to the display (via `on_kv_post`).

These animations are currently built-in. Future enhancements could include methods to customize or disable specific animations.
