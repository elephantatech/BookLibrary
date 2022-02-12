# Design

Design documentation for the for book library


## Backend

Backend data we need is as follows

Books
    - Title
    - Author
    - ISDN Number
    - Published Date
    - Edition
    - Synopsis

Person (borrower)
    - First Name
    - Last Name
    - Phone
    - Email
    - Addresss

Loaning
    - Person
    - Book
    - Date loaned
    - Date Due

Actions that will auto trigger
    - When someone borrows a book it gets date due get populated with 14days after it was loaned. Add late charges ( $1 a day) to users who are late.
    - Trigger reminder notification when return date is due
    - Log all transactions from Creation, updates, deletions everything.