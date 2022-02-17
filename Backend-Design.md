# Design

Design documentation for the for book library


## Backend

Backend data we need is as follows:

__Books__

- Title
- Author
- ISDN Number
- Published Date
- Edition
- Synopsis

__Person (borrower)__

- First Name
- Last Name
- Phone
- Email
- Addresss

__Loaning__

- Person
- Book
- Date loaned
- Date Due

Actions that will auto trigger:

- When someone borrows a book it gets date due get populated with 14days after it was loaned. Add late charges ( $1 a day) to users who are late.
- Trigger reminder notification when return date is due
- Log all transactions from Creation, updates, deletions everything.