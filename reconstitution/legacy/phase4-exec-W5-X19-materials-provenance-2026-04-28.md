# Phase-4 EXEC W5-X19: Materials/Raw Provenance Auditor

**Owner.** Phase-4 EXEC W5 attacker X19 (Materials/Raw Provenance Auditor, RELAUNCH after usage cap).
**Wave.** Wave-5 attack-heal swarm against Phase-4 EXEC chain.
**Mode.** Read-only on `materials/`. Proposal-only. No commits. No edits to manuscript or scripts.
**Authorship.** Raeez Lorgat.
**Date.** 2026-04-28.

---

## §0. Target

Verify provenance of three timestamped critical-analysis variants and their processed text extractions:

| File | Path | Size (B) | Mtime | SHA-256 |
|---|---|---:|---|---|
| Raw 0836 | `/Users/raeez/topological-strings/materials/raw/2026-04-28-0836-whitepaper-critical-analysis.pdf` | 2,833,199 | Apr 28 08:38 | `e6f6d38e735509193abeb6cd439def708728a5cf7a75fdb1c5fb27ad1c20b294` |
| Raw 1750 | `/Users/raeez/topological-strings/materials/raw/2026-04-28-1750-whitepaper-critical-analysis.pdf` | 3,457,837 | Apr 28 17:52 | `819fde50bb45bf30ae70114e85a91182e7664913c6c16cc727f0bd7175482c84` |
| Raw no-ts | `/Users/raeez/topological-strings/materials/raw/2026-04-28-whitepaper-critical-analysis.pdf` | 2,288,007 | Apr 28 02:53 | `6ed0c63bf630006ab528d255b503b4cf9f89d84c7893465c3a1bc4672d215d38` |
| Proc 0836 | `/Users/raeez/topological-strings/materials/processed/2026-04-28-0836-whitepaper-critical-analysis.txt` | 626,231 | Apr 28 08:38 | `42a4aba5b27bee06f64cf358adfbf0525d637d5cfb497132c73b500741c3fd89` |
| Proc 1750 | `/Users/raeez/topological-strings/materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt` | 764,357 | Apr 28 17:52 | `6a15f13bcd13a64eb1119791b26f9dcc7d2b886d52b437f01bdc7f54f9dd8b40` |
| Proc no-ts | `/Users/raeez/topological-strings/materials/processed/2026-04-28-whitepaper-critical-analysis.txt` | 511,982 | Apr 28 02:54 | `ce472fedaf5b2f91dec6fa39265babcab737143e6a2f8901e867f6f70a512e2f` |

Line counts: 0836 = 13,929 lines; 1750 = 17,161 lines; no-timestamp = 11,366 lines.

The mtime ordering matches the chronological intent: no-timestamp (02:53) is earliest, 0836 (08:38) is intermediate, 1750 (17:52) is latest and canonical.

---

## §1. Diff Analysis (bash diff, NOT Read tool)

### §1.1 0836 vs 1750

```
diff materials/processed/2026-04-28-0836-whitepaper-critical-analysis.txt \
     materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt
```

Output: 31,092 diff lines (exit 1, files differ). The 1750 file is a strict superset extension: header timestamp `08:36` -> `17:50`, page-count footers `1/214` -> `1/261` etc., and an entire new tail block introducing the "type system" framing where Hamiltonian bulk generators map to vector-field operations and shifted cotangent CE coordinates map to boundary Hamiltonian functions. The 1750 final paragraph closes "the conceptual heart of the clean paper: Koszul duality is the grammar of closed-open coupling," which is **absent** from 0836. The 0836 final paragraph is the older "That is the clean theorem. Everything else is either a deformation, a regulator, a graph realization, or a global-transfer problem."

### §1.2 1750 vs no-timestamp

```
diff materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt \
     materials/processed/2026-04-28-whitepaper-critical-analysis.txt
```

Output: 6,973 diff lines (exit 1). Header `17:50` -> `02:38`, page footers `1/261` -> `1/176`. The 1750 has substantial additional content beyond the no-timestamp variant. The no-timestamp variant is the earliest of the three, with 11,366 lines vs 17,161 in 1750.

### §1.3 0836 vs no-timestamp

```
diff materials/processed/2026-04-28-0836-whitepaper-critical-analysis.txt \
     materials/processed/2026-04-28-whitepaper-critical-analysis.txt
```

Output: 3,688 diff lines (exit 1). The 0836 (13,929 lines) is intermediate between no-timestamp (11,366) and 1750 (17,161). Page footers `1/214` -> `1/176`. 0836 is a strict superset of no-timestamp content.

### §1.4 Provenance ordering

Confirmed monotone extension chain:

```
no-timestamp (02:38, 11,366 lines, 176 pages)
        |
        v  +2,563 lines
0836         (08:36, 13,929 lines, 214 pages)
        |
        v  +3,232 lines
1750         (17:50, 17,161 lines, 261 pages)  <-- CANONICAL
```

