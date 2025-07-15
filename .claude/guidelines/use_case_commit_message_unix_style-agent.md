# UNIX Style Commit Message Rule

## Critical Rules

- The commit message **title (subject line) must be 50 characters or fewer**.
- The title must be **capitalized**, written in the **imperative mood**, and **must not end with a period**.
- The **second line must be blank**.
- The **body (if present) must wrap at 72 characters per line**.
- The body should explain **what** and **why**, not **how**.
- Use bullet points in the body if listing changes.
- Use an optional footer for breaking changes or issue references.
- Reject commit messages that do not comply with these rules.
- Create multiple smaller commits instead of 1 single commit with all the changes
- **Must not Push the changes**, ask before you push commits to origin
- Print which branch you are committing to.
- Create a new branch if you are on `master` or `main` branch.
- **Never make commit on `master` or `main` branch.**

## Examples

<example type="valid">
Add OAuth2 login support

Implements OAuth2 login for third-party providers.
Improves security and user convenience.

- Refactors authentication flow
- Adds tests for new endpoints
</example>

<example type="valid">
Update constant value to 2.44
</example>

<example type="invalid">
added OAuth2 login support.

This commit adds OAuth2 login for third-party providers. It also
refactors the authentication flow and adds tests for new endpoints.
</example>

<example type="invalid">
refactored OAuth2 login support.
</example>
