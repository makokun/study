#!/usr/bin/env python
# -*- coding:utf8 -*-

import smtplib,sys
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email.Header import Header

print sys.argv[1]

addr=''
pass=''

from_address = "<%s>" % addr
to_address   = sys.argv[1]
mail_subject = u'テスト'.encode('iso-2022-jp')
mail_body    = u'本文'.encode('iso-2022-jp')

msg            = MIMEText(mail_body, 'plain', 'iso-2022-jp')
msg['Subject'] = Header(mail_subject, 'iso-2022-jp')
msg['From']    = from_address
msg['To']      = to_address
msg['Date']    = formatdate()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login(addr, pass)
s.sendmail(from_address, [to_address], msg.as_string())
s.close()


