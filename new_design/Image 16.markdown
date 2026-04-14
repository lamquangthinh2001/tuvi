# Design System Specification: The Celestial Archive

## 1. Overview & Creative North Star
Modern Vietnamese astrology is often cluttered by legacy grid systems and overwhelming text density. This design system seeks to transform that complexity into a high-end, editorial experience.

**Creative North Star: "The Digital Oracle"**
The system functions as a sophisticated curator of cosmic data. It breaks away from the rigid, "boxed-in" layout of traditional charts by using intentional asymmetry, layered depth, and a high-contrast typographic scale. The goal is to move beyond a simple utility and create a sanctuary for self-discovery—an interface that feels as much like a premium fashion periodical as it does a spiritual guide.

## 2. Colors: Tonal Depth & Elemental Soul
The palette is rooted in the Five Elements (Ngũ Hành) but interpreted through a luxurious, nocturnal lens.

*   **Mystic Base:** Utilizing `surface` (#131313) as the canvas creates a "void" where celestial information can glow.
*   **The Primary Red:** `primary` (#ffb3ac) and its containers are used exclusively for vital "Hỏa" (Fire) stars and critical life-path indicators.
*   **The Golden Ratio:** `secondary` (#e9c349) represents "Thổ" (Earth) and royalty. Use this for the "Mệnh" (Life) and "Thân" (Body) palaces to denote their supreme importance.
*   **Emerald Vitality:** `tertiary` (#88d982) serves the "Mộc" (Wood) element, signifying growth and auspicious transitions.

**The "No-Line" Rule**
Traditional charts (as seen in the reference) rely on harsh black lines to separate the 12 Palaces. This design system **prohibits 1px solid borders**. Boundaries must be defined solely by background shifts. Use `surface_container_low` for the general grid and `surface_container_high` for the active focus Palace.

**The Glass & Gradient Rule**
To add "soul," use subtle radial gradients on Hero components, transitioning from `primary_container` to `surface`. Floating elements, such as star descriptions, should utilize Glassmorphism: a semi-transparent `surface_variant` with a 20px backdrop blur to simulate frosted glass against the cosmos.

## 3. Typography: Architectural Clarity
We use a dual-font strategy to balance modernity with readability.

*   **The Authority (Manrope):** Used for `display` and `headline` scales. Its geometric construction provides an architectural, trustworthy feel for large numbers (Year of Birth) and Palace titles.
*   **The Narrator (Be Vietnam Pro):** Used for `title`, `body`, and `label`. This font is optimized for Vietnamese diacritics, ensuring that complex star names like "Thiên Khôi" or "Hóa Lộc" remain legible even at the `label-sm` scale.

**Hierarchy as Brand Identity**
By using `display-lg` for the central "Lá Số" summary and `label-md` for the secondary stars, we create a clear "read-order" that prevents the user from feeling overwhelmed by the 100+ stars in a typical chart.

## 4. Elevation & Depth: Tonal Layering
In this system, depth is not "added"—it is "revealed."

*   **The Layering Principle:** Instead of shadows, stack surface tiers. Place a `surface_container_lowest` card (the "Lá số" details) on top of a `surface_container_low` section to create a soft, natural lift.
*   **Ambient Shadows:** If a Palace card must "float" during a drag-and-drop interaction, use a shadow with a 32px blur at 6% opacity, tinted with `on_surface`.
*   **The "Ghost Border" Fallback:** For accessibility in the astrology grid, use a "Ghost Border"—the `outline_variant` token at 15% opacity. This provides a structural hint without cluttering the visual field.
*   **Signature Textures:** Minimalist Bát Quái (Eight Trigrams) and cloud motifs should be treated as "watermarks," using `outline_variant` at 10% opacity, placed behind the typography to add cultural texture without hindering legibility.

## 5. Components

### The Palace Card (Cung)
The core unit of the app.
*   **Structure:** No borders. Background: `surface_container_low`. 
*   **States:** On hover/active, shift to `surface_container_highest` with a `secondary` (Gold) accent corner.
*   **Typography:** Palace name in `title-md`, primary stars in `body-md` (colored by element), and secondary stars in `label-sm`.

### Primary Action Button
*   **Style:** Pill-shaped (`rounded-full`). 
*   **Visual:** A subtle gradient from `primary` to `primary_container`. 
*   **Text:** `label-md` in `on_primary`, all-caps with 0.05em letter spacing for an editorial look.

### Celestial Chips
Used for tagging star properties (e.g., "Đắc Địa", "Vượng Địa").
*   **Visual:** Semi-transparent backgrounds using `tertiary_container` (for positive) or `error_container` (for negative) at 30% opacity. 
*   **Corner:** `rounded-sm` (0.125rem) to maintain a crisp, modern edge.

### Input Fields
*   **Style:** Minimalist "Underline" style rather than a box.
*   **Border:** Use `outline_variant` at 40% for the resting state, moving to `secondary` (Gold) at 100% on focus.

## 6. Do's and Don'ts

### Do:
*   **Use White Space:** Allow at least 24px of padding between Palace content and the card edge. Astrology is complex; the UI shouldn't be.
*   **Respect the Diacritics:** Ensure line-height in `body-md` is at least 1.5x to prevent Vietnamese tone marks from overlapping.
*   **Color with Intent:** Only color text that has a specific astrological meaning (e.g., Red for Fire stars). Keep administrative text (labels, dates) in `on_surface_variant`.

### Don't:
*   **Don't Use Dividers:** Avoid horizontal lines between stars. Use the `body-sm` spacing scale to group information.
*   **Don't Overuse Gold:** Gold (`secondary`) is for the "Self" (Mệnh/Thân). Overusing it across all palaces dilutes the sense of importance.
*   **Don't Use Pure White:** Never use #FFFFFF. Always use `on_surface` (#e5e2e1) to maintain the sophisticated, low-eye-strain nocturnal aesthetic.