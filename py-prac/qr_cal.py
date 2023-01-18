# %% [markdown]
# ## Calendar & Schedule creator
#
# ## QR Code creator
#

# %%
from pyzbar import pyzbar
import cv2
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styledpil import StyledPilImage
import qrcode
from datetime import datetime, timedelta
import datetime
import calendar
from pytz import timezone
import pytz
import pyttsx3
import icalendar


def schedule_day() -> None:
    tasks: dict = {}
    while True:
        task: str = input("Enter task (or 'q' to quit): ")
        if task == 'q':
            break
        importance: int = int(input('Enter level of importance \
            (1-3): '))
        tasks[task] = importance

    now = datetime.datetime.now(timezone('US/Eastern'))
    for task, importance in tasks.items():
        if importance == 1:
            event_time = now + datetime.timedelta(days=1)
        elif importance == 2:
            event_time = now + datetime.timedelta(days=2)
        elif importance == 3:
            event_time = now + datetime.timedelta(days=3)

        # need to use the iCalendar library instead
        calendar.event(task, event_time)
        print(f'Event created: {task} on {event_time}')

        engine = pyttsx3.init()
        engine.say(f'Don\t forget to {task} on {event_time}')
        engine.runAndWait()


# %%
# Return a datetime.tzinfo implementation \
# for the given timezone
# *! ToDo -> datetime module example


utc = timezone('UTC')
eastern = timezone('US/Eastern')
eastern.zone
# 'US/Eastern'
# timezone(unicode('US/Eastern')) is eastern
# True
utc_dt = datetime(2002, 10, 27, 6, 0, 0, tzinfo=utc)
loc_dt = utc_dt.astimezone(eastern)
fmt = '%Y-%m-%d %H:%M:%S %Z (%z)'
loc_dt.strftime(fmt)
# '2002-10-27 01:00:00 EST (-0500)'
(loc_dt - timedelta(minutes=10)).strftime(fmt)
# '2002-10-27 00:50:00 EST (-0500)'
eastern.normalize(loc_dt - timedelta(minutes=10)).strftime(fmt)
# '2002-10-27 01:50:00 EDT (-0400)'
(loc_dt + timedelta(minutes=10)).strftime(fmt)
# '2002-10-27 01:10:00 EST (-0500)'


# %% [markdown]
# # QR Code functions
#
# - URLS for data param
#   - "https://www.himabalde.netlify.app"
#   - "https://raw.githubusercontent.com/bahim22/bahim22/master/himacard.png"
#   - "https://avatars.githubusercontent.com/u/78245175?v=4"
#

# %%


def gen_rd_qr(data: str, color: list[str], **round: bool):
    """
        creates a QRCode => PilImage .png fi
        :param data = URL of what the QRCode points to
        :param color = a list of 2 str for fill color and back color
        :param round = option param to round edges
        ! Best version
    """
    qr = qrcode.QRCode(
        version=1, box_size=15, border=4, error_correction=qrcode.constants.ERROR_CORRECT_H
    )
    qr.add_data(data, optimize=10)
    qr.make(fit=True)

    if round == True:
        img11 = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer()
        )
        return img11.save('round_qrcode.png')
    else:
        img0 = qr.make_image(
            fill_color=color[0], back_color=color[1])
        return img0.save('qr_color.png')


# %%
gen_rd_qr(data='https://avatars.githubusercontent.com/u/78245175?v=4',
          round=True, color=['yellow', 'black'])
# works; created round_qrcode.png


# %%
data = 'https://avatars.githubusercontent.com/u/78245175?v=4'
gen_rd_qr(data, round=False, color=['yellow', 'black'])
# works; created qr_color.png


# %%
# v2 QRCode func for pic or rounded


