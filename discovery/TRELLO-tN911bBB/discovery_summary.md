# Discovery Summary — The Internet

- Trello Card: https://trello.com/c/tN911bBB/52-discovery-https-the-internetherokuappcom
- Target: https://the-internet.herokuapp.com
- Generated: 2026-05-15 (UTC)
- Pages discovered: 24 in-scope modules/pages (161 raw captures during crawl)
- Auth: public site; `/login` supports demo credentials shown on the page (`tomsmith / SuperSecretPassword!`)
- Google Doc: https://docs.google.com/document/d/1l6WbnuIHPIuO1ltMpFkdSW42yU1SHJUc9WzZ3P4wSLA/edit
- Google Sheet: https://docs.google.com/spreadsheets/d/1JewhWTsBsqYa-1pJkrBEVh396fua7-Ll-8r4mw5ushA/edit

## Recommended automation order
- P0: Form Authentication, Dynamic Loading, JavaScript Alerts, Add/Remove Elements
- P1: Frames/iFrame, Checkboxes, Dropdown, Inputs, Key Presses, Multiple Windows, Context Menu
- P2: Notification Messages, Hovers, Floating Menu, Infinite Scroll, Horizontal Slider, Sortable Data Tables, Shadow DOM
- High-risk / later hardening: Drag and Drop, Disappearing Elements

## Key findings
- This target is a public UI practice site made up of isolated challenge pages, so modules should be automated independently rather than as one end-to-end journey.
- The login path is straightforward: `GET /login` -> `POST /authenticate` -> redirect to `/secure` on success, with a logout link returning to `/login`.
- Dynamic Loading pages require explicit waits; `notification_message_rendered` returns unstable/randomized messages; `drag_and_drop` remains the highest-risk interaction for browser automation.
- `iframe`, Shadow DOM, and Multiple Windows each need special locator/context strategies (frame-scoped locators, shadow-root access, and child-page handling respectively).
- Disappearing Elements intentionally mutates navigation presence, so tests should verify a required subset rather than exact full-menu equality.

## Suggested scenario coverage from discovery
- Form Authentication: valid login, invalid login, logout
- Dynamic Loading: hidden-element reveal and DOM-late-render variants
- JavaScript Alerts: alert accept, confirm dismiss, prompt input
- Add/Remove Elements: add button spawns delete controls; delete removes control
- iFrame: edit TinyMCE body; verify toolbar chrome
- Multiple Windows: spawn child window and assert destination heading
- Notification Messages: assert banner presence / allowed message family, not exact text
- Checkboxes / Dropdown / Inputs / Key Presses: low-complexity control-state smoke coverage

## Automation blockers / brittleness notes
- Drag and Drop may need fallback event simulation if native drag helpers are unreliable.
- Notification text must use pattern-based assertions.
- Dynamic Loading must avoid `time.sleep()` and wait on real DOM state changes.
- Shadow DOM and iFrame pages require dedicated locator helpers.

## Output status
- Discovery report created and shared publicly
- Structured Google Sheet test cases created and shared publicly
- Repo branch prepared for follow-up implementation sessions
