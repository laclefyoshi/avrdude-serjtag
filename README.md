
serjtag patches for avrdude
===========================

How to use
----------

patch

    $ tar zxvf bin/avrdude-5.11.1.tar.gz
    $ cd avrdude-5.11.1
    $ (linux optional) patch -p1 < ../src/avrdude-5.8-baud.patch
    $ patch -p1 < ../src/avrdude-5.10-serjtag.patch
    $ patch -p1 < ../src/avrdude-5.11-serjtag.patch
    $ patch -p1 < ../src/avrdude-5.8-ft245r.patch
    $ patch -p1 < ../src/avrdude-5.11-ft245r.patch
    $ patch -p1 < ../src/avrdude-5.8-confu2.patch

build (after installing [d2xx drivers](http://www.ftdichip.com/Drivers/D2XX.htm))


    $ (usb optional) brew install libusb-compat
    $ ./configure CFLAGS="-g -O2 -DSUPPORT_FT245R" LIBS="-lftd2xx" --prefix=/opt/usr/avrdude
    $ make
    $ sudo make install

check

    $ otool -L /opt/usr/avrdude/bin/avrdude
    /opt/usr/avrdude/bin/avrdude:
        /opt/homebrew/lib/libusb-0.1.4.dylib (compatibility version 9.0.0, current version 9.4.0)
        /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 744.18.0)
        /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)
        /opt/homebrew/lib/libusb-1.0.0.dylib (compatibility version 2.0.0, current version 2.0.0)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 169.3.0)
        /usr/lib/libedit.3.dylib (compatibility version 2.0.0, current version 3.0.0)
        /usr/lib/libncurses.5.4.dylib (compatibility version 5.4.0, current version 5.4.0)
        /usr/local/lib/libftd2xx.1.2.2.dylib (compatibility version 0.1.0, current version 1.2.2)

Please read README of original avrdude-serjtag for using serjtag and FT232R/FT245R.

