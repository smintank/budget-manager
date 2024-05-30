## Budget API (in developing)

### About
Api service for an automation of financial transaction records and budget control. Powered by FastAPI framework and Sqlite3 DB. 
Allows to avoid routine actions when managing own budget by automation and decreasing manual touch. Works together only with Apple Shortcut on ios.

#### About shortcut:
The shortcut automatically tracks SMSes from banks on iPhone and send it in POST request to server.
[Download the shortcut.](https://www.icloud.com/shortcuts/e5d3a6c244e7403eb7fa56cabb0fd2ac)

### TODO:
iOS Shortcut Features
- [X] Track income SMSes from certain sender
- [X] Write text in file if no internet connection
- [X] Setup automation to read text from files and send it to server
- [ ] Send SMS's text in POST API request

FastApi Features
- [ ] FastApi install
- [ ] Raw endpoint handler
- [ ] Add models
- [ ] Authorization and Authentication 
- [ ] Parse messages
- [ ] Add transaction in SQLite3 DB
- [ ] Celery (maybe?)

Telegram-Bot Features 
- [ ] Install aiogram
- [ ] Ask handle unparsed messages manually with inline menu
- [ ] Adding expenses and incomes manually with inline menu
- [ ] Financial statistic (day, week, month, year, custom period)
- [ ] Debts and payments reminder

Deprecated feature
- [ ] Adding expenses and incomes in Google Sheets

Frontend
- Planned in future

Testing
- [ ] Tests covering

Deploy
- [ ] Docker
- [ ] Nginx
- [ ] CI/CD

### Api Endpoints
```
POST    /api/v1/budget/raw/
```

Planned soon:
```
POST    /api/v1/budget/expence/
GET     /api/v1/budget/expences/
GET     /api/v1/budget/expence/{exprnce_id}/
DELETE  /api/v1/budget/expence/{exprnce_id}/

POST    /api/v1/budget/income/
GET     /api/v1/budget/incomes/
GET     /api/v1/budget/income/{income_id}/
DELETE  /api/v1/budget/income/{income_id}/
```

### Install

#### 1. Shortcut install
Open [the shortcut link](https://www.icloud.com/shortcuts/e5d3a6c244e7403eb7fa56cabb0fd2ac) on your iPhone and download it.
