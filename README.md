                                            OFFICIAL PROJECT FROM DDSINFOTECH https://instagram.com/ddsinfotech
                                            
# THE APPY `(Artificial Intelligence Model)`

## Developer 
   DHRUV MARATHE 
## What is APPY ?

APPY is an Artificial Intelligence model developed by DDSINFOTECH 
APPY can serve you with the daily tasks and many more things.
The Project will be getting update ASAP (10th Class is going on so be patient)

## Social Media	Links 			

    Instgram: https://instagram.com/ddsinfotech or https://instagram.com/dhruvmarathe
    Twitter:  https://twitter.com/dhruvmarathe18
    Linkden:  https://in.linkedin.com/in/dds-infotech-a274581b8
    Youtube:  https://www.youtube.com/channel/UCi9eDPoQktxRL6VRsJVJrgQ/videos
    Email:    dhruvmarathe18@gmail.com  
    website:  https://ddsinfotech.tk
    Github:   https://github.com/ddsinfotech-offcial/





**Note**: Below are instructions for installing and to run `appy.py` for Windows & linux

# Installation on Windows & Linux
### Steps
      git clone https://github.com/ddsinfotech-offcial/Jarvis-appy.git
      cd Jarvis-appy
      pip3.8 install -r requirement.txt
### Running the program
      python3 appy.py or python appy.py

# Commands

   #### THIS ARE ALL VOICE COMMAND

    1 :- wikipedia
    2 :- play music or new song play kar
    3 :- what is the time
    4 :- open chrome (Change path) 
    5 :- open visual studio code or open code (Change path)
    6 :- open camera
    7 :- send email (please change required email)
    8 :- describe yourself or what are you ment for
    9 :- show commands
    10 :- search on google
    11 :- play video on youtube
    12 :- switch off or  stop or  close 
    14 :- set alarm
    15 :- tell me a joke
    16 :- shut down my laptop
    17 :- restart my laptop
    19 :- next tab or switch window
    20 :- tell me news or latest news
    21 :- where i am or where are we
    22 :- search instagram profile  
    23 :- read pdf (pdf should be there in main folder for these command)
    24 :- location
 
`Above List will get updated soon`
 **Note**: (or) is used for multiple commands 

#### CentOS/RHEL 8

    sudo yum config-manager --set-enabled powertools
    sudo yum install epel-release
    sudo yum install libtool pkgconfig sqlite-devel autoconf automake openssl-devel libpcap-devel pcre-devel rfkill libnl3-devel gcc gcc-c++ ethtool hwloc-devel libcmocka-devel make file expect hostapd wpa_supplicant iw usbutils tcpdump screen zlib-devel

#### openSUSE

    sudo zypper install autoconf automake libtool pkg-config libnl3-devel libopenssl-1_1-devel zlib-devel libpcap-devel sqlite3-devel pcre-devel hwloc-devel libcmocka-devel hostapd wpa_supplicant tcpdump screen iw gcc-c++ gcc ethtool pciutils usbutils

#### Mageia

    sudo urpmi autoconf automake libtool pkgconfig libnl3-devel libopenssl-devel zlib-devel libpcap-devel sqlite3-devel pcre-devel hwloc-devel libcmocka-devel hostapd wpa_supplicant tcpdump screen iw gcc-c++ gcc make

#### Alpine

    sudo apk add gcc g++ make autoconf automake libtool libnl3-dev openssl-dev ethtool libpcap-dev cmocka-dev hostapd wpa_supplicant tcpdump screen iw pkgconf util-linux sqlite-dev pcre-dev linux-headers zlib-dev pciutils usbutils

**Note**: Community repository needs to be enabled for iw

### BSD

#### FreeBSD

    pkg install pkgconf shtool libtool gcc9 automake autoconf pcre sqlite3 openssl gmake hwloc cmocka

#### DragonflyBSD

    pkg install pkgconf shtool libtool gcc8 automake autoconf pcre sqlite3 libgcrypt gmake cmocka

#### OpenBSD

    pkg_add pkgconf shtool libtool gcc automake autoconf pcre sqlite3 openssl gmake cmocka

### OSX

XCode, Xcode command line tools and HomeBrew are required.

    brew install autoconf automake libtool openssl shtool pkg-config hwloc pcre sqlite3 libpcap cmocka

### Windows

#### Cygwin

Cygwin requires the full path to the `setup.exe` utility, in order to
automate the installation of the necessary packages. In addition, it
requires the location of your installation, a path to the cached
packages download location, and a mirror URL.

