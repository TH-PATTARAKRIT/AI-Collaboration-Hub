# QID Executor State Machine

`ELIGIBLE-A1 -> A1-RUNNING -> A1-QID-SEALED | A1-CORRECTION-REQUIRED | A1-HOLD`

A2 remains `WAITING-RUNTIME-ACCESS-CONTRACT` until a separate blind runtime/config observation profile is independently verified. While A2 is blocked, the executor continues unaffected A1 modules from frozen W1 batches and maintains WIP up to 4.
