# ABU Integrated ERP System (AIES)
![image](https://github.com/ademoord/abu_tech_test/assets/69139708/0133923e-44c1-4ec8-881b-d69e1fe4ba4a)

This repo consists of two Odoo custom module:
1. abu_sale
2. abu_website_vendor

# Sale Stock Picking Stored Procedure
The stored procedure that going to create a picking record everytime a sale order confirmed is placed in a SQL file, at the root directory. You can simply execute that using PGadmin, Navicat or your favorite PostgreSQL client.

# Usage of Endpoint
Go to http://[your-server-address]/api/products - [GET] to retrieve and display all of the products stored in the Odoo DB with some details.

# AIES Sale and Purchase Dashboard
The Sale and Purchase Dashboard is built 100% only using Odoo's front-end (OWL). It is placed in parent Menu just like showed in the screenshot below.
![image](https://github.com/ademoord/abu_tech_test/assets/69139708/2f674d4b-d532-4286-9c38-9c8791856b68)

# AIES Vendor Portal
This portal website will work properly only if you fulfill the dependencies that consists of these modules:
- Website
- Discuss
- Purchase
- Portal
Here are the list of endpoints and their screenshots in this portal:
- /my/contacts --> to shows all of the listed vendors
![image](https://github.com/ademoord/abu_tech_test/assets/69139708/64ea2eca-0501-42a2-b0ff-92ca4bb526c9)
- /my/contacts/<int> --> to shows vendor with desired id
![image](https://github.com/ademoord/abu_tech_test/assets/69139708/91e1649f-3603-4304-9435-9c33e199e6bb)
- /contact_request_form --> to create new vendor
![image](https://github.com/ademoord/abu_tech_test/assets/69139708/89d2da32-87bd-4b7d-8608-344a93412763)

