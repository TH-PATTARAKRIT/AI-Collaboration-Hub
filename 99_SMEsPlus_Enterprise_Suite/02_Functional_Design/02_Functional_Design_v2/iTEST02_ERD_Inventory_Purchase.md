# iTEST02 ERD - Inventory Purchase

Source dump: `iTEST02_2026-06-14_14-41-19.dump`

This ERD is a readable module-level extraction from the PostgreSQL custom dump. It intentionally limits the number of tables and edges so reviewers can understand the functional relationships without opening the full 1,395-table schema.

## Scope

- Module: `Inventory_Purchase`
- Tables in module: 169
- Tables shown in ERD: 18
- Full foreign key inventory: see `iTEST02_foreign_keys.csv`

## Mermaid ERD

```mermaid
erDiagram
  PRODUCT_PRODUCT {
    int id PK
    int product_tmpl_id FK
    int create_uid
    int write_uid
    string default_code
    string barcode
    string combination_indices
    json standard_price
  }
  STOCK_LOCATION {
    int id PK
    int location_id FK
    int company_id FK
    int removal_strategy_id FK
    int cyclic_inventory_frequency
    int warehouse_id FK
    int storage_category_id FK
    int create_uid
  }
  STOCK_WAREHOUSE {
    int id PK
    int company_id FK
    int partner_id FK
    int view_location_id FK
    int lot_stock_id FK
    int wh_input_stock_loc_id FK
    int wh_qc_stock_loc_id FK
    int wh_output_stock_loc_id FK
  }
  PRODUCT_TEMPLATE {
    int id PK
    int sequence
    int categ_id FK
    int uom_id FK
    int company_id FK
    int color
    int create_uid
    int write_uid
  }
  STOCK_MOVE {
    int id PK
    int sequence
    int company_id FK
    int product_id FK
    int product_uom
    int location_id FK
    int location_dest_id FK
    int location_final_id FK
  }
  STOCK_PICKING_TYPE {
    int id PK
    int color
    int sequence
    int sequence_id FK
    int default_location_src_id FK
    int default_location_dest_id FK
    int return_picking_type_id FK
    int warehouse_id FK
  }
  STOCK_PICKING {
    int id PK
    int backorder_id FK
    int return_id FK
    int location_id FK
    int location_dest_id FK
    int picking_type_id FK
    int partner_id FK
    int company_id FK
  }
  PURCHASE_ORDER {
    int id PK
    int partner_id FK
    int dest_address_id FK
    int currency_id FK
    int invoice_count
    int fiscal_position_id FK
    int payment_term_id FK
    int incoterm_id FK
  }
  STOCK_MOVE_LINE {
    int id PK
    int picking_id FK
    int move_id FK
    int company_id FK
    int product_id FK
    int product_uom_id FK
    int package_id FK
    int lot_id FK
  }
  STOCK_ROUTE {
    int id PK
    int sequence
    int supplied_wh_id FK
    int supplier_wh_id FK
    int company_id FK
    int create_uid
    int write_uid
    json name
  }
  STOCK_PACKAGE {
    int id PK
    int package_type_id FK
    int location_id FK
    int company_id FK
    int parent_package_id FK
    int package_dest_id FK
    int create_uid
    int write_uid
  }
  PURCHASE_ORDER_LINE {
    int id PK
    int sequence
    int product_uom_id FK
    int product_id FK
    int order_id FK
    int company_id FK
    int partner_id FK
    int create_uid
  }
  STOCK_LOT {
    int id PK
    int product_id FK
    int company_id FK
    int location_id FK
    int create_uid
    int write_uid
    string name
    string ref
  }
  STOCK_RULE {
    int id PK
    int sequence
    int company_id FK
    int location_dest_id FK
    int location_src_id FK
    int route_id FK
    int route_sequence
    int picking_type_id FK
  }
  PRODUCT_TEMPLATE_ATTRIBUTE_VALUE {
    int id PK
    int product_attribute_value_id FK
    int attribute_line_id FK
    int product_tmpl_id FK
    int attribute_id FK
    int color
    int create_uid
    int write_uid
  }
  STOCK_SCRAP {
    int id PK
    int company_id FK
    int product_id FK
    int product_uom_id FK
    int lot_id FK
    int package_id FK
    int owner_id FK
    int picking_id FK
  }
  STOCK_WAREHOUSE_ORDERPOINT {
    int id PK
    int warehouse_id FK
    int location_id FK
    int product_id FK
    int replenishment_uom_id FK
    int company_id FK
    int route_id FK
    int create_uid
  }
  PURCHASE_REQUEST_LINE {
    int id PK
    int product_uom_id FK
    int request_id FK
    int company_id FK
    int analytic_account_id FK
    int requested_by
    int assigned_to
    int supplier_id FK
  }
  PRODUCT_TEMPLATE ||--o{ PRODUCT_PRODUCT : "product_tmpl_id"
  PRODUCT_TEMPLATE ||--o{ PRODUCT_TEMPLATE_ATTRIBUTE_VALUE : "product_tmpl_id"
  PRODUCT_TEMPLATE ||--o{ PRODUCT_TEMPLATE : "product_revise_id"
  STOCK_LOCATION ||--o{ PURCHASE_ORDER_LINE : "location_final_id"
  PURCHASE_ORDER ||--o{ PURCHASE_ORDER_LINE : "order_id"
  STOCK_WAREHOUSE_ORDERPOINT ||--o{ PURCHASE_ORDER_LINE : "orderpoint_id"
  PRODUCT_PRODUCT ||--o{ PURCHASE_ORDER_LINE : "product_id"
  STOCK_PICKING_TYPE ||--o{ PURCHASE_ORDER : "picking_type_id"
  STOCK_WAREHOUSE_ORDERPOINT ||--o{ PURCHASE_REQUEST_LINE : "orderpoint_id"
  PRODUCT_PRODUCT ||--o{ PURCHASE_REQUEST_LINE : "product_id"
  STOCK_LOCATION ||--o{ STOCK_LOCATION : "location_id"
  STOCK_WAREHOUSE ||--o{ STOCK_LOCATION : "warehouse_id"
  STOCK_LOCATION ||--o{ STOCK_LOT : "location_id"
  PRODUCT_PRODUCT ||--o{ STOCK_LOT : "product_id"
  PURCHASE_REQUEST_LINE ||--o{ STOCK_MOVE : "created_purchase_request_line_id"
  STOCK_LOCATION ||--o{ STOCK_MOVE_LINE : "location_dest_id"
  STOCK_LOCATION ||--o{ STOCK_MOVE_LINE : "location_id"
  STOCK_LOT ||--o{ STOCK_MOVE_LINE : "lot_id"
  STOCK_MOVE ||--o{ STOCK_MOVE_LINE : "move_id"
  STOCK_PACKAGE ||--o{ STOCK_MOVE_LINE : "package_id"
  STOCK_PICKING ||--o{ STOCK_MOVE_LINE : "picking_id"
  PRODUCT_PRODUCT ||--o{ STOCK_MOVE_LINE : "product_id"
  STOCK_PACKAGE ||--o{ STOCK_MOVE_LINE : "result_package_id"
  STOCK_LOCATION ||--o{ STOCK_MOVE : "location_dest_id"
  STOCK_LOCATION ||--o{ STOCK_MOVE : "location_final_id"
  STOCK_LOCATION ||--o{ STOCK_MOVE : "location_id"
  STOCK_WAREHOUSE_ORDERPOINT ||--o{ STOCK_MOVE : "orderpoint_id"
  STOCK_MOVE ||--o{ STOCK_MOVE : "origin_returned_move_id"
  STOCK_PICKING ||--o{ STOCK_MOVE : "picking_id"
  STOCK_PICKING_TYPE ||--o{ STOCK_MOVE : "picking_type_id"
```

## Selected tables

- `product_product`
- `stock_location`
- `stock_warehouse`
- `product_template`
- `stock_move`
- `stock_picking_type`
- `stock_picking`
- `purchase_order`
- `stock_move_line`
- `stock_route`
- `stock_package`
- `purchase_order_line`
- `stock_lot`
- `stock_rule`
- `product_template_attribute_value`
- `stock_scrap`
- `stock_warehouse_orderpoint`
- `purchase_request_line`
