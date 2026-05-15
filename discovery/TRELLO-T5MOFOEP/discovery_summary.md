# Discovery Summary — The Internet

- Trello Card: https://trello.com/c/T5MOFOEP
- Target: https://the-internet.herokuapp.com
- Pages crawled: 26
- Auth: public site; /login uses demo credentials shown on page

## Recommended automation order
- P0: Form Authentication, Dynamic Loading, JavaScript Alerts, Add/Remove Elements
- P1: Frames/iFrame, Checkboxes/Dropdown/Inputs/Key Presses, Multiple Windows, Context Menu
- P2: Notification Messages, Hovers, Floating Menu, Infinite Scroll, Horizontal Slider, Sortable Data Tables, Shadow DOM
- P3 / high-risk: Drag and Drop, Disappearing Elements (conditional nav)

## Risk notes
- Login page exposes demo credentials in the UI; implementation should treat them as public fixture data rather than secrets.
- Notification messages are intentionally unstable across reloads; assertions should target banner visibility and allowed message patterns, not an exact string.
- Dynamic Loading and iFrame pages need explicit wait and frame-scoping strategies; avoid sleep-based timing.
- Drag and Drop is historically brittle in browser automation because HTML5 drag events may not fire uniformly; keep this high-risk in backlog ordering.
- Disappearing Elements intentionally mutates navigation links; assert only the required subset of links.

## User flows identified
- Public landing page -> select a challenge page -> perform a single focused interaction -> confirm UI feedback on the same page.
- Form Authentication -> submit credentials -> land on secure area or receive inline flash error.
- Dynamic Loading -> click Start -> wait for spinner / deferred content -> assert final DOM state.
- Frames/iFrame -> enter frame context -> interact with framed content -> return to top document if needed.
- Multiple Windows -> open secondary window -> assert child page -> preserve parent context.

## Page inventory
- `/` — headings: Welcome to the-internet, Available Examples
- `/add_remove_elements/` — buttons: Add Element; headings: Add/Remove Elements
- `/checkboxes` — 1 form(s); inputs: 2; headings: Checkboxes
- `/context_menu` — headings: Context Menu
- `/disappearing_elements` — headings: Disappearing Elements
- `/drag_and_drop` — headings: Drag and Drop
- `/dropdown` — inputs: 1; headings: Dropdown List
- `/dynamic_loading` — headings: Dynamically Loaded Page Elements
- `/floating_menu` — headings: Floating Menu
- `/frames` — headings: Frames
- `/horizontal_slider` — inputs: 1; headings: Horizontal Slider
- `/hovers` — headings: Hovers
- `/infinite_scroll` — headings: Infinite Scroll
- `/inputs` — inputs: 1; headings: Inputs
- `/javascript_alerts` — buttons: Click for JS Alert, Click for JS Confirm, Click for JS Prompt; headings: JavaScript Alerts
- `/key_presses` — 1 form(s); inputs: 1; headings: Key Presses
- `/login` — 1 form(s); buttons: Login; inputs: 2; headings: Login Page
- `/shadowdom` — headings: Simple template
- `/tables` — tables: 2; headings: Data Tables
- `/windows` — headings: Opening a new window
- `/` — headings: Welcome to the-internet, Available Examples
- `/dynamic_loading/1` — buttons: Start; headings: Dynamically Loaded Page Elements
- `/dynamic_loading/2` — buttons: Start; headings: Dynamically Loaded Page Elements
- `/iframe` — buttons: File, Edit, View; inputs: 1; headings: An iFrame containing the TinyMCE WYSIWYG Editor
- `/infinite_scroll/4` — headings: 
- `/windows/new` — headings: New Window

## Suggested assertions
- Prefer role/text selectors on stable demo controls; use frame locators for `/iframe`.
- Use explicit waits for spinner disappearance or late DOM attachment on dynamic loading pages.
- For notification messages, assert visibility or allowed-message pattern only.
- For drag and drop, budget for fallback implementation strategy if native HTML5 drag is unreliable.
