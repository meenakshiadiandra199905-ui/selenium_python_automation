### Day 1 – Requirement Analysis & Scope Definition
Project: E-commerce Website – Shopping Cart Testing
Domain: Web Application Testing (Manual + Automation Ready)

## Project Overview
The purpose of this project is to test the Shopping Cart module of an e-commerce website. The shopping cart allows users to add products, update quantities, remove products, view total prices, and proceed to checkout.

## Features to be Tested
- Add product to cart
- Remove product from cart
- Increase/decrease quantity
- Auto-update total price
- Stock validation
- Navigate to checkout

## Functional Requirements
1. User should be able to add a product to the cart.
2. User should be able to update item quantity.
3. Cart should automatically update total price.
4. User should be able to remove items from the cart.
5. Quantity should not exceed available stock.
6. Cart should not accept zero or negative values.

## Assumptions
- User is already logged in.
- Payment functionality is out of scope.
- Desktop browser testing only.

## Out of Scope
- Payment gateway testing
- Login functionality
- Mobile responsiveness
- Performance testing

## Acceptance Criteria
- Cart functions work without errors.
- Prices update correctly.
- User can proceed to checkout.

### Day 2 – Test Plan
## Test Plan Overview
This test plan describes the testing approach, scope, resources, and schedule for validating the Shopping Cart module of an e-commerce application.

## Test Objective
- To verify all cart functionalities work as expected
- To identify functional and UI defects
- To ensure accurate price and quantity calculations

## Scope of Testing
### In Scope
- Add to cart
- Remove from cart
- Update quantity
- Price calculation
- Stock validation
- Checkout navigation

### Out of Scope
- Payment gateway
- Login and authentication
- Order history

## Types of Testing
- Functional Testing
- UI Testing
- Regression Testing
- Negative Testing

## Test Environment
- Browser: Google Chrome
- OS: Windows 10
- Testing Type: Manual Testing

## Entry Criteria
- Application is accessible
- Shopping cart feature is available
- Test data is prepared

## Exit Criteria
- All planned test cases executed
- Major defects logged
- Test summary prepared

## Risks
- Incorrect price calculation
- Cart not updating in real time
- Stock mismatch

## Deliverables
- Test scenarios
- Test cases
- Bug reports
- Test summary report


### Day 3 – Test Scenarios
## Test Scenarios for Shopping Cart Module
### Add to Cart
1. Verify user can add a product to the cart from product listing page
2. Verify user can add a product to the cart from product detail page
3. Verify cart icon updates item count after adding product

### Update Quantity
4. Verify user can increase product quantity in cart
5. Verify user can decrease product quantity in cart
6. Verify total price updates when quantity is changed
7. Verify user cannot set quantity to zero
8. Verify user cannot set quantity to negative value

### Remove from Cart
9. Verify user can remove a product from the cart
10. Verify cart is empty after removing all products

### Price Validation
11. Verify total price calculation is correct
12. Verify price updates correctly after removing a product
13. Verify tax/discount is applied correctly (if applicable)

### Stock Validation
14. Verify user cannot add quantity more than available stock
15. Verify appropriate error message is displayed for stock limit

### Navigation
16. Verify user can proceed to checkout from cart
17. Verify cart retains items when navigating back from checkout

### Negative Scenarios
18. Verify cart behavior when internet connection is lost
19. Verify cart behavior on page refresh
20. Verify cart handles unexpected input gracefully

### Day 4 – Detailed Test Cases
## Test Cases for Shopping Cart Module
| TC ID | Test Case Description | Preconditions | Test Steps | Expected Result | Priority |
|------|----------------------|---------------|------------|-----------------|----------|
| TC_01 | Add product to cart | User on product page | Click Add to Cart | Product added to cart | High |
| TC_02 | Increase quantity | Product added to cart | Increase quantity | Quantity increases | High |
| TC_03 | Decrease quantity | Quantity > 1 | Decrease quantity | Quantity decreases | Medium |
| TC_04 | Remove product | Product in cart | Click Remove | Product removed | High |
| TC_05 | Update total price | Multiple items in cart | Update quantity | Total price updates | High |
| TC_06 | Prevent zero quantity | Product in cart | Set quantity to 0 | Error shown | High |
| TC_07 | Prevent negative quantity | Product in cart | Set quantity to -1 | Error shown | High |
| TC_08 | Stock limit validation | Limited stock product | Increase quantity beyond stock | Error displayed | High |
| TC_09 | Cart persistence | Items in cart | Refresh page | Cart retains items | Medium |
| TC_10 | Proceed to checkout | Items in cart | Click Checkout | Navigates to checkout | High |

### Day 5 – Bug Report Writing
## Bug Reports – Shopping Cart Module
### Bug 1
- Bug ID: BUG_01
- Title: Cart total price not updating after quantity change
- Module: Shopping Cart
- Severity: High
- Priority: High
- Description: When user increases the product quantity, the total price remains unchanged.
- Steps to Reproduce:
  1. Add a product to cart
  2. Increase quantity
- Expected Result: Total price should update automatically
- Actual Result: Total price does not update

### Bug 2
- Bug ID: BUG_02
- Title: Negative quantity allowed in cart
- Module: Shopping Cart
- Severity: High
- Priority: High
- Description: System allows user to enter negative values in quantity field.
- Steps to Reproduce:
  1. Add product to cart
  2. Enter -1 in quantity field
- Expected Result: Error message should be shown
- Actual Result: Quantity updates incorrectly

### Bug 3
- Bug ID: BUG_03
- Title: Cart items removed after page refresh
- Module: Shopping Cart
- Severity: Medium
- Priority: Medium
- Description: Cart does not retain items after refreshing the page.
- Steps to Reproduce:
  1. Add items to cart
  2. Refresh browser
- Expected Result: Cart should retain items
- Actual Result: Cart becomes empty

### Bug 4
- Bug ID: BUG_04
- Title: Checkout button enabled for empty cart
- Module: Shopping Cart
- Severity: Medium
- Priority: Medium
- Description: Checkout button is enabled even when cart is empty.
- Steps to Reproduce:
  1. Open cart without items
- Expected Result: Checkout button should be disabled
- Actual Result: Checkout button is enabled

### Bug 5
- Bug ID: BUG_05
- Title: No error message when stock limit exceeded
- Module: Shopping Cart
- Severity: High
- Priority: High
- Description: System does not show error when quantity exceeds available stock.
- Steps to Reproduce:
  1. Add limited stock product
  2. Increase quantity beyond stock
- Expected Result: Stock limit error message
- Actual Result: Quantity increases without warning