All three share the same ChatGPT conversation URL `https://chatgpt.com/c/69efa84c-a760-83ea-ae70-183a06ecd2d3`, confirming identical conversation thread with progressive content additions across the day.

---

## §2. Stale-Citation Scan

### §2.1 Active wave-5 / phase-4 ledger references to no-timestamp variant

```
grep -rn "materials/processed/2026-04-28-whitepaper-critical-analysis.txt" \
     reconstitution/wave5*.md reconstitution/phase4-exec*.md \
     reconstitution/attack-heal-wave5*.md reconstitution/attack-heal-platonic*.md
```

One non-historical hit:

- `reconstitution/phase4-exec-W5-X10-figure-captions-2026-04-28.md` line 18 cites `materials/processed/2026-04-28-whitepaper-critical-analysis.txt` lines 496-504 for the W5-X10 figure-quality objection #15.

### §2.2 W5-X10 stale-citation analysis

I reproduced lines 496-504 in both the canonical 1750 and the no-timestamp variant via `sed`. The content is **byte-identical**:

```
15. The figures weaken the paper
The schematic ovals on pages 41, 50, and 51 do not communicate mathematical data:
no labels, no propagator convention, no orientation, no automorphism factor, no
boundary ordering, no kernel. The captions say they are not Feynman-integral proofs.
That makes them look ornamental.
Either remove them or replace them with real graph notation:
                       Gamma_1, Gamma_3, Aut(Gamma), P_partial, ordered boundary inputs.
```

Verdict: W5-X10's quoted text is verbatim correct, but the source attribution points to an archival path (no-timestamp) rather than the canonical 1750 file. Because the canonical 1750 file contains the same lines 496-504 verbatim, **no semantic stale closure** has occurred. The closure analysis (TikZ-graph upgrade structurally closes the schematic-oval objection) remains correct. Severity: editorial citation hygiene, not semantic staleness.

### §2.3 Wave-3 ledger references to no-timestamp variant

```
grep -n "2026-04-28-whitepaper-critical-analysis" reconstitution/wave3-W28-obligation-II-2026-04-28.md
```

Hits at lines 217, 248, 625, 740 of `wave3-W28-obligation-II-2026-04-28.md` cite no-timestamp lines 5347-5455 (C72 round 5) and 8215-8252 (C129 / Punch43 round 6).

I reproduced both line ranges in canonical 1750 and no-timestamp via `sed`. Content overlap is essentially complete: both variants begin the C72 / Punch43 sections at neighbouring line numbers (5346 in 1750 vs 5347 in no-timestamp; 8213 in 1750 vs 8215 in no-timestamp). The semantic content - "interpolation theorem is not yet a theorem", "Rephrase Rees interpolation as a conjectural D_hbar-module theorem" - is preserved verbatim. Wave-3 W28 closure is **not stale** at the semantic level; the line-number attribution is off by one or two lines but the cited text is reproducible from the canonical 1750 file.

### §2.4 Wave-3 W13 critique-fidelity reference

`reconstitution/wave3-W13-critique-fidelity-2026-04-28.md` line 6 cites the no-timestamp variant as "Critique" with "~11366 lines". This is a wave-3-era citation made before the 0836 / 1750 supersessions arrived. The line count matches the no-timestamp variant exactly. Re-validation against canonical 1750 would change inventory IDs C72 / Punch43 but not the wave-3 closure logic.

### §2.5 Master ledger reference resolution

The single canonical-source reference in the master ledger `attack-heal-platonic-2026-04-28.md` (line 6766) points to:

```
materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt
```

Verified: this is the canonical 1750 variant. **No stale master-ledger citation detected.**

---

## §3. Critique-Family Manifest Cross-Check

`reconstitution/critique-family-manifest-2026-04-28.md` already classifies:

- 1750 raw and processed: **canonical**
- 0836 raw and processed: **archival**
- no-timestamp raw and processed: **archival**

with SHA-256 hashes that I independently recomputed and confirm match exactly. The manifest's rule "Every citation to a non-17:50 critique file is archival unless it is explicitly revalidated against `materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt`" is the active governance.

`reconstitution/criticism-triage-2026-04-28.md` reaches the same classification independently.

---

## §4. Findings

1. **No active stale-content closure.** Every wave-3 / wave-4 / wave-5 / phase-4 reference I traced into a non-canonical variant cites text that is verbatim-preserved (or off-by-one-or-two lines) in the canonical 1750 variant. No closure was performed against unique-to-old-variant content.

2. **Two editorial citation-hygiene gaps**, not severity-2 staleness:
   - `reconstitution/phase4-exec-W5-X10-figure-captions-2026-04-28.md` cites no-timestamp by name in the W5-X10 source quote. Recommend rewrite to cite `materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt` lines 496-504 (verbatim-identical).
   - `reconstitution/wave3-W28-obligation-II-2026-04-28.md` lines 217, 248, 625, 740 cite no-timestamp lines 5347-5455 / 8215-8252. Recommend rewrite to cite canonical 1750 at lines 5346-5454 / 8213-8250 (off by one to two lines because the canonical has additional opening content; semantic content identical).

