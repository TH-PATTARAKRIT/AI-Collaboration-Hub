P10-ENUM-03 DEPLOYED-DATABASE CORRELATION  (executed 2026-09-04)
PATH SET: $HOME/Downloads/*.dump   -- 4 dumps found, 3 readable
TOOLING : pg_restore and psql present; no server required (schema and per-table
          data extracted directly from the archives)

=== iTEST02_2026-07-14_16-34-51 ===
  SCHEMA EXTRACTION FAILED: unsupported version (1.16) in file header
  -> class C, NOT SEARCHED. Written to a newer archive format than the local tool.

=== BK12MAY26_2026-08-03_05-48-30 ===   schema bytes: 4323210
  hits[deferred_start_date]                        = 10   -> on public.account_move_line
  hits[deferred_end_date]                          = 10
  hits[account_move_deferred_rel]                  = 16   -> table present
  hits[generate_deferred_expense_entries_method]   = 16   -> on public.res_company
  hits[CREATE TABLE public.account_asset ]         = 1
  hits[CREATE TABLE public.account_loan]           = 4
  hits[CREATE TABLE public.account_transfer_model] = 0    -> ABSENT
  hits[account_account_res_company_rel]            = present
  public.account_account has NO company_id column  -> chart is many-to-many only
  data[account_account_res_company_rel] rows 545 (artefact bytes 12k+)
     -> 544 distinct accounts, 11 distinct companies, 1 account in >1 company
  data[res_company] rows 44, 195 columns (artefact bytes 1612691)
     -> ALL 44 companies: generate_deferred_expense=on_validation,
        calc_expense=month, generate_deferred_revenue=on_validation,
        calc_revenue=month.  Asymmetric expense/revenue settings: 0
     -> 43 of 44 companies have at least one deferral account or journal set
  data[account_move_deferred_rel] rows 0  (artefact bytes 886 = header only,
     i.e. the table is genuinely empty, not a failed extraction)

=== iEVING_2026-07-23_10-31-06 ===   schema bytes: 4250585
  identical structural result to BK12MAY26 on every probe above
  data[account_account_res_company_rel] rows 544
     -> 544 distinct accounts, 11 distinct companies, 0 accounts in >1 company
  data[res_company] rows 44, 188 columns (artefact bytes 1459141)
     -> ALL 44 companies on on_validation/month for both directions;
        asymmetric settings: 0; 43 of 44 provisioned
  data[account_move_deferred_rel] rows 0 (artefact bytes 886 = header only)

=== iSMEs_2026-07-11_05-03-27 ===   schema bytes: 3096408
  hits[deferred_start_date]                        = 0
  hits[deferred_end_date]                          = 0
  hits[account_move_deferred_rel]                  = 0
  hits[generate_deferred_expense_entries_method]   = 0
  hits[CREATE TABLE public.account_asset ]         = 1
  hits[CREATE TABLE public.account_loan]           = 0
  hits[CREATE TABLE public.account_transfer_model] = 3    -> PRESENT
  hits[account_account_res_company_rel]            = 0
  public.account_account HAS company_id integer NOT NULL -> scalar chart shape
  -> The deferred revenue/expense function has no physical structure in this
     deployed database.  Class A, scope = this database.
