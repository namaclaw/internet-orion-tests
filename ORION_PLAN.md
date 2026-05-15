# Orion Implementation Plan — Form Authentication: Login flow and authenticated session behavior — The Internet — Herokuapp UI Tests

## What I found
- `conftest.py`: minimal scaffold only; no auth reuse, page fixture, or base-url helpers exist yet.
- `features/README.md`: no feature coverage has been implemented in this repo yet.
- `pages/README.md`: no page objects exist yet.
- `steps/README.md`: no step definitions exist yet.
- `discovery/TRELLO-T5MOFOEP/discovery_summary.md`: prior discovery already identified `/login` as a P0 module and noted that credentials are public fixture data shown in the UI.

## Existing test structure summary
- `features/`: currently placeholders only; will need a new auth-focused `.feature` file.
- `steps/`: currently placeholders only; will need matching pytest-bdd step definitions for login, logout, flash messaging, and direct `/secure` access checks.
- `pages/`: currently placeholders only; will need page objects for the login page and secure area.
- Fixtures: only `browser_context_args` exists. No reusable authenticated storage-state fixture exists yet, so one must be added.

## Approach
Start by proving the site and login flow work with a standalone Playwright smoke script against `https://the-internet.herokuapp.com/login`. Use that probe to measure page speed, verify the public credentials, and save authenticated browser state into `.auth/state.json`. Then build a small, stable pytest-bdd auth stack around two page objects (`LoginPage`, `SecureAreaPage`), a session-scoped auth fixture, and one focused feature file covering happy path plus core negative-path and session-behavior scenarios.

## Files to change
- `conftest.py`: add base URL support, auth-state bootstrap/reuse, and browser/page fixtures for unauthenticated vs authenticated contexts.
- `README.md`: update with the module scope and test-run instructions if the new structure needs brief documentation.

## Files to create
- `features/form_authentication.feature`: up to ~10 focused auth/session scenarios.
- `steps/test_form_authentication_steps.py`: pytest-bdd step definitions and assertions.
- `pages/login_page.py`: selectors and actions for `/login`, flash banner, and form submission.
- `pages/secure_area_page.py`: selectors and helpers for `/secure`, logout, and auth-state assertions.
- `.auth/.gitkeep` if needed to preserve the auth directory without committing browser state.
- `/tmp/orion_form_auth_smoke.py` during execution only: standalone smoke probe script.

## Step-by-step implementation approach
1. Run smoke script for `/login` and `/secure`, measure load/login time, confirm public credentials, and save storage state.
2. Record environment speed in this plan and set timeouts accordingly.
3. Expand `conftest.py` with a session-scoped fixture that can create authenticated state once and load it for protected-page tests.
4. Create page objects for login and secure area using stable selectors (`#username`, `#password`, `button[type=submit]`, `#flash`, `.icon-2x.icon-signout`, etc., adjusting after live inspection if needed).
5. Add `form_authentication.feature` scenarios in P0/P1 order:
   - successful login
   - secure-area landing validation
   - logout return to unauthenticated state
   - invalid username
   - invalid password
   - direct `/secure` access before login
   - direct `/secure` access after login via saved state
   - flash visibility checks across success/error/logout
   - optional empty-field behavior if stable and present
6. Implement step definitions with explicit waits only; no `sleep`.
7. Run the single feature repeatedly, fixing failures with the 5-attempt rule.
8. Commit auth scaffold first, then commit passing scenario batches.
9. Update the existing Google Doc section and Google Sheet tab after implementation.
10. Run pre-PR review, push branch, open PR, comment on Trello, and move the card to Review.

## Test strategy
- Smoke probe:
  `PYTHONPATH=/home/node/.openclaw/lib/python PLAYWRIGHT_BROWSERS_PATH=/home/node/.openclaw/playwright-browsers python3 /tmp/orion_form_auth_smoke.py`
- Feature run:
  `PYTHONPATH=/home/node/.openclaw/lib/python PLAYWRIGHT_BROWSERS_PATH=/home/node/.openclaw/playwright-browsers python3 -m pytest features/form_authentication.feature -q --tb=short`
- If selector behavior is unclear, inspect the live DOM with a targeted Playwright script before changing assertions.

## Risks
- Flash banner copy includes trailing close glyph/newlines; assertions should normalize and target meaningful fragments or state, not exact full strings.
- `/secure` access behavior may redirect immediately back to `/login`; protected-page assertions should check URL + flash visibility rather than over-assuming intermediate states.
- Because the repo is a fresh scaffold, fixture and page-object patterns must be established cleanly once to avoid brittle step definitions.

## Environment speed note
- Smoke probe results: `/login` loaded in ~1.14s and successful login completed in ~0.32s.
- Environment classification: FAST — default timeouts are acceptable, but keep explicit waits on redirect/flash state changes.
- Auth state saved successfully to `.auth/state.json` for fixture reuse.
