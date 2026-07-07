# Security Policy

## Who this is for

This repository is a template for **LLM-assisted autograding** of student
assignments (e.g. with GitHub Classroom). If you adopt it, please read this
first: the *naive* setup can expose **your** LLM API keys to your own students.

## ⚠️ The risk — API keys inside student-controlled workflows

The grading / AI-tutor workflow passes API keys into a GitHub Actions job:

```yaml
# RISKY when this workflow runs inside a repository the student controls:
env:
  CLAUDE_API_KEY: ${{ secrets.CLAUDE_API_KEY }}
  GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
```

In a GitHub Classroom setup **each student owns their assignment repository**, so a
student can:

1. Edit the workflow in their own repo (`.github/workflows/…`);
2. Add a step that exfiltrates the secret — base64/split it to defeat log masking,
   or `curl` it to an external host;
3. Push. The workflow runs **with your org/repo secrets**, and the key is gone.

Log masking is **not** a defense (it is trivially bypassed), and this is a direct
push to a repo the student owns — **not** a fork pull request, so fork-PR secret
protections do not apply. If your keys are org secrets visible to student repos,
**treat them as exposed** the moment this pattern ships.

## ✅ The secure pattern — grade centrally, keep keys off student repos

Do **not** run keyed grading inside student-controlled repos. Instead:

1. **Grade in a repo students cannot push to.** A private *grader* repository (or
   org) checks out the student's code as **data** and grades it in an isolated
   container (`--network none`, non-root, read-only mount). Keys live **only**
   there.
2. **Keep student repos keyless *and* CI-less.** The student repo needs no grading
   workflow at all. **Disable Actions on student repositories** so a pushed
   workflow cannot run in the first place.
3. **Isolate the secrets.** Never set LLM keys as org secrets on the *students'*
   org; store them only on the grader repo.
4. **Trust only authentic grades.** If you report results as check-runs, verify
   each was authored by *your* grading GitHub App — a student can otherwise post
   their own check-run to fake a passing grade.
5. **Rotate exposed keys.** Any key ever reachable by a student-controlled
   workflow should be considered compromised and rotated.

The tutor reads student source as **text** to build its prompt; it never executes
student code with the keys in scope, and the key authenticates the API call — it
never appears in the prompt, so hostile student input cannot echo it back.

## Reporting a vulnerability

Please report security issues **privately** via
[GitHub Security Advisories](../../security/advisories/new), not a public issue.

---

*This policy applies to every repository derived from this template. If you fork or
copy it, keep `SECURITY.md` and adopt the secure pattern above before wiring in any
API keys.*
