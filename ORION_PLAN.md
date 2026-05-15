# Orion Implementation Plan — Dynamic Modules: Explicit waits and brittle interaction coverage — The Internet — Herokuapp UI Tests

## What I found
- `conftest.py`: the repo now has a reusable base URL fixture plus authenticated/unauthenticated page fixtures backed by `.auth/state.json`; this is enough to support both public modules and auth-dependent reuse without re-logging for every test.
- `features/form_authentication.feature`: the current feature pattern is one module-focused `.feature` file with concise scenarios and stable, behavior-level assertions.
- `steps/test_form_authentication_steps.py`: step definitions currently bind one feature file directly and keep assertions close to page-object helpers rather than embedding raw selectors everywhere.
- `pages/login_page.py` + `pages/secure_area_page.py`: existing page objects are intentionally thin and expose stable selectors plus small, composable helper methods. New dynamic modules should follow the same minimal POM style.
- `discovery/TRELLO-tN911bBB/discovery_summary.md`: discovery already prioritized Dynamic Loading, JavaScript Alerts, iFrame, Notification Messages, and later brittle modules like Drag and Drop. It also explicitly warned that dynamic loading must use real DOM waits and notifications must avoid exact randomized-text assertions.

## Existing test structure summary
- `features/`: one implemented auth feature file plus README placeholder. New module coverage should be split into discrete feature files by module family, not one giant scenario file.
- `steps/`: one implemented auth step file. The current pattern is one Python step module per feature file.
- `pages/`: two auth page objects. No helpers exist yet for dynamic loading, alerts, iframe editing, add/remove elements, or notification banners.
- Fixtures: reusable `authenticated_page` and `unauthenticated_page` already exist. No extra auth fixtures are needed for the first public dynamic modules.

## Approach
Build this session around ~10 high-value scenarios in P0 → P1 order, starting with the most brittle-but-automatable pages: Dynamic Loading, JavaScript Alerts, Add/Remove Elements, iFrame, and Notification Messages. Keep assertions structural and state-based: wait for real visibility/text changes, verify result containers and editor contents, and avoid overfitting to randomized notification copy. Defer Shadow DOM and Drag and Drop unless time remains after the more stable high-risk modules are green.

## Files to change
- `conftest.py`: raise the default timeout slightly and, if helpful, add a tiny shared fixture/helper for public module pages so explicit waits stay centralized.
- `README.md`: optionally update the covered-module list once the new batch is implemented.

## Files to create
- `features/dynamic_loading.feature`: scenarios for `/dynamic_loading/1` and `/dynamic_loading/2` with explicit waits only.
- `features/javascript_alerts.feature`: scenarios for JS alert accept, confirm dismiss, and prompt input.
- `features/add_remove_elements.feature`: scenarios for adding and deleting dynamic controls.
- `features/iframe.feature`: scenarios for TinyMCE editor visibility and editable body behavior.
- `features/notification_messages.feature`: scenario(s) for rendered notification visibility and allowed message-family assertions.
- `pages/dynamic_loading_page.py`: helpers for start button, loading indicator, and revealed-content waits.
- `pages/javascript_alerts_page.py`: helpers for triggering each alert type and reading `#result`.
- `pages/add_remove_elements_page.py`: helpers for add/delete button counts and visibility.
- `pages/iframe_page.py`: helpers for toolbar visibility, frame access, editor text replacement, and readback.
- `pages/notification_messages_page.py`: helpers for reloading notifications and normalizing flash text.
- `steps/test_dynamic_loading_steps.py`
- `steps/test_javascript_alerts_steps.py`
- `steps/test_add_remove_elements_steps.py`
- `steps/test_iframe_steps.py`
- `steps/test_notification_messages_steps.py`

## Step-by-step implementation approach
1. Reuse the existing auth scaffold by branching from main and carrying forward the prior auth commits already implemented in the repo history.
2. Re-run a smoke probe on `/login` to refresh `.auth/state.json` and timing data for this branch.
3. Implement P0 module pages + steps first:
   - Dynamic Loading: hidden-element variant and DOM-late-render variant.
   - JavaScript Alerts: JS Alert accept, JS Confirm dismiss, JS Prompt input.
   - Add/Remove Elements: create dynamic delete buttons, then remove them.
4. Run the corresponding feature files and fix failures before moving on.
5. Implement P1 module pages + steps:
   - iFrame: verify TinyMCE chrome and editable-body update/readback.
   - Notification Messages: verify flash banner renders after click and text belongs to the known message family without matching exact randomized copy.
6. If the core set is green and time remains, probe one extra brittle module (likely Shadow DOM or Drag and Drop) and only implement it if it is stable within the 5-attempt rule.
7. Update the Google Doc section `Dynamic Modules implementation` and mark implemented sheet rows as `Automated` on the existing discovery artifacts.
8. Run pre-PR review, push branch, open a PR, comment on Trello with the PR/doc/sheet links, and move the card to Review.

## Planned scenario batch for this session
### P0
1. Dynamic Loading example 1 reveals hidden content after Start.
2. Dynamic Loading example 2 renders content after Start.
3. JavaScript Alert accept updates `#result`.
4. JavaScript Confirm dismiss updates `#result`.
5. JavaScript Prompt accepts typed input and echoes it in `#result`.
6. Add/Remove Elements adds a delete control per click.
7. Add/Remove Elements removes a delete control when clicked.

### P1
8. iFrame page shows editable TinyMCE area and toolbar shell.
9. iFrame body text can be replaced and read back.
10. Notification Messages renders a visible flash banner from the allowed message set.

## Test strategy
- Full targeted batch:
  `PYTHONPATH=/home/node/.openclaw/lib/python PLAYWRIGHT_BROWSERS_PATH=/home/node/.openclaw/playwright-browsers python3 -m pytest features/dynamic_loading.feature features/javascript_alerts.feature features/add_remove_elements.feature features/iframe.feature features/notification_messages.feature -q --tb=short`
- Per-module runs during implementation:
  `python3 -m pytest features/<module>.feature -q --tb=short`
- Live selector probes only when needed, using short one-off Playwright scripts. No `time.sleep()` in test code.

## Risks
- `/dynamic_loading/1` hides the final content in the DOM before it becomes visible, while `/dynamic_loading/2` delays DOM insertion entirely; the page object must wait differently for each variant.
- TinyMCE toolbar markup is noisy and brittle; assertions should target the iframe body and a minimal toolbar presence signal, not full toolbar text equality.
- `/notification_message_rendered` rotates among several valid messages and may include trailing formatting characters, so assertions must normalize text and match against an allowed set/pattern family.
- Drag and Drop remains intentionally brittle and should not displace the planned P0/P1 coverage if it starts burning retries.

## Environment speed note
- Refreshed smoke probe results on this branch: `/login` loaded in ~1.70s and login completed in ~0.32s.
- Environment classification: FAST/MODERATE boundary; use explicit waits with a 15s default timeout and no hard sleeps.
- Auth state refreshed successfully at `.auth/state.json` for any follow-on authenticated scenarios.
