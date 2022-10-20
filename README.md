# Skipthelineubc 

## Introduction

Skipthelineubc is an online food ordering system website serving ubco students across different vendors in the UNC building. The web application provide services for vendors, staffs and customers (students) on campus. This application is a food ordering system which has three interfaces i.e. vendor, admin and customer. 

### Functionalities:

Each user can interact with the system to perform an activity.

The login page has three navigation tabs allowing different types of user to log in accordingly.

The options avaliable to the Admin are edit vendor list, update vendor logo, add/remove vendors, and view vendor analytics.

The options available to the Vendor are add food category, add food details, add delivery person, assign delivery person to an order, update food order, view food details, view revenue and delete order.

The options available to the Customer are view menu, sign up and log in, create an order, checkout and view order details and status.

### Language used:

Python/Flask web framework; HTML/CSS/JavaScript

### Breakdown of the code structure:

----This needs to get updated----
1. /main - application source files
   - model.py contains user model classes
   - view.py blueprint of web views in subclasses
   - /template where individual html pages get stored
1. app.py - holds the codes for the web application - I think

## How to run the program?

Download the project files and run `flask run` command in the terminal.