def qr_pic_rd(data: str, pic: bool):
    """ returns a PilImage saved as a png fi \
        containing a QR Code w/ \
        a pic in the center or rounded blocks
        * Good Version
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=4
    )
    # qr.add_data(data, optimize=5)
    qr.add_data(data, optimize=10)
    qr.make(fit=True)

    """
        version w/ image in center of QRCode | rounded
    """
    if pic:
        img11 = qr.make_image(image_factory=StyledPilImage,
                              embeded_image_path="himacard.png")
        return img11.save('qr_base_pic.png')
    else:
        img1 = qr.make_image(image_factory=StyledPilImage,
                             module_drawer=RoundedModuleDrawer())
        return img1.save('qr_base_rd.png')

# previous version called the func w/ data preset and saved 1 version
# data = "https://www.github.com/bahim22"
# img = generate_qr(data, pic=False)
# img.save('qr_code33.png')


# %%
qr_pic_rd(data="https://www.himabalde.netlify.app", pic=False)


# %%
qr_pic_rd(data="https://www.himabalde.netlify.app", pic=True)


# %%
# v3 QRCode func
# from PIL import Image

# def generate_qr(data: str, pic: bool, color: list)-> BaseImage | PilImage | Any:


def generate_qr1(data: str, color: list[str], **pic: bool):
    """
        :param data = URL of what the QRCode points to
        :param color = a list made of 2 str to identify the fill color and back color
        :param pic = optional param to put pic in center of code
        !  need to adjust pic to get input from user that is a path to saved image
        * (this is version after og, prior to fixing errors)
    """
    qr = qrcode.QRCode(
        version=1,
        # error correction can be L, M, Q | H[highest]
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=4
    )
    # data to add and optimize: 0<= int <=20
    qr.add_data(data, optimize=10)
    qr.make(fit=True)

    """
        version w/ ctr img | rounded | color
    """
    if pic == True:
        img1 = qr.make_image(image_factory=StyledPilImage,
                             embeded_image_path="himacard.png")
        return img1.save('pic_qrcode.png')
    elif pic == False:
        img11 = qr.make_image(image_factory=StyledPilImage,
                              module_drawer=RoundedModuleDrawer())
        return img11.save('round_qrcode.png')
    # elif not pic & color == ['white', 'blue']:
    # elif not pic & color == [str, str]:
    #     img11 = qr.make_image(
    #         fill_color=color[0], back_color=color[1])
    #     return img11
    else:
        img0 = qr.make_image(
            fill_color=color[0], back_color=color[1])
    return img0.save('color_qrcode.png')
    # img2 = qr.make_image(
    #     fill_color='black', back_color='red')
    # return img2
# img = img11.save('qr_code55.png')


# %%
generate_qr1(data="https://www.himabalde.netlify.app",
             color=['blue', 'black'], pic=True)

generate_qr1(data="https://www.himabalde.netlify.app", color=['white', 'blue'])
# worked, returned white, blue qrcode


# %%


def read_qr(img_path):
    # read image from fi
    img2 = cv2.imread(img_path)

    # find QR codes
    decoded = pyzbar.decode(img2)

    # extract data from QRcodes
    for obj in decoded:
        return obj.data.decode()


# test read_qr func
qr_data = read_qr('qr_code.png')
print(qr_data)


# %% [markdown]
# ## Contacting via cards and online
#
# # Address, CC, BCC, subject, body
#
# mailto:someone@yoursite.com?cc=someoneelse@theirsite.com,another@thatsite.com,me@mysite.com&bcc=lastperson@theirsite.com&subject=Big%20News&body=Body%20goes%20here.
#
# MECARD:N:Hima Balde;ORG:Dionysus Era;TEL:4125555555;URL:https\://dev--himabalde.netlify.app/;EMAIL:ibalde@dionysuseradev.onmicrosoft.com;ADR:Pennsylvania;NOTE:Information Technology and Development ServicesCEO;;
#
# BEGIN:VEVENT
# SUMMARY:req event
# DTSTART;VALUE=DATE:20240113
# DTEND;VALUE=DATE:20240114
# LOCATION:Pittsburgh
# DESCRIPTION:event description!
# END:VEVENT
#
# MECARD:N:Owen,Sean;ADR:76 9th Avenue, 4th Floor, New York, NY 10011;TEL:12125551212;EMAIL:srowen@example.com;;
#
# BEGIN:VCARD
# VERSION:3.0
# N:Owen;Sean;;;
# FN:Sean Owen
# TITLE:Software Engineer
# EMAIL;TYPE=INTERNET;TYPE=WORK;TYPE=PREF:srowen@google.com
# URL;TYPE=Homepage:https://example.com
# END:VCARD
#
# BEGIN:VEVENT
# SUMMARY:Summer+Vacation!
# DTSTART:20180601T070000Z
# DTEND:20180831T070000Z
# END:VEVENT
#
# WIFI:T:WPA;S:mynetwork;P:mypass;;
#
# BEGIN:VEVENT
# SUMMARY:Summer+Vacation!
# DTSTART:20180601T070000Z
# DTEND:20180831T070000Z
# END:VEVENT
#
