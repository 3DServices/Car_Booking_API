from django.shortcuts import render
from django.http import FileResponse
from fpdf import FPDF
from api.models import *


def report_generator():

    queryset = PassengerTrip.objects.all()
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'These are all the trips of this month ', 0, 1)
    pdf.cell(40, 10, '', 0, 1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Destination'.ljust(10)} {'Pick_up_location'.rjust(10)} {'Passenger'.ljust(10)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)

    for line in queryset:
        pdf.cell(200, 8, f"{line.trip.destination.ljust(10)} {line.trip.pick_up_location.rjust(7)}{line.passenger.user.username.rjust(18)}", 0, 1)

    report = pdf.output('report.pdf', 'F')
    return report
