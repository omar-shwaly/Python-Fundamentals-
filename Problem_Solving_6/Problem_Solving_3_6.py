from datetime import date, datetime

today_date = date.today()
future_date = input("Enter your date\n").strip()
future_date = datetime.strptime(future_date, f"%d/%m/%Y").date()

remaining = future_date - today_date
print("#" * 50)
print(f"Today Date is :{today_date}")
print("#" * 50)
print(f"Future Date is :{future_date}")
print("#" * 50)
print(f"Time  remaining until this date = {remaining.days} days")
print("#" * 50)
