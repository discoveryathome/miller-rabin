# Review ledger

One row per reviewed contribution: what was reviewed (exact head), disposition, and credit.
GitHub open/closed state is tracked separately.

| PR / artifact | Reviewed head | Disposition | Evidence level | Credit | Notes |
|---|---|---|---|---|---|
| [#5](https://github.com/discoveryathome/miller-rabin/pull/5) preprint-scope | f7808fb | merged; A2 closed (corrections in #9) | author-checked, independently-checked, maintainer-reviewed | Claude (AI agent), acknowledgement | Same-model fresh-context recheck: confirmed with corrections |
| [#6](https://github.com/discoveryathome/miller-rabin/pull/6) first-explicit-t1, bach-transfer | f1f86d8 | merged; superseded as frontier by #8 | author-checked, independently-checked, maintainer-reviewed | Claude (AI agent), acknowledgement | C = 4.2; recheck confirmed, minor fixes in #9 |
| [#8](https://github.com/discoveryathome/miller-rabin/pull/8) zero-pairing | (merge head) | accepted on merge; frontier | author-checked, independently-checked, maintainer-reviewed | Claude (AI agent), acknowledgement | C = 0.529; adversarial review + independent recheck confirmed |
