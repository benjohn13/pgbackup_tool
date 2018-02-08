# Manual testing after all other testing and coding is thought
# to be complete at this stage

# (pgbackup-E7nj_BsO) [pgbackup $] 
# (pgbackup-E7nj_BsO) [pgbackup $] PYTHONPATH=./src python
Python 2.7.5 (default, Aug  4 2017, 00:39:18) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-16)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> from pgbackup import pgdump
>>> ip_address = os.getenv("SERVER_IP")
>>> dump = pgdump.dump("postgres://demo:password@%s:80/sample" % ip_address)
>>> dump.stdout.read()
"--\n-- PostgreSQL database dump\n--\n\n-- Dumped from database version 9.6.6\n-- Dumped..."


# Another test
>>> dump = pgdump.dump("postgres://demo:password@%s:80/sample" % ip_address)
>>> f = open('dump.sql', 'w')
>>> f.write(dump.stdout.read())
>>> f.close()
>>> exit()
# (pgbackup-E7nj_BsO) [pgbackup $] 
# (pgbackup-E7nj_BsO) [pgbackup $] cat dump.sql
--
-- PostgreSQL database dump
--
-- Dumped from database version 9.6.6
-- Dumped by pg_dump version 9.6.7
SET statement_timeout = 0;
SET lock_timeout = 0;
...
...
...
980     Roldan  Smorthit        rsmorthitr7@example.com Male    #7717f0
981     Rockwell        Playfair        rplayfairr8@example.com Male    #22dd26
982     Jessa   Beckson jbecksonr9@example.com  Female  #06329a
983     Mariann Lawful  mlawfulra@example.com   Female  #db9635
984     Forester        Helkin  fhelkinrb@example.com   Male    #8323d5
985     Hynda   Hall-Gough      hhallgoughrc@example.com        Female  #c5727b
986     Carena  Doleman cdolemanrd@example.com  Female  #ca1629
987     Sheila-kathryn  Shadfourth      sshadfourthre@example.com       Female  #ea90e5
988     Jdavie  Rosel   jroselrf@example.com    Male    #cabc92
989     Sheilakathryn   Ogus    sogusrg@example.com     Female  #0f513d
990     Yolane  Jeanes  yjeanesrh@example.com   Female  #239ef6
991     Ewan    Marcus  emarcusri@example.com   Male    #1b911b
992     Marsha  Tomasi  mtomasirj@example.com   Female  #786d5c
993     Vivia   Screwton        vscrewtonrk@example.com Female  #465af2
994     Ragnar  Brewitt rbrewittrl@example.com  Male    #1478c3
995     Arri    Kempton akemptonrm@example.com  Male    #bf3e44
996     Rich    Fearnehough     rfearnehoughrn@example.com      Male    #71a10c
997     Rosamond        Vergine rverginero@example.com  Female  #fdc545
998     Malinde Powell  mpowellrp@example.com   Female  #766951
999     Teirtza Loadman tloadmanrq@example.com  Female  #096c18
1000    Killie  Peperell        kpeperellrr@example.com Male    #c523eb
\.
--
-- PostgreSQL database dump complete
--
# (pgbackup-E7nj_BsO) [pgbackup $] 