# myPNRStatus
A script in python3 to check PNR status on your terminal

## Installation

This script uses `requests` which requires python 3.6 or higher runtime.
```
pip3 install -r requirements.txt
```

## Usage

### As script

```
bash$ python3 main.py
Enter your PNR: 8606850987

*** You Queried For : PNR Number: 8606850987 ***
Charting Status: No	No. of Passengers: 1

  Train Number  Train Name      Boarding Date    From          To              Reserved Upto    Boarding Point    Class
--------------  --------------  ---------------  ------------  --------------  ---------------  ----------------  -------
         15635  DWARKA EXPRESS  10-08-2018       AHMEDABAD JN  NEW JALPAIGURI  NEW JALPAIGURI   VADODARA JN       3A

  S. No.  Booking Status (Coach No , Berth No., Quota)    *Current Status (Coach No , Berth No.)
--------  ----------------------------------------------  ----------------------------------------
       0  RLWL/-/25/GN                                    RLWL/-/11/GN
```

## TODO

- [x] Test with waiting tickets for single passenger.
- [x] Test with waiting tickets for multi-passenger.
- [x] Test with confirmed tickets.
