from . import controller

ROUTING={
    "index":controller.start,
    "master":controller.master,
    "login":controller.loginpage,
    "registration":controller.register,
    "classes":controller.classmaster,
    "subjects":controller.subjectmaster,
    "session":controller.sessionmaster,
    "exam":controller.exammaster,
    "fees":controller.feesmaster,
    "assignsubject":controller.assignsub,
    "assignsubject":controller.assignsub,
    "assignclass":controller.assigncls,
    "institutereg":controller.institutemaster,
    "seniorstudentreg":controller.seniorRegistration,
    "studentdetails":controller.Studentdetails,
}