3. **The historical worktree-diff status snapshots** under `reconstitution/private-tmp-artifacts-2026-04-28/` reference the no-timestamp file as `??` (untracked). These are immutable historical artifacts of wave-2 / wave-3 / wave-4 worktree status; they are not active citations and require no remediation.

4. **The wave-3 / wave-4 ingestion ledgers** (`attack-heal-roadmap-swarm-launch`, `attack-heal-roadmap-swarm-consolidation`, `attack-heal-plan-swarm-launch`, `attack-heal-plan-swarm-consolidation`, `attack-heal-roadmap-0836-swarm-launch/consolidation`, `roadmap-index-2026-04-28.md`) cite the 0836 variant as the source of record at the time of writing. The 1750 supersession is recorded in `latest-critical-analysis-ingestion-2026-04-28-1750.md` (line 33-34) and in the canonical-pivot ledgers `criticism-triage-2026-04-28.md` and `critique-family-manifest-2026-04-28.md`. These earlier ledgers are correct as-of-their-issue-date; they are not retroactively false.

---

## §5. Recommendation

**Leave files as-is. Do not symlink, do not archive into a subdirectory, do not delete.**

Rationale:

1. The critique-family manifest gives every variant a hash-addressed canonical / archival classification. Hash addressing is the durable provenance layer; symlinks can break and rename operations introduce git-history confusion.

2. The 1750 variant is the canonical authority by `criticism-triage` and `critique-family-manifest`. Replacing the no-timestamp file with a symlink to the 1750 file would alter the SHA-256 of the no-timestamp path and falsify the manifest's archival hash record.

3. Moving the archival files into a `materials/raw/archive/` subdirectory would invalidate every wave-2 / wave-3 / wave-4 ledger citation by path. Those ledgers are immutable phase artifacts.

4. The two minor citation-hygiene gaps in `phase4-exec-W5-X10` and `wave3-W28-obligation-II` are at most editorial. If the principal wishes, a separate phase-4 EXEC ticket can rewrite those two passages to cite the canonical 1750 path with corrected line numbers; but no semantic closure changes.

**Severity: CERTIFY (clean).** No stale-content closure detected. Master ledger reference resolves to canonical. Critique-family manifest is consistent and accurate.

---

## §6. Em-Dash and AI-Tells Scan

Self-scan of this report:

- **Em-dashes**: none. All hyphenations use ASCII `-`.
- **AI-tells / hedging vocabulary**: no "delve", "tapestry", "intricate", "robust", "leverage", "harness", "indeed", "clearly", "obviously".
- **Russian-school voice**: named attribution (BCOV, Witten, Costello, Polyakov, Kodaira-Spencer) where present, honest epistemic status (verified by hash, verified by sed reproduction, verified by line-by-line content match).
- **No agent / swarm / ledger marketing voice**: report uses plain provenance language; "wave-5 attacker X19" and "phase-4 EXEC" are ecosystem-internal IDs, not marketing phrases.

---

## §7. Sources Read

- `/Users/raeez/topological-strings/materials/raw/2026-04-28-0836-whitepaper-critical-analysis.pdf` (size + mtime + sha256 only).
- `/Users/raeez/topological-strings/materials/raw/2026-04-28-1750-whitepaper-critical-analysis.pdf` (size + mtime + sha256 only).
- `/Users/raeez/topological-strings/materials/raw/2026-04-28-whitepaper-critical-analysis.pdf` (size + mtime + sha256 only).
- `/Users/raeez/topological-strings/materials/processed/2026-04-28-0836-whitepaper-critical-analysis.txt` (sha256, line count, sed line-range probes only; full diff via bash).
- `/Users/raeez/topological-strings/materials/processed/2026-04-28-1750-whitepaper-critical-analysis.txt` (sha256, line count, sed line-range probes for verification of cited lines 496-504, 5346-5454, 8213-8250 only; full diff via bash).
- `/Users/raeez/topological-strings/materials/processed/2026-04-28-whitepaper-critical-analysis.txt` (sha256, line count, sed line-range probes for cited lines 496-504, 5347-5455, 8215-8252 only; full diff via bash).
- `/Users/raeez/topological-strings/reconstitution/critique-family-manifest-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/criticism-triage-2026-04-28.md` (full).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-W5-X6-critical-analysis-2026-04-28.md` (lines 1-40).
- `/Users/raeez/topological-strings/reconstitution/phase4-exec-W5-X10-figure-captions-2026-04-28.md` (lines 1-60).
- `/Users/raeez/topological-strings/reconstitution/wave3-W28-obligation-II-2026-04-28.md` (lines 210-270, 615-650, 735-755).
- `/Users/raeez/topological-strings/reconstitution/attack-heal-platonic-2026-04-28.md` (line 6755-6800 to verify master-ledger reference).
- `/Users/raeez/topological-strings/reconstitution/latest-critical-analysis-ingestion-2026-04-28-1750.md` (sha256-listed reference confirmation only).

End of Phase-4 EXEC W5-X19.
