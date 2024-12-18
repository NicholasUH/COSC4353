from status import Status

def evaluate_application(application):
    return (Status.PASS, "Applicant is good financially.") if application.employment or application.credit_records else \
        (Status.FAIL, "Applicant not good financially")
