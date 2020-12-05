#envelope size: 110 by 145 mm

# Elliot Torres
# 4321 Loser Road
# La Crescenta, CA 91214
#
# Ryan Lee
# 1234 Boomer Road
# La Crescenta, CA 91214

import os
from dotenv import load_dotenv, find_dotenv
from fpdf import FPDF
import pathlib

load_dotenv(find_dotenv())

# types out address on envelope

sender_name = os.environ['sender_name']
sender_addr1 = os.environ['sender_addr1']
sender_addr2 = os.environ['sender_addr2']

recipient_name = os.environ['recipient_name']
recipient_addr1 = os.environ['recipient_addr1']
recipient_addr2 = os.environ['recipient_addr2']

pdf = FPDF('L', 'mm', (110, 145))
pdf.add_page()
pdf.set_font('Times', '', 9.8)
pdf.set_margins(0, 0, 0)

pdf.text(7, 7.5, sender_name)
pdf.text(7, 10.5, sender_addr1)
pdf.text(7, 13.5, sender_addr2)

pdf.set_font('Times', '', 14)
pdf.text(44, 78, recipient_name)
pdf.text(44, 82, recipient_addr1)
pdf.text(44, 86, recipient_addr2)

# types out message on back fo envelope

pdf.add_page()
pdf.set_margins(0, 0, 0)
message = f"Happy Birthday {recipient_name}! From the CVHS Bday Team and from Dr. Neat! Have a wonderful day and enjoy your sweet!"

pdf.text(44, 78, message)

envelope_file = pathlib.Path('envelope.pdf')
if envelope_file.exists():
    envelope_file.unlink()
pdf.output('envelope.pdf', dest='F').encode('latin-1')