An example of automatically installing all the dependencies
is as follows:

    c:\cygwin\setup-x86.exe -qnNdO -R C:/cygwin -s http://cygwin.mirror.constant.com -l C:/cygwin/var/cache/setup -P autoconf -P automake -P bison -P gcc-core -P gcc-g++ -P mingw-runtime -P mingw-binutils -P mingw-gcc-core -P mingw-gcc-g++ -P mingw-pthreads -P mingw-w32api -P libtool -P make -P python -P gettext-devel -P gettext -P intltool -P libiconv -P pkg-config -P git -P wget -P curl -P libpcre-devel -P libssl-devel -P libsqlite3-devel

#### MSYS2

    pacman -Sy autoconf automake-wrapper libtool msys2-w32api-headers msys2-w32api-runtime gcc pkg-config git python openssl-devel openssl libopenssl msys2-runtime-devel gcc binutils make pcre-devel libsqlite-devel

## Compiling

To build `aircrack-ng`, the Autotools build system is utilized. Autotools replaces
the older method of compilation.

**NOTE**: If utilizing a developer version, eg: one checked out from source control,
you will need to run a pre-`configure` script. The script to use is one of the
following: `autoreconf -i` or `env NOCONFIGURE=1 ./autogen.sh`.

First, `./configure` the project for building with the appropriate options specified
for your environment:

    ./configure <options>

**TIP**: If the above fails, please see above about developer source control versions.

Next, compile the project (respecting if `make` or `gmake` is needed):

 * Compilation:

    `make`

 * Compilation on *BSD or Solaris:

    `gmake`

Finally, the additional targets listed below may be of use in your environment:

 * Execute all unit testing:

    `make check`

 * Execute all integration testing (requires root):
 
    `make integration`

 * Installing:

    `make install`

 * Uninstall:

    `make uninstall`


###  `./configure` flags

When configuring, the following flags can be used and combined to adjust the suite
to your choosing:

* **with-airpcap=DIR**:  needed for supporting airpcap devices on windows (cygwin or msys2 only)
                Replace DIR above with the absolute location to the root of the
                extracted source code from the Airpcap CD or downloaded SDK available
                online. Required on Windows to build `besside-ng`, `besside-ng-crawler`, 
                `easside-ng`, `tkiptun-ng` and `wesside-ng` when building experimental tools.
                The developer pack (Compatible with version 4.1.1 and 4.1.3) can be downloaded at
                https://support.riverbed.com/content/support/software/steelcentral-npm/airpcap.html

* **with-experimental**: needed to compile `tkiptun-ng`, `easside-ng`, `buddy-ng`,
                    `buddy-ng-crawler`, `airventriloquist` and `wesside-ng`.
                    libpcap development package is also required to compile most of the tools.
                    If not present, not all experimental tools will be built.
                    On Cygwin, libpcap is not present and the Airpcap SDK replaces it.
                    See --with-airpcap option above.

* **with-ext-scripts**: needed to build `airoscript-ng`, `versuck-ng`, `airgraph-ng` and 
                   `airdrop-ng`. 
                   Note: Each script has its own dependencies.

* **with-gcrypt**:   Use libgcrypt crypto library instead of the default OpenSSL.
                And also use internal fast sha1 implementation (borrowed from GIT)
                Dependency (Debian): libgcrypt20-dev

* **with-duma**:	Compile with DUMA support. DUMA is a library to detect buffer overruns and under-runs.
            	Dependencies (debian): duma

* **disable-libnl**:  Set-up the project to be compiled without libnl (1 or 3). Linux option only.

* **without-opt**:  Do not enable stack protector (on GCC 4.9 and above).

* **enable-shared**:   Make OSdep a shared library.

* **disable-shared**: When combined with **enable-static**, it will statically compile Aircrack-ng.

* **with-avx512**:  On x86, add support for AVX512 instructions in aircrack-ng. Only use it when
                    the current CPU supports AVX512.

* **with-static-simd=<SIMD>**: Compile a single optimization in aircrack-ng binary. Useful when compiling
                    statically and/or for space-constrained devices. Valid SIMD options: x86-sse2,
                    x86-avx, x86-avx2, x86-avx512, ppc-altivec, ppc-power8, arm-neon, arm-asimd.
                    Must be used with --enable-static --disable-shared. When using those 2 options, the default
                    is to compile the generic optimization in the binary. --with-static-simd merely allows
                    to choose another one.

* **enable-maintainer-mode**: It is important to enable this flag when developing with Aircrack-ng. This flag enables additional compile warnings and safety features.

