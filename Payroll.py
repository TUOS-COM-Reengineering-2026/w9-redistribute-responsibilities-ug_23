from PaySchedule import PaySchedule


class Payroll:
    def __init__(self):
        self.pay_dates = None
        self.pay_schedules = {"Manager": PaySchedule("1st")}


    def get_schedule(self, staff_category):
        return self.pay_schedules.get(staff_category)

    def get_staff_category_pay_day(self, staff_category):
        self.pay_dates =self.get_schedule(staff_category).get_pay_date()
        return self.pay_dates

    def update_category_date(self, category, new_date):
        schedule = self.pay_schedules.get(category)
        if schedule:
            schedule.set_pay_date(new_date)