#### Examples:

  * Configure and compiling:

    ```
    ./configure --with-experimental
    make
    ```

  * Compiling with gcrypt:

    ```
    ./configure --with-gcrypt
    make
    ```

  * Installing:

    `make install`

  * Installing (strip binaries):
  
    `make install-strip`

  * Installing, with external scripts:

    ```
    ./configure --with-experimental --with-ext-scripts
    make
    make install
    ```

  * Testing (with sqlite, experimental and pcre)

    ```
    ./configure --with-experimental
    make
    make check
    ```

  * Compiling on OS X with macports (and all options):

    ```
    ./configure --with-experimental
    gmake
    ```

  * Compiling on OS X 10.10 with XCode 7.1 and Homebrew:

    ```
    env CC=gcc-4.9 CXX=g++-4.9 ./configure
    make
    make check
    ```

    *NOTE*: Older XCode ships with a version of LLVM that does not support CPU feature
    detection; which causes the `./configure` to fail. To work around this older LLVM,
    it is required that a different compile suite is used, such as GCC or a newer LLVM
    from Homebrew.

    If you wish to use OpenSSL from Homebrew, you may need to specify the location
    to its' installation. To figure out where OpenSSL lives, run:

    `brew --prefix openssl`

    Use the output above as the DIR for `--with-openssl=DIR` in the `./configure` line:

    ```
    env CC=gcc-4.9 CXX=g++-4.9 ./configure --with-openssl=DIR
    make
    make check
    ```

  * Compiling on FreeBSD with gcc9

    ```
    env CC=gcc9 CXX=g++9 MAKE=gmake ./configure
    gmake
    ```

  * Compiling on Cygwin with Airpcap (assuming Airpcap devpack is unpacked in Aircrack-ng directory)

    ```
    cp -vfp Airpcap_Devpack/bin/x86/airpcap.dll src
    cp -vfp Airpcap_Devpack/bin/x86/airpcap.dll src/aircrack-osdep
    cp -vfp Airpcap_Devpack/bin/x86/airpcap.dll src/aircrack-crypto
    cp -vfp Airpcap_Devpack/bin/x86/airpcap.dll src/aircrack-util
    dlltool -D Airpcap_Devpack/bin/x86/airpcap.dll -d build/airpcap.dll.def -l Airpcap_Devpack/bin/x86/libairpcap.dll.a
    autoreconf -i
    ./configure --with-experimental --with-airpcap=$(pwd)
    make
    ```

 * Compiling on DragonflyBSD with gcrypt using GCC 8

   ```
   autoreconf -i
   env CC=gcc8 CXX=g++8 MAKE=gmake ./configure --with-experimental --with-gcrypt
   gmake
   ```

 * Compiling on OpenBSD (with autoconf 2.69 and automake 1.16)

   ```
   export AUTOCONF_VERSION=2.69
   export AUTOMAKE_VERSION=1.16
   autoreconf -i
   env MAKE=gmake ./configure
   gmake
   ```

 * Compiling and debugging aircrack-ng

   ```
   export CFLAGS='-O0 -g'
   export CXXFLAGS='-O0 -g'
   ./configure --with-experimental --enable-maintainer-mode --without-opt
   make
   LD_LIBRARY_PATH=.libs gdb --args ./aircrack-ng [PARAMETERS]
   ```


# Packaging

Automatic detection of CPU optimization is done at run time. This behavior
**is** desirable when packaging Aircrack-ng (for a Linux or other distribution.)

Also, in some cases it may be desired to provide your own flags completely and
not having the suite auto-detect a number of optimizations. To do this, add
the additional flag `--without-opt` to the `./configure` line:

`./configure --without-opt`

# Using precompiled binaries

## Linux/BSD
 * Use your package manager to download aircrack-ng
 * In most cases, they have an old version.

## Windows
 * Install the appropriate "monitor" driver for your card (standard drivers doesn't work for capturing data).
 * aircrack-ng suite is command line tools. So, you have to open a commandline
   `Start menu -> Run... -> cmd.exe` then use them
 * Run the executables without any parameters to have help

# Documentation


Documentation, tutorials, ... can be found on https://aircrack-ng.org

See also manpages and the forum.

For further information check the [README](README) file

# Infrastructure sponsors

<img src="https://uploads-ssl.webflow.com/5ac3c046c82724970fc60918/5c019d917bba312af7553b49_MacStadium-developerlogo.png" alt="MacStadium" width="150" height="61">









